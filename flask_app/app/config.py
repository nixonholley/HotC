import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    ENV = os.getenv('ENV', 'development')

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'