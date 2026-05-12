class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456BrianC$@localhost/mechanic_db'
    DEBUG = True


class ProductionConfig:
    pass

class TestingConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
    DEBUG = True 
    CACHE_TYPE = 'SimpleCache'
    RATELIMIT_ENABLED = False