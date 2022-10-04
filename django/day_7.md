# 실습 정리



- Django란?
  
  - 파이썬 기반 웹 프레임워크(서버를 만들 수 있도록 도와주는 프레임워크)
  1. **url로 `요청`을 받아서**
  
  2. **쿼리에서 `처리`하고**
  
  3. **적절한 `응답`을 해준다.**



- **`MTV`**



## 가상환경 설치 및 실행

- 설치 : python -m venv [가상환경 이름]

- 실행 : source [가상환경 이름]/Scripts/activate



## Django설치 및 프로젝트 생성

- 설치 : pip install django==3.2.13

- 프로젝트 생성 : django-admin startproject [프로젝트 이름] .



## 앱 설치 및 등록

- 설치 : python manage.py startapp [앱 이름]

- 등록 : 프로젝트의 settings.py 중 INSTALLED_APPS 에 앱 이름 등록



------------------------------------------------------------------------------------------------------------

## urls.py에 include로 각각의 앱에서 urls.py로 관리

-  pjt의 urls.py에 include 추가하고 path 추가

- 앱에서 urls.py 생성하고 pjt의 urls.py와 연결



## url을 등록하고, view 함수 생성, templates 만든다



## views.py에 index 추가

- templates 파일에 base.html 만들고 settings.py에서 TEMPLATES의 DIRS에 BASE_DIR/'templates' 추가



________________________________________________________________________________________



## CRUD 기능 구현

- 데이터베이스에 생성, 조회, 수정, 삭제 기능을 활용할 수 있는 사이트를 만든다.

- uI(기능) / DB 



### model에 데이터베이스 설계

- model에서 DB 설계

- python manage.py makemigrations

- python manage.py migrate

- phthon manage.py showmigrations 으로 확인 가능



### 1. 게시글 생성

- 각 기능마다 url에 매핑되는 views함수가 1개 필요

- 기능
  
  - 사용자에게 HTML을 주는 기능
  
  - view함수로 실제 DB에 저장하는 기능
  
  - 이런 기능을 같은 곳에서 처리할 수 없다



1. 사용자에게 HTML Form 제공해, 입력한 데이터를 처리

2. form에서 가장 중요한 것
   
   1. 사용자에게 양식을 제공하고 값(input value)을 받아서 서버에 전송

3. 입력받은 데이터 처리
   
   1. 게시글 DB에 생성하고 index 페이지로 redirect



### 게시글 목록 기능 구현

- 게시글을 가져와서 template에 뿌려준다.

- 정렬 반대 -> Article.objects.order_by('-pk')





### method "POST"

- GET : 어떠한 리소스의 표현, 데이터를 조회할 때 사용

- POST : 서버에 어떠한 변화를 야기시킵니다. 어떤 엔티티를 특별한 리소스로 제출



- new.html에 method="POST"

- {% csrf_token %}을 추가

- views.py 에서 create에 request.GET을 전부 request.POST로 바꾼다.



- 일반적으로 form은 POST요청으로 처리한다.

- 만약 URL 평점을 기록하고 싶다면 : POST /movies/score

- 만약 URL 평점을 조회하고 싶다면 : GET /movies/123/score





### ModelForm

- HTML Form(UI)은 Django의 모델(DB)과 매우 밀접한 관계
  
  - 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문
  
  - 즉, 모델에 정의한 필드의 구성 및 종류에 따라 HTML Form이 결정됨



- input에 required 넣으면 공백으로 입력 불가
  
  - 하지만 개발자도구에서 삭제 후 공백입력 가능해짐 -> 보안 취약
  
  - 궁극적으로 서버쪽에서 조치를 취해야 함



### form의 구조를 만듬

- 앱에 forms.py 추가

```python
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

-> Article 모델에 있는 모든 필드를 가져다가 쓰겠다. 라는 의미



- model form의 인스턴스를 new.html에 넘겨준다.
  
  - 넘겨주기 위해 context 필요



- new.html에 {{ article_form.as_p }} 추가
  
  - form의 라벨과 구조를 만듬



### 유효성 검사

- views.py의 create에 article_form = ArticleForm(request.POST)

- if article_form.is_valid():
  
  - article_form.save()

- else:
  
  - print('유효하지 않습니다...!')



- 유효하지 않을 때 어떻게 해주면 좋을까요?
  
  - alret
  
  - 메시지 추가
  
  - 등등



- new 부분의 context ~ return까지 복사 후 create의 else 부분에 붙여넣기



- new와 create를 합칠 수 있다.

- new를 없애고

- create에 if request.method == "POST": 추가

- else에 article_form = ArticleForm() 추가

- 기존에 new url을 사용하던 곳 create로 수정







### 상세보기

- 특정한 글을 본다.

- urlpattern이 반드시 pk를 넣어야 한다.





### 삭제하기

- 특정한 글을 삭제한다.





### 수정하기

- 특정한 글을 수정한다. => 사용자에게 수정할 수 있는 양식을 제공(GET)하고 글을 받아서 특정한 글을 수정한다.(POST)



- **`인스턴스 지정`**



- create와 인스턴스 뺴고 똑같다.





Create : 1. UI 제공 2. DB저장 

Read(Detail) : 1. DB에서 특정 가져와서 조회

Delete : 1. DB에서 특정 가져와서 삭제

Update : 1. UI 제공 2. DB저장





ModelForm : Model에 정의된 필드에 맞춰서 UI그려주고 유효성 검사를 하고 DB에 저장도 함



url 동일하고 GET 과 POST로 나눠서 같은 함수에서 처리


