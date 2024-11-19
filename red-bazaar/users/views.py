from django.shortcuts import render, redirect
from allauth.account.views import LoginView, SignupView
from .forms import CustomUserForm, ProfileForm
from products.models import Product
from orders.models import Order, OrderItem

from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    """
    This function renders the home page of the application.

    Parameters:
    request (HttpRequest): The request object that contains information about the current web request.

    Returns:
    HttpResponse: The rendered home page template.
    """
    return render(request, 'users/home.html')


class CustomLoginView(LoginView):  # CBV
    """
    Custom Login view
    """
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        # Add extra data to the context for the template
        context = super().get_context_data(**kwargs)
        context["extra_message"] = "Loging View from Users APP"
        return context


class CustomSignupView(SignupView):  # CBV
    """
    Custom Signup view
    """
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        # Add extra data to the context for the template
        context = super().get_context_data(**kwargs)
        context["extra_message"] = "Loging View from Users APP"
        return context


@login_required
def profile(request):
    """
    View to display the user's profile.

    This view allows authenticated users to view their profile details.
    The profile page is rendered with a template that displays the user's 
    information and any additional profile-specific information.

    Parameters:
    request (HttpRequest): The request object that contains information about the current web request.
        This object has a 'user' attribute, which represents the authenticated user making the request.

    Returns:
    HttpResponse: The rendered profile page template, which displays the user's information.
    """

    return render(request, 'users/profile.html')


@login_required
def edit_profile(request):
    """
    View to display and update the user's profile.

    This view allows authenticated users to view and edit their profile details.
    The profile consists of two forms: one for the user (username and email) 
    and another for profile-specific information (such as address, country, etc.).

    If the request is a POST, both forms are validated and saved, and the user is 
    redirected back to the profile page. If the request is not a POST, the forms 
    are pre-filled with the current user's data.

    Args:
        request: The HTTP request object, which can be a POST or GET request.

    Returns:
        A rendered HTML page with the user and profile forms, or a redirection 
        to the user's profile page after a successful form submission.
    """
    user = request.user

    # Load the user form and profile form
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST, instance=user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Save user changes
            profile_form.save()  # Save profile changes
            # Redirect to the profile page
            return redirect('users:user_profile')
    else:
        user_form = CustomUserForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)

    return render(request, 'users/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required
def dashboard(request):
    """
    View to display the user's dashboard.
    This view allows authenticated users to view and manage their products, orders, etc.
    """
    user = request.user

    # Data to pass to the template
    context = {
        'user': user,
    }

    if user.role == 'SUP':  # Supplier dashboard
        products = Product.objects.filter(seller_id=user)
        received_orders = Order.objects.filter(
            seller=user).order_by('-id')  # Orders for the supplier

        context['products'] = products
        context['received_orders'] = received_orders

    elif user.role == 'BUY':  # Buyer dashboard
        orders = Order.objects.filter(buyer=user)  # Orders placed by the buyer

        context['orders'] = orders

    return render(request, 'users/dashboard.html', context)
