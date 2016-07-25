from base import *
import dj_database_url

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


DATABASES['default'] = dj_database_url.parse(
    "mysql://bec999e1787895:978e9893@eu-cdbr-west-01.cleardb.com/heroku_9b53a7d93e26e04")



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEBUG = False
ALLOWED_HOSTS = ['cryptic-cliffs-51895.herokuapp.com']
# SECURITY WARNING: don't run with debug turned on in production!
