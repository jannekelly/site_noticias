import os

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    absPath = os.path.dirname(os.path.abspath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(absPath,'allnews.db')


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}