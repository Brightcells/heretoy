"""
Django settings for heretoy project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJ_DIR = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&hs@jr%$w%sff4r12&%!^sc)qna@7uzf!%=@o_l*x67un94*22'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'heretoy',
    'accounts',
    'south',
    'eatshit',
    'html5games',
    'data',
    'developer',
    'cogames',
    'games_bak',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mobi.middleware.MobileDetectionMiddleware',
)

UTHENTICATION_BACKENDS = (
    'accounts.backends.UserBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'heretoy.urls'

WSGI_APPLICATION = 'heretoy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# List of callables that know how to import templates from various sources.

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJ_DIR, 'templates'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(PROJ_DIR, "static").replace('\\', '/'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static').replace('\\', '/')

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

MEDIA_URL = '/media/'

DOWNLOADS_ROOT = os.path.join(BASE_DIR, 'downloads').replace('\\', '/')

LOGIN_URL = '/accounts/login'

DOMAIN = 'http://heretoy.com'

APP_DEFAULT_LOGO = 'http://heretoy.com/static/data/img/heretoy_0003s_0000_heretoy.png'

APP_DOWNLOAD_URL_PC = 'http://heretoy.com/static/html5games/downloads/heretoy_1.0.0_C0013.apk'
APP_DOWNLOAD_URL_WAP = 'http://heretoy.com/static/html5games/downloads/heretoy_1.0.0_C0012.apk'
APP_DOWNLOAD_URL_WEIXIN = 'http://a.app.qq.com/o/simple.jsp?pkgname=com.brightcells.heretoy'

GAME_NUM_PER_PAGE = 10
PLAY_NUM_PER_CLICK = 8
LIKE_NUM_PER_CLICK = 8

CONPON = 'http://t.jzt.58.com/weixingamebaggame/binding'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        '': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

from local_settings import *
