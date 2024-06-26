# 개인 프로젝트

![image](https://github.com/Skylee0310/personal_project_0430/assets/155412049/22dc4918-7a45-4793-8a9e-dd804fbbe566)

### 📝 주제 선정
=> 외국인 학생을 위한 TOPIK 단어장

### ✏ 주제 선정 배경
- 각 학교 학급 별 한국어 교육 환경 편차 大 (기자재 부족)
=> 태국인 학생을 위한 한국어 TOPIK 단어장 프로그램 개발

### ✏ 데이터 정보 및 수집 방법
- TOPIK 1~6급 단어 크롤링
  - 한국교육바다(https://kleocean.com/토픽-어휘-topik-vocab/)
 
### ✏ 기능 (목표)
- TOPIK 급수별 단어 목록을 통해 의미 학습하기
- 개인 단어장 생성
- 레벨 테스트 (어휘)
- 문장 분석을 통한 학생 급수 평가
- 발음 연습

### ✏ 기능 (구현) 2024년 04월 30일 기준
- TOPIK 1급 단어 목록
- TOPIK 2급 단어 목록 
- 레벨 테스트 (어휘)

### ✏ 사용 스킬 
- 파이썬 : 함수, Pandas
- SQL : DB
- 크롤링
- 웹 페이지 : FLASK

### ✏ 진행 과정
- '한국교육바다'에서 TOPIK 어휘 크롤링
- 데이터 가공
  - 크롤링을 통해 txt로 저장한 어휘 목록을 with 구문을 이용해서 읽어오기
  - 필요한 내용을 각각의 리스트에 담아서 저장
  - 데이터 프레임 생성
  - topik I 어휘 목록 생성 후 csv 파일로 저장
  - 일본어 의미 라벨링 (1300개)
- 데이터베이스 구축
  - DBeaver 23.3.3에서 단어장으로 쓸 데이터베이스 korean_db 생성
- 데이터베이스 연결 및 테이블 생성
 - Word, Meaning 테이블 생성(클래스 사용)
 - 테이블에 csv 파일을 입력하는 insert_word 함수 생성
 - 중복 데이터 삭제를 위해 지정된 범위의 값을 삭제하는 delete_recodes_from_id 함수 생성

<hr></hr>

✏  **웹 구현**
![image](https://github.com/Skylee0310/personal_project_0430/assets/155412049/6b41ed81-00ec-436e-ba70-99c8503a5711)

![image](https://github.com/Skylee0310/personal_project_0430/assets/155412049/bf952527-e1d1-406c-9aee-00c785cbf911)

