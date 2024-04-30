from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

## 모듈 로딩
import os


## 다양한 DBMS URI - SQLITE
BASE_DIR = os.path.dirname(__file__)
DB_NAME_SQLITE = 'app.db'

## 다양한 DBMS URI
DB_MYSQL_URI = 'mysql+pymysql://root:5387@localhost:3306/korean_db'           # 원격

# 사용할 DBMS 설정 / SQLALCHEMY_시작 변수명 고정 
SQLALCHEMY_DATABASE_URI = DB_MYSQL_URI # 데이터베이스 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLAlchemy의 이벤트를 처리하는 옵션 ==> 현재 불필요하여 비활성화.


# 위 둘은 환경 변수라서 변수명을 반드시 저걸로 해주어야 함