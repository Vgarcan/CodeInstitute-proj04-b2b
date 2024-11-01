"""
Django settings for _core project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.contrib.messages import constants as messages


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get(('DJANGO_DEBUG'), False)

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1',
                 'localhost', '192.168.1.163', '192.168.2.116']

# MEDIA SETTINGS
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# # STATIC SETTINGS
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ALLAUTH apps:
    # The following apps are required:
    'allauth',
    'allauth.account',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    # Extra Apps:
    # Utilities for implementing Modified Preorder Tree Traversal with your Django Models and working with trees of Model instances.
    'mptt',
    # Project's APPs:
    'main',
    'users',
    'products',
    'orders',


]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 9,
        },
    }
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
            'secret': os.environ.get('GOOGLE_SECRET'),
            'key': os.environ.get('GOOGLE_ID')
        }
    }
}

ROOT_URLCONF = '_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # `allauth` needs this from django
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_USER_MODEL = 'users.User'  # Overrides Django's included ABSTARCTUSER

SITE_ID = 1

# ALLAUTH SETTINGS
"""
AllAuth settings:
This section contains configuration settings for Django Allauth, which provides 
authentication, registration, and account management features. These settings 
control how user accounts are handled, how email verification works, and how 
users log in and register.
"""

# >>> Email Settings
# Ensures that each email address is unique for every account. Users cannot register with an email that is already in use.
ACCOUNT_UNIQUE_EMAIL = True
# Requires that users provide an email address when registering.
ACCOUNT_EMAIL_REQUIRED = True
# Specifies that email verification is optional. Other options are 'mandatory' or 'none'.
# 'mandatory' means users must verify their email to use the account.
ACCOUNT_EMAIL_VERIFICATION = 'none'
# Prefix added to the subject of all outgoing emails from the application, such as verification or password reset emails.
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'XemiDevs'
# Sets the number of days before an email confirmation link expires.
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

# >>> Login/Logout Settings
# URL to redirect users when they need to log in. This is usually the login page of the site.
LOGIN_URL = '/accounts/login/'
# Allows users to log in using either their username or email address.
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# URL to redirect users after they log out. In this case, it's set to the homepage ('/').
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
# URL to redirect users after they successfully log in.
LOGIN_REDIRECT_URL = '/'
# Automatically log in users immediately after they confirm their email address, skipping the login step.
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# >>> Signup Settings
# Requires users to provide a username during the signup process.
ACCOUNT_USERNAME_REQUIRED = True
# Sets the minimum length required for usernames to 3 characters.
ACCOUNT_USERNAME_MIN_LENGTH = 3
# Sets the minimum length required for passwords to 8 characters.
ACCOUNT_PASSWORD_MIN_LENGTH = 8
# Requires users to input their email address twice during signup to prevent typos.
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
# Requires users to input their password twice during signup to prevent typos.
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
# URL to redirect users to after they successfully complete the signup process.
ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/signup-success'
# Defines a list of usernames that cannot be registered, such as 'admin'.
ACCOUNT_USERNAME_BLACKLIST = ['admin',]

# >>> Password Reset Settings
# Defines the expiration time for password reset links (in days). After 2 days, the link will expire.
ACCOUNT_PASSWORD_RESET_TIMEOUT_DAYS = 2

# >>> Security Settings
# Ensures that all URLs generated by Allauth use HTTPS by default, enhancing security.
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

# >>> Custom Form Settings
# Custom forms used by Allauth for various actions like signup, login, and password reset.
ACCOUNT_FORMS = {
    # Custom form for user registration.
    'signup': 'users.forms.CustomSignupForm',
    'login': 'allauth.account.forms.LoginForm',  # Custom form for user login.
    # Custom form for adding an additional email to an account.
    'add_email': 'allauth.account.forms.AddEmailForm',
    # Custom form for changing the user's password.
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    # Custom form for requesting a password reset.
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    # Custom form for resetting the password using a reset key.
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordFromKeyForm',
}

WSGI_APPLICATION = '_core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'users.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_DIR / "static",
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Mesages Tags settings
# https://docs.djangoproject.com/en/5.1/ref/contrib/messages/#message-tags

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',  # BOOTSTRAP
}
