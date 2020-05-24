from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(9^9dmyww8p5)8lf)k(5eu64=-kz9wlc+m@idcikmsnurwc-aw'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
