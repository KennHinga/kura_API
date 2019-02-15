import os

postgres_link = "postgres://postgres@localhost:5432"
database_name = 'kura'


class Config:

    """ Parent configuration class """

    DEBUG = False
    TESTING = False
    DATABASE_URI = postgres_link + database_name
    APP_SETTINGS = os.getenv('development')


class DevelopmentConfig(Config):

    """ Configuration for development environment """

    DEBUG = True
    TESTING = False
    DATABASE_URI = postgres_link + database_name
    os.environ['ENV']= 'development'

class TestingConfig(Config):

    """ Configuration for the testing environment """

    TESTING = True
    DEBUG = True
    DATABASE_URI = postgres_link + database_name +'_test'
    os.environ['ENV']= 'testing'

    
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}