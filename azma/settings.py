"""
Django settings for azma project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.jonin(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'stat')
COMPRESS_ROOT = os.path.join(BASE_DIR, 'stat')


# COMPRESS_CSS_FILTERS = [
# #creates absolute urls from relative ones
# 'compressor.filters.css_default.CssAbsoluteFilter',
# #css minimizer
# 'compressor.filters.cssmin.CSSMinFilter'
# ]
# COMPRESS_JS_FILTERS = [
# 'compressor.filters.jsmin.JSMinFilter'
# ]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#mmm(c*ezo)q(!z3@7xdcrgv88960a5ryvz2+8n1i235tr2r4d'
INTERNAL_IPS = ['localhost', '127.0.0.1']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# COMPRESS_ENABLED = True

ALLOWED_HOSTS = ['*']

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)

TEMPLATE_CONTEXT_PROCESSORS = (
    'exam.context_processor.categories',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'zinnia.context_processors.version',
)

AUTH_PROFILE_MODULE = 'user_profile.models.UserProfile'

# Application definition

INSTALLED_APPS = (
    'azma_cms',
    'south',
    'compressor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'exam',
    'user',
    'answer',
    'Postchi',
    'user_profile',
    'wage_meter',
    'tutorial',
    'rest_framework',
    'django.contrib.sites',
    'tagging',
    'mptt',
    'pytz',
    'feincms',
    'tinymce',
    'feincms.module.page',
    'feincms.module.medialibrary',
    'feincms.module.extensions',
    'elephantblog.navigation_extensions',
    'elephantblog'
)

FEINCMS_USE_PAGE_ADMIN = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'exam.middleware.CommonObjectsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'azma.urls'

WSGI_APPLICATION = 'azma.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'AZMA'),
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'root'),
        'HOST': '127.0.0.1'
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/



LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),  # Assuming BASE_DIR is where your manage.py file is
)

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'queries_above_300ms': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda record: record.duration > 0.0  # output slow queries only
        },
    },
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "log", "logfile"),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
            # 'filters': ['queries_above_300ms'],
        },
        'error_logfile': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "log", "error"),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        }
    },
    'loggers': {
        '*': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'error': {
            'handlers': ['error_logfile'],
            'level': 'ERROR',
            'propagate': True,
        }
    }
}

DEFAULT_LOGIN_URL = '/profile'
DEFAULT_LOGOUT_URL = '/'

#Mail Setting
DEFAULT_FROM_EMAIL = 'noreply@onlinecademy.com'
EMAIL_HOST = 'smtp.onlinecademy.com'
EMAIL_HOST_PASSWORD = 'sorooshMAHDI123'
EMAIL_HOST_USER = 'admin'
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = 'AzmaWeb : '

SERVER_BASE_ADDRESS = 'http://127.0.0.1:8000/'

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.eggs.Loader',
    'app_namespace.Loader',
]

# MEDIA config
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'upload')
MEDIA_URL = '/static/upload/'

# weblog config
SITE_ID = 1


#cms

# FEINCMS_RICHTEXT_INIT_CONTEXT = {
#
# }

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'language': "en",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "right",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_buttons3_add': "ltr,rtl",
    'theme_advanced_path': False,
    'theme_advanced_blockformats': "p,h2,h3",
    'theme_advanced_resizing': True,
    'width': '1300',
    'height': '400',
    #
    'plugins': "table,spellchecker,paste,searchreplace,fullscreen,directionality",
    # 'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}