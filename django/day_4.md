# App URL mapping

## App URL mapping

- 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법 이해하기

- 두번쨰 app인 pages를 생성 및 등록하고 진행

- app의 view 함수가 많아지면서 사용하는 path() 또한 많아지고, app또한 더 많이 작성되기 때문에 프로젝트의urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음

- 각 앱의 view함수를 다른 이름으로 import할 수 있음

- 하나의 프로젝트의 여러 앱이 존재한다면, 각각의 앱 안에 urls.py을 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁할 수 있음

- urlpatten은 언제든지 다른 UTLconf 모듈을 포함할 수 있음

- include되는 앱의 url.py에 urlpatterns가 작성되어 있지 않다면 에러가 발생

- 예를 들어, pages앱의 urlpatterns가 빈 리스트라도 작성되어 있어야 함

```python
# firstpjt/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```



## Including other URLconfs

- 메인 페이지 주소가
  
  http://~ :8000/index/ -> http:// ~ :8000/articles/index/ 로 바뀜



## Include()

- 다른 URLconf들을 참조할 수 있도록 돋는 함수

- 함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속처리를 위해 include된 URLconf로 전달



# Template namespace

- pages app의 index url(http://localhost:8000/pages/index/)로 직접 이동해도 articles app의 index 페이지가 출력됨



## 개요

- Django는 기본적으로 app_name/templates/ 경로에 있는 templates 파일들만 찾을 수 있으며, settings.py의 INSTALLED_APPS에 작성한 app 순서로 template을 검색후 렌더링 함

- 바로 이 속성 값이 해당 경로를 활성화하고 있음

```python
# settings.py
TEMPLATES = [
{
    ...,
    'APP_DIRS': True,    
    ...
    },
]
```



## 디렉토리 생성을 통해 물리적인 이름공간 구분

- Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 app_name/templates/app_name/형태로 변경

- Django templates의 기본 경로 자체를 변경할 수 없기 떄문에 물리적으로 이름 공간을 만드는 것



## 템플릿 경로 변경

- 폴더 구조 변경 후 변경괸 경로로 해당하는 모든 부분을 수정

```python
# articles/views.py
return render(request, 'articles/index.html')
```

```python
# pages/views.py
return render(request, 'pages/index.html')
```


