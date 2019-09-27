import os

DEBUG = os.environ.get('DEBUG', "False") == "True"
ENV = os.environ.get('ENV', "DEVELOPMENT")

if ENV == "DEVELOPMENT":
    from .dev import *
if ENV == "PRODUCTION":
    from .prod import *