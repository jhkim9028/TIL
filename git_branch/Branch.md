# Branch

- 특정한 버전의 흐름(작업 내역)

- 가지치기



## 목적

- 독립적인 버전들을 만들어 나갈 수 있도록 하기 위해서



---

> branch 합치는 과정을 merge(병합)라고 함
>
> merge 진행 중 충돌 발생 가능

---



### 브랜치를 합쳤을 때 나오는 상황

- 조모임 - 조장, 조원

- 제출 과제 - 보고서(docx), 발표자료(PPT)



- 배분
  - 조장이 보고서, 발표자료 전부 다하기
  - 조장이 보고서, 조원이 발표자료 하기
  - 조장이 보고서 파트1, 발표자료 파트1 / 조원이 보고서 파트2, 발표자료 파트 2



#### 상황

1. 혼자 작업, 조원 프리라이팅(fast-foward)
2. 보고서 파일 + 발표자료 파일(각자 커밋이 발생했는데, 다른 파일만 수정된 경우)
3. 진정한 협업(각자 커밋이 있는데, 같은 파일이 수정됨)



### Branch 병합 시나리오

#### 상황 1. fast-foward (혼자 작업, 조원 프리라이딩)

>fast-foward는 feature 브랜치 생성된 이후 master 브랜치에 변경 사항이 없는 상황

1. feature/home branch 생성 및 이동

```bash
(master) $ git branch featuer/home
(master) $ git checkout featuer/home
```



```bash
(master) $ git checkout -b feature/home
```



2. 작업 완료 후 commit

```bash
(feature/home) $ touch home.txt
(feature/home) $ git add .
(feature/home) $ git commit -m 'Add home.txt'
(feature/home) $ git log --oneline
74cd27d (HEAD -> feature/home) Add home.txt
5d8e24e (master) first
```

3. master 이동

```bash
(feature/home) $ git checkout master
(master) $ git log --oneline
5d8e24e (HEAD -> master) first
```

4. master에 병합

```bash
(master) $ git merge feature/home
```

5. 결과 : fast - foward

```bash
(master) $ git log --oneline
74cd27d (HEAD -> master, feature/home) Add home.txt
5d8e24e first
```

2번 git log와 3번 git log 결과가 다르게 나옴

그래서 4번에서 merge를 통해 병합



---



- ```bash
  $ git branch -d feature/home
  ```

  - branch 삭제

---



#### 상황2. merge commit(보고서 파일 + 발표자료 파일 / 각자 커밋이 발생했는데, 다른 파일만 수정된 경우)

> 서로 다른 이력(commit)을 병합하는 과정에서 **다른 파일이 수정**되어 있는 상황
>
> git이 auto merging을 진행하고, **commit이 발생된다.**



1. featuer/about branch 생성 및 이동

```bash
(master) $ git checkout -b featuer/about
```



2. 작업 완료 후 commit

```bash
(feature/about) $ touch about.txt
(feature/about) $ git add .
(feature/about) $ git commit -m 'Add about.txt'
(feature/about) $ git log --oneline
8b891f4 (HEAD -> feature/about) Add about.txt
74cd27d (master) Add home.txt
5d8e24e first
```



3. master 이동

```bash
(feature/about) $ git checkout master
```



4. master에 추가 commit이 발생!!
   - 다른 파일 수정 혹은 생성을 통해!

```bash
(master) $ touch master.txt
(master) $ git add .
(master) $ git commit -m 'Add master.txt'
(master) $ git log --oneline
07045ec (HEAD -> master) Add master.txt
74cd27d Add home.txt
5d8e24e first
```

- 2번과 4번에서 git log 했을 때 커밋 2개는 같지만 2번의 Add home.txt 와 4번의 Add master.txt 가 다르다!!



5. master에 병합

```bash
(master) $ git merge feature/about
$ git log --oneline --graph
*   3193830 (HEAD -> master) Merge branch 'feature/about'
|\
| * 8b891f4 (feature/about) Add about.txt
* | 07045ec Add master.txt
|/
* 74cd27d Add home.txt
* 5d8e24e first
```



6. branch 삭제

```bash
(master) $ git branch -d feature/about
```





### 상황3. merge commit 충돌(진정한 협업 / 각자 커밋이 있는데, 같은 파일이 수정됨)

> 서로 다른 이력(commit)을 병합하는 과정에서 같은 파일의 동일한 부분이 수정되어 있는 상황
>
> git이 auto merging을 하지 못하고, 충돌 메시지가 뜬다.
>
> 해당 파일의 위치에 표준 형식에 따라 표시 해준다.
>
> 원하는 형태의 코드로 직접 수정을 하고 직접 commit을 발생시켜야 한다.



1. feature/test branch 생성 및 이동

```bash
(master) $ git checkout -b feature/test
```



2. 작업 완료 후 commit

```bash
# 기존 파일 열어서 수정
(feature/test) $ touch test.txt
(feature/test) $ git add .
(feature/test) $ git commit -m 'Add test.txt'
(feature/test) $ git log --oneline
06aa977 (HEAD -> feature/test) Add test.txt
3193830 Merge branch 'feature/about'
07045ec Add master.txt
8b891f4 Add about.txt
74cd27d Add home.txt
5d8e24e first
```



3. master 이동

```bash
(feature/test) $ git checkout master
```



4. master에 추가 commit 발생!!
   - 동일 파일을 수정 혹은 생성!

```bash
#기존 파일 열어서 수정
(master) $ git add <파일명>
(master) $ git commit -m 'update'
$ git log --oneline
d697bcb (HEAD -> master) update
3193830 Merge branch 'feature/about'
07045ec Add master.txt
8b891f4 Add about.txt
74cd27d Add home.txt
5d8e24e first
```



5. master에 병합

```bash
(master) $ git merge feature/test
```



6. 결과 -> merge conflict 발생

> git status 명령어로 충돌 파일 확인 가능

```bash
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
        new file:   test-1.txt
        new file:   test-2.txt

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   1.txt

```



7. 충돌 확인 및 해결

```
<<<<<<< HEAD
ww
=======
ff
>>>>>>> feature/test

```



8. merge commit 해결

```bash
(master) $ git add .
(master) $ git commit
```

- vs code 편집기에서 메시지보고 닫아주세요~!



9. 커밋 및 확인하기

```bash
$ git log --oneline --graph
*   1849545 (HEAD -> master) Merge branch 'feature/test'
|\
| * 06aa977 (feature/test) 기존 파일 수정하고 test 작성
* | d697bcb 1 수정
|/
*   3193830 Merge branch 'feature/about'
|\
| * 8b891f4 Add about.txt
* | 07045ec Add master.txt
|/
* 74cd27d Add home.txt
* 5d8e24e first
```



10. branch 삭제

```bash
$ git branch -d feature/test
```



___

### Feature Branch Workflow

> shared repository model (저장소의 소유권이 있는 경우)

- 프로세스

		1. 각 사용자는 원격 저장소의 소유권을 가진 상태
		1. 기능 구현 후 원격 저장소에 브랜치 반영
		1. 병합 진행
		1. 병합 완료 후 완료된 브랜치 삭제



1. branch 생성 및 이동

```bash
(master) $ git checkout -b hotfix
```



2.  파일 편집



3. 커밋

```bash
(hotfix) $ git add .
(hotfix) $ git commit -m 'readme hotfix'
```



4. push

```bash
(hotfix) $ git push origin hotfix
```



5. Github에 가서 pull request하기

- hotfix 브랜치를 master에게 보냄
- create pull request



6. merge pull request 하기





### Forking Workflow

- Fork & Pull model (저장소의 소유권이 없는 경우)

#### Clone & Branch 생성

1. Github의 Fork할 저장소에서 우측 상단의 Fork 버튼을 누릅니다.
2. 자신의 원격저장소에 저장될 이름을 작성하고 Create fork 합니다.
3. 자신의 원격저장소에서 확인합니다.
4. Fork 받아온 저장소를 로컬로 clone 합니다.

```bash
$ git clone hhtps://github.com/user.name/저장소 이름.git
```

5. branch 생성하고 이동합니다.

```bash
$ git branch example
```

```bash
$ git checkout example
```

위에 두 줄을 한번에

```bash
$ git checkout -b example
```

master => example 확인

#### 내용 수정하고 커밋

6. 작업 및 파일 수정
7. 작업 완료 후 변경 사항을 add, commit, push 합니다.

```bash
$ git add .
$ git commit -m '커밋메시지'
$ git push origin example
```

#### Pull Request

8. Github에서 Compare & Pull request를 생성합니다.
9. pull request 내용을 작성한 후 create pull request합니다.
   1. head repository와 base repository를 확인해야 합니다.
   2. head => base 방향으로 merge 됩니다.

















