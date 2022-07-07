# Github

> Git과 마찬가지로 버전관리



## 원격 저장소(Remote Repository) 기본 흐름

```
$ git push
```

- 로컬 저장소의 버전을 원격 저장소로 보낸다.

```
$ git pull
```

- 원격 저장소의 버전을 로컬 저장소로 가져온다.



## Github 원격 저장소 만들기

1. 깃허브 홈페이지 우측 상단 + 에서 New Repository 클릭
2. 저장소 설정
   1. repository 이름 설정
   2. 저장소 설명
   3. 공개 여부 설정
3. 확인하기
   1. https://github.com/Github Username/저장소 이름.git



## 원격 저장소 활용 명령어

```
$ git push <원격 저장소 이름> <브랜치 이름>
```

- 원격 저장소로 로컬 저장소 변경 사항을 올림



```
$ git pull <원격 저장소 이름> <브랜치 이름>
```

- 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함



```
$ git clone <원격 저장소 주소>
```

- 원격 저장소를 복제하여 가져옴



```
$ git remote -v
```

- 원격 저장소 정보 확인



```
$ git remote add <원격 저장소> <url>
```

- 원격 저장소 추가











