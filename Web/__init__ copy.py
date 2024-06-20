
# # 모듈 로딩
# from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy

# # DB관련 인스턴스 생성
# db = SQLAlchemy() # 전역 변수
# migrate = Migrate() # 전역 변수

# # Application Factory 함수
# def create_app():
#     # Flask Server 인스턴스 생성
#     app = Flask(name)

#     # 설정 내용 로딩 (파이썬 파일에서 읽어들인다.)
#     app.config.from_pyfile('config.py')

#     # ORM 즉, DB 초기화 -> db객체를 create_app 안에서 생성하면 블루프린트와 같은 다른 모듈에서 불러올 수 없기 때문에 밖에서 생성.
#     db.init_app(app)
#     migrate.init_app(app, db)

#     # 테이블 클래스
#     from . import modelBuildError

#     # 블루프린트
#     from .views import main_views
#     app.register_blueprint(main_views.bp)

#     # insert_word 함수 호출
#     from .model import Word, Meaning, insert_word, delete_records_from_id

#     with app.app_context():
#         db.create_all()  # 모든 모델에 대한 테이블 생성
#         #insert_word()  # 데이터 입력
#         #delete_records_from_id(1301) # 중복으로 들어간 데이터 삭제.

#     return app