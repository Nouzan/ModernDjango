from .base import *

SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='d1*z8w2)4$u-6xd)2mv7!^7olwqp**2#0*__db#=gd&4x(thtr'
)

DEBUG = env.bool('DJANGO_DEBUG', default=True)
