import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'l(+sdl8f5dh47t*%jyblveol7yw#!qb3lu&#_wecv)buj72_jl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# try:
#     from .local_settings import *
# except InmportError:
#     pass

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'corsheaders',
    'rest_auth',
    'rest_auth.registration',
    'rest_framework',
    'rest_framework.authtoken',

    'bootstrap4',

    'property',
    'agents',
    'about',
    'contact',
    'home',
    'register',
    'chat',
    'channels',
    'build',
    'todos',
    # 'todo',
    # 'build-test',
    # 'public'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
            # 'public'
            os.path.join(BASE_DIR, 'reactapp2-1/build'),
            os.path.join(BASE_DIR, 'talk/build'),
        ],
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

WSGI_APPLICATION = 'project.wsgi.application'
ASGI_APPLICATION = 'project.routing.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# import dj_database_url
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'name',
#         'USER': 'user',
#         'PASSWORD': '',
#         'HOST': 'host',
#         'PORT': '',
#     }
# }
# db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
# DATABASES['default'].update(db_from_env)
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# カスタムユーザーを使う
AUTH_USER_MODEL = 'register.User'

# ログインページと、直接ログインページへ行った後のリダイレクトページ
LOGIN_URL = 'register:login'
LOGIN_REDIRECT_URL = 'register:top'

# STATIC_URL = '/static/'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
if not DEBUG:
    import dj_database_url
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'name',
            'USER': 'user',
            'PASSWORD': '',
            'HOST': 'host',
            'PORT': '',
        }
    }
    db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'].update(db_from_env)
    # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    SECRET_KEY = os.environ['SECRET_KEY']
    import django_heroku #追加
    django_heroku.settings(locals()) #追加

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'public', 'build', "static"),
# ]
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = 'test@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
DEFAULT_FROM_EMAIL = 'test2019reiwafirst@gmail.com'
EMAIL_HOST_USER = 'test2019reiwafirst@gmail.com'
EMAIL_HOST_PASSWRD = 'kacywxkyjgsmitpf'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

# authentication settings

SITE_ID = 1
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 'EXCEPTION_HANDLER': 'djangotodo.todos.utils.custom_exception_handler'
}
CORS_ORIGIN_WHITELIST = (
    'localhost:3000/',
    'localhost:3000',
    '127.0.0.1:3000/',
    '127.0.0.1:3000',
    '127.0.0.1:8000/',
    '127.0.0.1:8000',
)
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'none'
CSRF_COOKIE_NAME = "csrftoken"

HOST_URL = 'https://justdjango-chat.herokuapp.com'
if DEBUG:
    HOST_URL = 'http://127.0.0.1:8000'