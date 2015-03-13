"""
Django settings for freegather project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uimgxe$&66g%k0ibk70_tva2q%x)r8+ml=7fb%p#01k(v1$2cg'

# SECURITY WARNING: don't run with debug turned on in production!
if socket.gethostname() == 'iZ23au1sj8vZ':
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['*', ]
else:
    DEBUG = True
    TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gather.job',
    'gather.page',
    'gather.rule',
    'xadmin',
    'crispy_forms',
    'reversion',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'freegather.urls'

WSGI_APPLICATION = 'freegather.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if socket.gethostname() == 'iZ23au1sj8vZ':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'freegather',
            'USER': 'root',
            'PASSWORD': 'nidongde',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'freegather',
            'USER': 'root',
            'PASSWORD': '1161hyx',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


TEMPLATE_DIRS = (
    BASE_DIR+'/freegather/templates',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

if socket.gethostname() == 'iZ23au1sj8vZ':
    STATIC_URL = '/static/'
    STATIC_ROOT = '/var/www/webapps/freegather_static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = '/var/www/webapps/freegather_media/'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = 'c:/freegather_static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = 'c:/freegather_media/'
