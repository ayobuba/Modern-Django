from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY',default='nila1v6c7@lco3ox$_#7+avovg8*qk5_n9p5&f9osz83)=$r_v')
DEBUG = env.bool('DJANGO_DEBUG',True)