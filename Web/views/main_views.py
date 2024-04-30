from flask import Blueprint, render_template, request
from ..model import Word, Meaning

bp = Blueprint('main',
               __name__,
               template_folder='templates',
               url_prefix = '/')

## 라우팅 함수들
@bp.route('/')
def index() : 
    return render_template('index.html')

@bp.route('/topik1')
def topik1():
    page = request.args.get('page', type=int, default=1)
    per_page = 20  # 한 페이지당 표시할 단어 수
    word_list = Word.query.filter(Word.level == '1급').order_by(Word.id.asc()).paginate(page=page, per_page=per_page)
    return render_template('topik1.html', word_list=word_list)

@bp.route('/topik2')
def topik2():
    page = request.args.get('page', type=int, default=1)
    per_page = 20  # 한 페이지당 표시할 단어 수
    word_list = Word.query.filter(Word.level == '2급').order_by(Word.id.asc()).paginate(page=page, per_page=per_page)
    return render_template('topik2.html', word_list=word_list)

@bp.route('/mylist')
def mylist():
    # 개인 단어장 페이지 구현
    return render_template('mylist.html')

from sqlalchemy.sql.expression import func

@bp.route('/leveltest', methods=['GET', 'POST'])
def leveltest():
    if request.method == 'POST':
        score = 0
        for i in range(8):
            answer = request.form.get(f'answer_{i}', '')
            word_id = request.form.get(f'word_id_{i}', '')
            word = Word.query.get(word_id)
            if answer == word.voca.rstrip("0-9"):
                score += 1
        return render_template('leveltest_result.html', score=score)
    else:
        words = Word.query.order_by(func.rand()).limit(8).all()
        return render_template('leveltest.html', words=words)

@bp.route('/writing')
def writing():
    # 레벨 테스트(문장) 페이지 구현
    return render_template('writing.html')

@bp.route('/pronunciation')
def pronunciation():
    # 발음 연습 페이지 구현
    return render_template('pronunciation.html')