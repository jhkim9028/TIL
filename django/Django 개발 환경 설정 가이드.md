# Django 개발 환경 설정 가이드

## 가상환경을 만드는 이유



**프로젝트마다 필요한 패키지들이나 여러 가지 세팅이 다르기 때문에 각각의 가상환경을 만들어 폴더 단위로 관리하기 위해 가상환경이 필요하다.**



## 참고 사항

1. 나의 파이썬 버전 확인
   
   - python --version
   
   - 나의 파이썬 버전 : 3.9.13

2. `/` 란 루트를 의미 => 최상위

3. `~` 란 홈을 의미 => 쉽게 말해 C드라이브의 사용자의 사용자ID 폴더

4. **수시로 상대경로 확인**

5. tip> git bash에서 code . 명령어를 통해 vscode 실행 가능





## 가상환경 생성 / 실행

1. git bash 실행

2. 내가 만들고 싶은 곳에 가상환경을 만들 폴더를 생성
   
   - mkdir server
   
   - server는 폴더 이름으로 원하는 이름으로 설정 가능

3. venv를 통해 가상환경 설치
   
   - python -m venv serverpjt
   
   - serverpjt는 가상환경 이름으로 원하는 이름으로 설정 가능
   
   - 가상환경을 설치하면 여러가지 폴더들이 생성되는데 하나씩 들어가서 무엇이 들어있는지 확인
   
   - python -m venv [가상환경 이름]

4. 가상환경 실행
   
   - source serverpjt/Scripts/activate
   
   - 다 입력할 필요없이 단어 앞 3글자 정도 입력 후 tab키를 통해 자동완성 가능
   
   - 가상환경을 종료하기 위해선 deactivate를 입력
   
   - source [가상환경 이름]/Scripts/activate

5. 가상환경 실행하면 `$`위에 (serverpjt) 라고 나온다.

6. Django 설치하기
   
   - pip install django==3.2.13 => 3.2.13버전 설치
   
   - pip install django => 최신버전 설치
   
   - pip list 를 통해 잘 설치되었는지 확인

7. Django에게 setup 명령
   
   - django-admin startproject firstpjt .
   
   - 장고 관리자에게 프로젝트를 시작할건데 프로젝트 이름은 firstpjt 이고 시작폴더는 현재 폴더라는 의미
   
   - `.`는 현재 폴더를 의미
   
   - django-admin startproject [프로젝트 이름] [시작 경로]
   
   - ls 명령어를 통해 확인

8. 서버 구동하기
   
   - python manage.py runserver
   
   - localhost:8000을 브라우저에 입력해서 웹서버 구동 확인
