# Git

> 분산 버전관리 시스템 = 버전 관리

## 기본 명령어



### init

> $ git init

- 로컬 저장소 생성



### add

> $ git add <파일명>

- working directory상의 변경 내용을 staging area에 추가하기 위해 사용
  - untracked 상태의 파일을 staged로 변경
  - modified 상태의 파일을 staged로 변경



### commit

> $ git commit -m '<커밋메시지>'

- staged 상태의 파일들을 커밋을 통해 버전으로 기록



### log

> $ git log
>
> - git log -1
> - git log --oneline
> - git log -2 --oneline

- 현재 저장소에 기록된 커밋을 조회



### status

> $ git status

- Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용



---



## 설정

### 사용자 설정

> git config --global user.name "username"

> git config --global user.email "my@email.com"



- 설정 확인

  > git config -l

  > git config --global -l

  > git config user.name



