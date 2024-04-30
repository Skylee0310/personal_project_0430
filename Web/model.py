# 모듈 로딩
from Web import db


# 클래스 생성
'''
# 클래스 1 Word #
컬럼 : 
- id(index), level, voca, class, guidance
'''
class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(30), nullable=False)
    voca = db.Column(db.Text(), nullable=False)
    wordclass = db.Column(db.Text(), nullable=False)
    guidance = db.Column(db.Text(), nullable=True)
    meaning = db.relationship('Meaning', uselist=False, back_populates='word')

'''
# 클래스 2 meaning #
컬럼 : 
- id2(index-고유식별자), word_index(FK), meaning
'''
class Meaning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id', ondelete='CASCADE'))
    word = db.relationship('Word', back_populates='meaning')
    meaning = db.Column(db.Text(), nullable=False)

def insert_word() :
    import pandas as pd
    df = pd.read_csv('C:/Users/KDP-48/PythonProject/Data/KDT-HTML/personal_project/txt/topikI_jp', 
                     usecols=['등급', '어휘', '품사', '길잡이말', 'jp'])
    df = df.fillna('')
    for n in range(df.shape[0]) :
        word = Word.query.filter_by(voca=df.iloc[n, 1]).first()
        word = Word(level=df.iloc[n,0], voca=df.iloc[n,1], wordclass=df.iloc[n,2], guidance=df.iloc[n,3])
        db.session.add(word)
        db.session.flush() # Word 객체를 데이터베이스에 저장하고 id 값을 생성

        # Meaning 레코드 생성
        meaning = Meaning(word_id=word.id, meaning=df.iloc[n,4])
        db.session.add(meaning)
    db.session.commit()

    print('데이터를 성공적으로 입력하였습니다.')

# 실행할 때마다 insert_word가 적용되는 바람에 생긴 중복 데이터를 삭제하기 위해 쓴 함수.
def delete_records_from_id(start_id):
    # start_id부터 끝까지의 모든 레코드 삭제
    words_to_delete = Word.query.filter(Word.id >= start_id).all()

    for word in words_to_delete:
        db.session.delete(word)  # 각 레코드를 삭제

    db.session.commit()  # 변경 내용을 데이터베이스에 반영

    print(f'{len(words_to_delete)}개의 레코드를 성공적으로 삭제했습니다.')