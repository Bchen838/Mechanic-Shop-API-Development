class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456BrianC$@localhost/mechanic_db'
    DEBUG = True

class TestingConfig:
    pass

class ProductionConfig:
    pass