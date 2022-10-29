# 제 3장 SQL 최적화 기본원리

## 제 1절 옵티마이저와 실행계획



### 1. 옵티마이저(중요)

- 다양한 실행방법들 중에서 최적의 실행 방법을 결정하는 것이 옵티마이저의 역할

![](C:\Users\jhkim\AppData\Roaming\marktext\images\4da51480008e44462d12884c3b7f09363c4e5c4a.PNG)

#### 가. 규칙 기반 옵티마이저

- 규칙(우선순위)을 가지고 실행계획을 생성한다.

![](C:\Users\jhkim\AppData\Roaming\marktext\images\aea195f920b83ab38f27c2e7f3108a0255b9c88f.PNG)

#### 나. 비용기반 옵티마이저

- SQL 문을 처리하는데 필요한 비용이 가장 적은 실행계획을 선택하는 방식

![](C:\Users\jhkim\AppData\Roaming\marktext\images\4fe0ace2eca9752c21d5dc5ccb36302de8a69b88.PNG)

- 비용기반 옵티마이저는 통계정보, DBMS 버전, DBMS 설정 정보 등의 차이로 인행 동일 SQL문도 서로 다른 실행 계획이 생성될 수 있다.

- 또한 비용기반 옵티마이저의 다양한 한계들로 인해 실행계획의 예측 및 제어가 어렵다는 단점이 있다.



### 2. 옵티마이저 실행 계획(중요)

- SQL에서 요구한 사항을 처리하기 위한 절차와 방법
  
  - 실행계획을 구성하는 요소에는 조인순서, 조인기법, 엑세스기법, 최적화정보, 연산 등

- 동일한 SQL에 대해 결과를 낼 수 있는 다양한 처리 방법이 존재할 수 있지만 각 처리 방법마다 실행 시간(성능)은 서로 다를 수 있다.
  
  - 옵티마이저는 다양한 처리 방법들 중에서 가장 효율적인 방법을 찾아준다.



### 3. SQL 처리 흐름도

- SQL의 내부적인 처리 절차를 시각적으로 표현한 도표

![](C:\Users\jhkim\AppData\Roaming\marktext\images\d9184c40e2e76618bb8ff89916a63302d5c4a27f.PNG)



## 제 2절 인덱스 기본

### 1. 인덱스 특징과 종류(중요)

- 원하는 데이터를 쉽게 찾을 수 있도록 돋는 책의 찾아보기와 유사한 기능
  
  - DML 작업은 테이블과 인덱스를 함께 변경해야하기 때문에 느려질 수 있다.



#### 가. 트리기반 인덱스

- DBMS에서 가장 일반적인 인덱스는 B-트리인덱스

- 리프블록은 인덱스를 구성하는 칼럼의 데이터와 해당 데이터를 가지고 있는 행의 위치를 가리키는 레코드식별자로(RID, Record Identifier / Rowid) 구성되어 있다.
  '='로 검색하는 일치 검색과 'BETWEEN'등의 범위 검색 모두 적합함

![](C:\Users\jhkim\AppData\Roaming\marktext\images\c9038f874071bb73ed5b87d3f290cbb94784f841.PNG)



#### 나. SQL Server의 클러스터형 인덱스

- 클러스터형 인텍스, 비클러스터형 인덱스

- 클러스터형 인덱스의 2가지 중요성
  
  - 인덱스의 리프페이지가 곧 데이터페이지
  
  - 리프페이지의 모든 로우는 인덱스 - 키 - 칼럼순으로 물리적으로 정렬되어 저장도미

![](C:\Users\jhkim\AppData\Roaming\marktext\images\7114ce185537dae35acdd0eef8bbfc0f35bad83a.PNG)



### 2. 전체 테이블 스캔과 인덱스 스캔

#### 가. 전체 테이블 스캔

#### 나. 인덱스 스캔

#### 다. 전체테이블 스캔과 인덱스 스캔방식의 비교

![](C:\Users\jhkim\AppData\Roaming\marktext\images\1733f458c6ceeb6a9003a58b2b7567916090baa7.PNG)





## 제 3절 조인 수행 원리(중요)

### 1. NL Join(중요)

- NL Join은 프로그래밍에서 사용하는 중첩된 반복문과 유사한 방식으로 조인을 수행한다. 
  반복문의 외부에 있는 테이블을 선행 테이블 또는 외부 테이블(Outer Table)이라고 하고, 
  반복문의 내부에 있는 테이블을 후행 테이블 또는 내부 테이블(Inner Table)이라고 한다. 

- 선행 테이블 또는 외부 테이블->후행 테이블 또는 내부 테이블 
  결과 행의 수가 적은 테이블을 조인 순서상 선행 테이블로 선택하는 것이 전체 일량을 줄임 
  조인이 성공하면 바로 조인 결과를 사용자에게 보여줌으로 온라인 프로그램에 적당



![](C:\Users\jhkim\AppData\Roaming\marktext\images\49b913e82a60ed55c9c00c00df9d5b386a650ce7.PNG)



### 2. Sort Merge Join(중요)

- 주로 스캔하는 방식으로 데이터를 읽음. 조인 칼럼 인덱스 없어도 사용가능 -> 단, 성능이 떨어질 수 있음 
- 조인 칼럼을 기준으로 데이터를 정렬하여 조인을 수행한다. 
  NL Join은 주로 랜덤 액세스 방식으로 데이터를 읽는 반면 
  Sort Merge Join은 주로 스캔 방식으로 데이터를 읽는다. 
  Sort Merge Join은 랜덤 액세스로 NL Join에서 부담이 되던 넓은 범위의 데이터를 처리할 때 이용되던 조인 기법이다.

![](C:\Users\jhkim\AppData\Roaming\marktext\images\f7fffb8b10ed2f2eba816e0c8d61c9fab18a8e4c.PNG)



### 3. Hash Join(중요)

- 조인을 수행할 테이블의 조인 칼럼을 기준으로 해쉬 함수를 수행하여 
  서로 동일한 해쉬 값을 갖는 것들 사이에서 실제 값이 같은지를 비교하면서 조인을 수행한다. 
- Hash Join은 NL Join의 랜덤 액세스 문제점과 Sort Merge Join의 문제점인 
  정렬 작업의 부담을 해결 위한 대안으로 등장하였다. 
- ‘=’로 수행하는 동등 조인에서만 사용할 수 있다. 
- 결과 행의 수가 적은 테이블을 선행 테이블로 사용하는 것이 좋다.

![](C:\Users\jhkim\AppData\Roaming\marktext\images\bbaf4ac81bf46afc8b5b8d5f89d2d31e169c8588.PNG)
