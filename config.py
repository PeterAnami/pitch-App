import os
from dotenv import load_dotenv
load_dotenv()

class Config:
  SQLALCHEMY_TRACK_MODIFICATIONS=True
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/peter'

 
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

  
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

  UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
  if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/peter'
  DEBUG = True

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/peter'

config_options = {
  'production':ProdConfig,
  'development':DevConfig,
  'test':TestConfig
}
