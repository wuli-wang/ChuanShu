#coding: utf-8
from app.config_default import Config as DefaultConfig

class Config(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wyq63409564@localhost/yyds?charset=utf8'