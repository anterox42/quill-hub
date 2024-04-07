from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
  "DJANGO_SECRET_KEY",
  default="wYCRw-22tyF8VBkjxsJO08J7cW96ema9WA9fFc-sqZQ4bGdeSr0",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]