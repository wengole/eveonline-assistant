import os
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin
    'suit',
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'south',  # Database migration helpers:
    'crispy_forms',  # Form layouts
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'users',  # custom users app
    # Your stuff: custom apps go here
    'skills',
    'characters',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

INSTALLED_APPS += (
    # Needs to come last for now because of a weird edge case between
    #   South and allauth
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    #'allauth.socialaccount.providers.google',
    'debug_toolbar'
)
########## END APP CONFIGURATION

########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
)
########## END MIDDLEWARE CONFIGURATION

########## DEBUG
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG

########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
#       In production, this is changed to a values.SecretValue() setting
SECRET_KEY = "CHANGEME!!!"
########## END SECRET CONFIGURATION

########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    join(BASE_DIR, 'fixtures'),
)
########## END FIXTURE CONFIGURATION

########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
########## END EMAIL CONFIGURATION

########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Ben Cole', 'wengole@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION

########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = 'postgres://localhost/assistant'
########## END DATABASE CONFIGURATION

########## CACHING
# Do this here because thanks to django-pylibmc-sasl and pylibmc memcacheify is painful to install on windows.
# memcacheify is what's used in Production
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}
########## END CACHING

########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Europe/London'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-gb'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION

########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    # Your stuff: custom template context processers go here
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    join(BASE_DIR, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap3'
########## END TEMPLATE CONFIGURATION

########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'staticfiles')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION

########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = join(BASE_DIR, 'media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION

########## URL Configuration
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'
########## End URL Configuration

########## AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
########## END AUTHENTICATION CONFIGURATION

########## Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "users:redirect"
########## END Custom user app defaults

########## SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
########## END SLUGLIFIER

########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION

########## End mail settings

########## django-debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}
########## end django-debug-toolbar