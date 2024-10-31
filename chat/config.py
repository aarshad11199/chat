import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_#$%@@'
    
    # Database configuration using the provided host, port, username, and password for MySQL
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL') or
        'mysql+pymysql://root:root@127.0.0.1:3306/chat'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
