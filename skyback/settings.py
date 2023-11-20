from pathlib import Path
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_b)8vy63ik7q49*tj87-)hqs2o4ont#)+ru^t+_s@x7g1s$r1s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'jet',
    'jet.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'ckeditor',
    'ckeditor_uploader',
    'drf_yasg',
    'blog'
]


MEDIA_URL = '/skyleta/media/'

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'skyback.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'skyback.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    #this is for postgresql when going to production
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'mydb',
    #     'USER': 'myuser',
    #     'PASSWORD': 'mypassword',
    #     'HOST': 'localhost',
    #     'PORT': '5432',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#further custtomizations comes here

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]



REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7)
}

################## file storage ################### cloudinary config


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
  "CLOUD_NAME" : "dhrexohux", 
  "API_KEY" : "232777867795216", 
  "API_SECRET" : "a71Ac7OYmW_162esgquS8AIvRZg"
}




#######################################################################



######## EMAIL CONFIGURATION #########

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'pixel.mxrouting.net'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'team@newgenafrica.co'
# EMAIL_HOST_PASSWORD = 'team033o!Xd'
# EMAIL_USE_SSL = True
# EMAIL_USE_TLS = False

##########################################


############ DJOSER CONFIGURATION #################################

# DJOSER = {
#     'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
#     'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
#     'ACTIVATION_URL': '#/activate/{uid}/{token}',
#     'SEND_ACTIVATION_EMAIL': False, #let's disble first
#     'SEND_ACTIVATION_EMAIL': False, #let's disable first
#     'SEND_CONFIRMATION_EMAIL': False,  #let's disable first
#     'PASSWORD_RESET_CONFIRM_URL': 'reset-password/{uid}/{token}',
#     'USERNAME_RESET_CONFIRM_URL': 'reset-username/{uid}/{token}',
#     'ACTIVATION_FROM_EMAIL': 'team@newgenafrica.co',
# }

########################################################################

CORS_ALLOW_ALL_ORIGINS = True



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'pixel.mxrouting.net'
EMAIL_PORT = 587  # Use the appropriate port for your SMTP server
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'noreply@lachofit.com'
EMAIL_HOST_PASSWORD = 'wgjM0AkK?lacho'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

############################################### CKEDITOR #########################################

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

############################################### CKEDITOR #########################################