#-*-coding:utf-8-*-
"""
Django settings for jkservice project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')t38#guxk@wq#dv=o90xq7@q^6k_rtfvz8%j#(-cmde*6jf7m1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'houses',
    'news',
    'feedback',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jkservice.urls'

WSGI_APPLICATION = 'jkservice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb',
        'USER': 'django',
        'PASSWORD': 'KVZr7dpA(jfXHgi',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = '/var/jkservice/static'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'

CAPTCHA_LENGTH = 7

CAPTCHA_NOISE_FUNCTIONS = False

CAPTCHA_OUTPUT_FORMAT = u'<div class="col-xs-6 text-right" onclick="captcha_refresh()" title="Кликните, чтобы обновить изображение.">%(image)s %(hidden_field)s</div><div class="col-xs-6 text">%(text_field)s</div>'

MEDIA_ROOT = "/var/jkservice/media/"

MEDIA_URL = "/media/"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'jkserviceserver@gmail.com'
EMAIL_HOST_PASSWORD = '405and110fwys'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
