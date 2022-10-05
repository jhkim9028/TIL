# Django Staticfiles



## admin

- /admin을 통해 들어갈 수 있다.

- 사용자 이름, 비밀번호가 필요하다.



- python manage.py createsuperuser을 통해 사용자이름과 비밀번호 설정



- admin.py에 모델을 등록
  
  - from .models import [모델 이름]
  
  - admin.site.register([모델 이름])



## Static files

- INSTALLED_APPS에 django.contrib.staticfiles가 포함되어있는지 확인

- settings.py에서 STATIC_URL이 정의되어 있는지 확인

- static 이란 폴더를 만들고 그 안에 이미지 넣고

- {% load static %} 넣고

- img 태그 src에 {% static '[이미지 이름]' %}



- css도 마찬가지로

- link의 href에 {% static 'css/style.css' %}



- {% load static %} == python에서 import



## bootstrap

- pip install django-bootstrap5

- settings.py의 INSTALLED_APPS에 django_bootstrap5 추가

- html 파일에 {% load django_bootstrap5 %} 추가

- html에 {% bootstrap_form [form이름] %} 추가

- {% bootstrap_css %}, {% bootstrap_javascript %} 추가
