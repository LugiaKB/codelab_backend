import dj_database_url

from codelab_backend.settings.base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}