# Git

> 분산 버전관리 시스템 = 버전 관리



## 기본 명령어

### init

```bash
$ git init
```

- 로컬 저장소 생성



### add

```bash
$ git add <파일명>
```

- working directory상의 변경 내용을 staging area에 추가하기 위해 사용
  - untracked 상태의 파일을 staged로 변경
  - modified 상태의 파일을 staged로 변경



### commit

```bash
$ git commit -m '<커밋메시지>'
```

- staged 상태의 파일들을 커밋을 통해 버전으로 기록



### log

```bash
$ git log
```

```bash
$ git log -1
$ git log --oneline
$ git log -2 --oneline
```

- 현재 저장소에 기록된 커밋을 조회



### status

```bash
$ git status
```

- Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용



---



## 설정

### 사용자 설정

```bash
$ git config --global user.name "username"

$ git config --global user.email "my@email.com"
```

- 설정 확인
  - $ git config -l
  - $ git config --global -l
  - $ git config user.name
  



## .gitkeep

빈 폴더는 git status 명령어를 실행했을 때 나타나지 않는다. 왜냐하면 git은 빈 폴더를 어떠한 변경사항도 없다고 생각하기 때문이다.

.gitkeep 파일은 빈 폴더를 만들고 싶을 때 사용한다.

 관용적으로 쓰이기 때문에 꼭 gitkeep이 아니어도 무방하다.





## .gitignore

.gitignore파일이란 Git의 버전 관리에서 제외할 파일 목록을 지정하는 파일로, Git이 gitignore파일 안에 있는 파일 목록에 대해 더 이상 관여할 수 없다.
