import os

import app as app_root


class BaseConfig(object):
    pass
    

class DevConfig(BaseConfig):
    """Development configuration options."""
    DEBUG = True


class PrdConfig(BaseConfig):
    """Production configuration options."""
    DEBUG = False
