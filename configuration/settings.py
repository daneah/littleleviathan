import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Set environment variables prepended with LITTLELEVIATHAN_ for configuration
PROJECT_NAME = 'LITTLELEVIATHAN'
PROJECT_VARIABLE_PATTERN = '_'.join((PROJECT_NAME, '{}'))

SECRET_KEY = os.getenv(PROJECT_VARIABLE_PATTERN.format('SECRET_KEY'))

DEBUG = os.getenv(PROJECT_VARIABLE_PATTERN.format('DEBUG'), False) == 'TRUE'

ALLOWED_HOSTS = os.getenv(PROJECT_VARIABLE_PATTERN.format('ALLOWED_HOSTS'), '*').split(',')

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
    'compressor',
]

DEV_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS = BUILTIN_APPS + THIRD_PARTY_APPS + MY_APPS

if DEBUG:
    INSTALLED_APPS += DEV_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SOCIAL_MEDIA = {
    'facebook': 'http://www.facebook.com/littleleviathanmusic',
    'instagram': 'http://www.instagram.com/littleleviathanmusic',
    'twitter': 'http://www.twitter.com/littleleviathan',
    'google_plus': 'http://www.google.com/+LittleLeviathan',
    'last_fm': 'http://www.last.fm/music/Little+Leviathan',
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
    os.path.join(BASE_DIR, 'node_modules'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

ROOT_URLCONF = 'configuration.urls'
WSGI_APPLICATION = 'configuration.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv(PROJECT_VARIABLE_PATTERN.format('DATABASE_NAME')),
        'USER': os.getenv(PROJECT_VARIABLE_PATTERN.format('DATABASE_USER')),
        'PASSWORD': os.getenv(PROJECT_VARIABLE_PATTERN.format('DATABASE_PASSWORD')),
        'HOST': os.getenv(PROJECT_VARIABLE_PATTERN.format('DATABASE_HOST'), 'localhost'),
        'PORT': os.getenv(PROJECT_VARIABLE_PATTERN.format('DATABASE_PORT'), 3306),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = os.getenv(PROJECT_VARIABLE_PATTERN.format('STATIC_URL'), '/static/')
STATIC_ROOT = os.path.join(BASE_DIR, os.getenv(PROJECT_VARIABLE_PATTERN.format('STATIC_ROOT'), 'static'))
MEDIA_URL = os.getenv(PROJECT_VARIABLE_PATTERN.format('MEDIA_URL'), '/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv(PROJECT_VARIABLE_PATTERN.format('MEDIA_ROOT'), 'media'))

COMPRESS_CSS_FILTERS = (
    'compressor.filters.cssmin.CSSMinFilter',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'sass {infile} {outfile}'),
)

COMPRESS_OUTPUT_DIR = ''

FEATURED_ALBUM = 'Little Leviathan'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '-d',
    '--quiet',
    '--with-fixture-bundling',
    '--with-coverage',
    '--cover-package=.',
    '--cover-erase',
    '--cover-branches',
]

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
