import os

from decouple import config
from django.contrib.messages import constants as message_constants


SITE_ID = 1

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.redirects',
]

LOCAL_APPS = [
    'server.auth',
    'client.apps.blog',
    'client.apps.services'
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'ckeditor'
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(BASE_DIR), "templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'server.custom_context_processors.menu.menu',
                'server.custom_context_processors.sessions.session',
                'server.custom_context_processors.site.site',
                'server.custom_context_processors.user.user',
                'server.custom_context_processors.seo.seo',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'

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

LANGUAGE_CODE = 'es-Pa'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

if config('STATIC_ROOT', default=False, cast=bool):
    STATIC_ROOT = '{staticfiles}'.format( staticfiles = os.path.join(os.path.dirname(BASE_DIR), "staticfiles" ))
else:
    STATICFILES_DIRS = [
        os.path.join(os.path.dirname(BASE_DIR), "staticfiles"),
    ]

MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR,os.pardir), 'media')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

MESSAGE_TAGS = {
    message_constants.DEBUG: 'info',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}

SITE_URL = 'http://www.asesaludlaboral.com.ve'

LOGIN_URL = '/auth'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = SITE_URL

PASSWORD_RESET_TIMEOUT_DAYS = 3

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'server.auth.email_backend.EmailBackend',
]

SESSION_COOKIE_AGE = 43200

SESSION_COOKIE_NAME = 'session'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    
    ALLOWED_HOSTS = ['*']

    MESSAGE_LEVEL = message_constants.DEBUG

else:
    ALLOWED_HOSTS = ['www.asesaludlaboral.com.ve',]
    """
    Email conf
    """
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    EMAIL_HOST = config('EMAIL_HOST')
    
    EMAIL_PORT = config('EMAIL_PORT')
    
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    
    EMAIL_USE_SSL = config('EMAIL_USE_SSL')
    
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')