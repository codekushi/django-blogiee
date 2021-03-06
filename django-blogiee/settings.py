import os
import mimetypes

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'test'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

OTP_TOTP_ISSUER = 'Django Blogiee'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'django_summernote',
    'django.contrib.sitemaps',
    'admin_honeypot',
    'django_otp',
    'django_otp.plugins.otp_totp',
#    'PWA',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_otp.middleware.OTPMiddleware',
]

ROOT_URLCONF = 'django-blogiee.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django-blogiee.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'blog/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

X_FRAME_OPTIONS = 'SAMEORIGIN'

#progressive web app data
#PWA_APP_NAME = 'Django Blogiee'
#PWA_APP_DESCRIPTION = "PWA for django Blogiee"
#PWA_APP_THEME_COLOR = '#0A0302'
#PWA_APP_BACKGROUND_COLOR = '#ffffff'
#PWA_APP_DISPLAY = 'standalone'
#PWA_APP_SCOPE = '/'
#PWA_APP_ORIENTATION = 'any'
#PWA_APP_START_URL = '/'
#PWA_APP_STATUS_BAR_COLOR = 'default'
#PWA_APP_ICONS = [
#    {
#        'src': '/static/icons/Django-Blogiee.png',
#        'sizes': '160x160'
#    }
#]
#PWA_APP_ICONS_APPLE = [
#    {
#        'src': '/static/icons/Django-Blogiee.png',
#        'sizes': '160x160'
#    }
#]
#PWA_APP_SPLASH_SCREEN = [
#    {
#        'src': '/static/images/icons/Django-Blogiee.png',
#        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
#    }
#]
#PWA_APP_DIR = 'ltr'
#PWA_APP_LANG = 'en-US'
mimetypes.add_type("application/javascript", ".js", True)
