import logging
import os

from django.http import Http404
from django.utils.log import DEFAULT_LOGGING

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ENVIRONMENT = os.getenv('STAGE', 'dev')
IS_DEVELOPMENT = ENVIRONMENT == 'dev'
IS_STAGING = ENVIRONMENT == 'staging'
IS_PRODUCTION = ENVIRONMENT == 'production'
IS_CI = os.getenv('CI', False) == 'true'

PREPEND_WWW = IS_PRODUCTION

# Set environment variables prepended with LITTLELEVIATHAN_ for configuration
PROJECT_NAME = 'LITTLELEVIATHAN'
PROJECT_VARIABLE_PATTERN = '_'.join((PROJECT_NAME, '{}'))


def get_env_var(var_name, default=None):
    return os.getenv(PROJECT_VARIABLE_PATTERN.format(var_name), default)


SECRET_KEY = get_env_var('SECRET_KEY')

DEBUG = IS_DEVELOPMENT or IS_CI

ALLOWED_HOSTS = get_env_var('ALLOWED_HOSTS', '*').split(',')

ADMINS = (
    ('Dane', 'github@danehillard.com'),
)

BUILTIN_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'main',
]

THIRD_PARTY_APPS = [
    'webpack_loader',
]

DEV_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS = BUILTIN_APPS + THIRD_PARTY_APPS + MY_APPS

if DEBUG:
    INSTALLED_APPS += DEV_APPS

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

SOCIAL_MEDIA = {
    'facebook': 'http://www.facebook.com/littleleviathanmusic',
    'instagram': 'http://www.instagram.com/littleleviathanmusic',
    'twitter': 'http://www.twitter.com/littleleviathan',
    'google_plus': 'http://www.google.com/+LittleLeviathan',
    'last_fm': 'http://www.last.fm/music/Little+Leviathan',
}

ROLLBAR = {
    'access_token': get_env_var('ROLLBAR_ACCESS_TOKEN'),
    'environment': ENVIRONMENT,
    'root': BASE_DIR,
    'exception_level_filters': [
        (Http404, 'ignored'),
    ]
}

BASE_KEYWORDS = [
    'Ann Arbor',
    'Michigan',
    'Ann Arbor Michigan',
    'folk',
    'music',
    'folk music',
    'Ann Arbor musicians',
    'Michigan musicians',
    'independent musicians',
    'Little Leviathan',
    'leviathan',
    'Little Leviathan music',
    'Little Leviathan album',
    'Little Leviathan band',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.template_visible_settings',
            ],
        },
    },
]

TEMPLATE_VISIBLE_SETTINGS = (
    'SOCIAL_MEDIA',
    'BASE_KEYWORDS',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

ROOT_URLCONF = 'configuration.urls'
WSGI_APPLICATION = 'configuration.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_var('DATABASE_NAME'),
        'USER': get_env_var('DATABASE_USER'),
        'PASSWORD': get_env_var('DATABASE_PASSWORD'),
        'HOST': get_env_var('DATABASE_HOST', 'localhost'),
        'PORT': get_env_var('DATABASE_PORT', 3306),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

FEATURED_ALBUM = 'Little Leviathan'

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000

LOGGING_CONFIG = None
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOGGERS = {
    '': {
        'level': 'WARNING',
        'handlers': ['console'],
    },
    'django.server': DEFAULT_LOGGING['loggers']['django.server']
}
LOGGERS.update({
    app: {
        'level': LOG_LEVEL,
        'handlers': ['console'],
        'propagate': False,
    } for app in MY_APPS
})
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server']
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'django.server': DEFAULT_LOGGING['handlers']['django.server']
    },
    'loggers': LOGGERS,
})

if IS_PRODUCTION or IS_STAGING:
    STATICFILES_STORAGE = 'configuration.storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'configuration.storages.MediaStorage'
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

BUCKET_PREFIX = os.getenv('BUCKET_PREFIX')

MEDIA_BUCKET_NAME = f'{BUCKET_PREFIX}-media-{ENVIRONMENT}'
MEDIA_DOMAIN = f'media-{ENVIRONMENT}.littleleviathan.com'
MEDIA_URL = '/media/' if DEBUG else f'https://{MEDIA_DOMAIN}/'

STATIC_BUCKET_NAME = f'{BUCKET_PREFIX}-static-{ENVIRONMENT}'
STATIC_DOMAIN = f'static-{ENVIRONMENT}.littleleviathan.com'
STATIC_URL = '/static/' if DEBUG else f'https://{STATIC_DOMAIN}/'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_IS_GZIPPED = True

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}
