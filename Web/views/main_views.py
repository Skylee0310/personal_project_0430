from flask import Blueprint, render_template, request, redirect, url_for
from ..model import Word, Meaning, MyList
from .. import db  # db 객체 import


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

@bp.route('/mylist', methods=['GET', 'POST'])
def mylist():
    if request.method == 'POST':
        my_word = request.form['my_word']
        my_meaning = request.form['my_meaning']
        new_word = MyList(my_word, my_meaning)
        db.session.add(new_word)
        db.session.commit()
        print('성공적으로 입력되었습니다.')

    # 페이지네이션
    page = request.args.get('page', 1, type=int)
    per_page = 10
    my_words = MyList.query.order_by(MyList.id.asc()).paginate(page=page, per_page=per_page)

    return render_template('mylist.html', my_words=my_words)

# Delete a specific word by index
@bp.route('/delete/<int:index>', methods=['POST'])
def delete_word(index):
    word_to_delete = MyList.query.get(index)
    if word_to_delete:
        db.session.delete(word_to_delete)
        db.session.commit()
        reorder_indexes()  # 삭제 후 인덱스 재정렬
        return redirect(url_for('main.mylist'))  # 삭제 후 리스트 페이지로 리다이렉트
    return '해당 인덱스의 단어가 존재하지 않습니다.'

# Reorder indexes of all words
def reorder_indexes():
    all_words = MyList.query.order_by(MyList.id).all()
    for idx, word in enumerate(all_words, start=1):
        word.id = idx
    db.session.commit()

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