from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser, Profile


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    This function creates a new user profile when a new CustomUser instance is saved.
    It checks if the user is not a superuser and if the instance was created.
    If both conditions are met, it creates a new Profile instance associated with the user.
    If the instance is not new, it saves the existing profile associated with the user.

    Parameters:
    sender (class): The model class sending the signal. In this case, it's the CustomUser model.
    instance (CustomUser): The instance of the CustomUser model that triggered the signal.
    created (bool): A boolean indicating whether the instance was created or updated.
    kwargs (dict): Additional keyword arguments passed to the signal handler.

    Returns:
    None
    """
    if created and not instance.is_superuser:
        Profile.objects.create(user=instance)
        print('Created user profile')
    elif not instance.is_superuser:
        instance.profile.save()
