# pylint: skip-file
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '08a0c9ab-f9fb-48c3-adc7-6f0b90799876'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': ''
    }
}

ALLOWED_HOSTS = ['*']
