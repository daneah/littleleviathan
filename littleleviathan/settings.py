import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Set environment variables prepended with LITTLELEVIATHAN_ for configuration
PROJECT_NAME = 'LITTLELEVIATHAN'
PROJECT_VARIABLE_PATTERN = '_'.join((PROJECT_NAME, '{}'))

SECRET_KEY = os.getenv(PROJECT_VARIABLE_PATTERN.format('SECRET_KEY'))

DEBUG = os.getenv(PROJECT_VARIABLE_PATTERN.format('DEBUG'), False) == 'TRUE'
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = os.getenv(PROJECT_VARIABLE_PATTERN.format('ALLOWED_HOSTS'), '*').split(',')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'context_processors.template_visible_settings',
)

TEMPLATE_VISIBLE_SETTINGS = (
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

ROOT_URLCONF = 'littleleviathan.urls'
WSGI_APPLICATION = 'littleleviathan.wsgi.application'

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
