# 제 2장 SQL 활용

## 제 1절 표준 조인

### 1. STANDAR SQL

#### 가. (중요)일반 집합 연산자 -> 현재의 SQL

UNION -> UNION 
INTERSECTION -> INTERSECT 
DIFFERENCE -> EXCEPT(Oracle은 MINUS) 
PRODUCT -> CROSS JOIN(CARTESIAN PRDUCT)

![](C:\Users\jhkim\AppData\Roaming\marktext\images\6825bf68c824e1d4a94f4613f90ba8feaa9b746b.PNG)

#### 나. 순수관계연산자 -> 현재의 SQL

SELECT->WHERE 
PROJECT->SELECT 
(NATURAL)JOIN->다양한JOIN 
DIVIDE->현재 사용하지 않음

![](C:\Users\jhkim\AppData\Roaming\marktext\images\4da51480008e44462d12884c3b7f09363c4e5c4a.PNG)

### 2. FROM절 JOIN 형태

ANSI/ISO SQL에서 표시하는 FROM 절의 JOIN 형태는 다음과 같다.

- INNER JOIN - NATURAL JOIN - USING 조건절 - ON조건걸 - CROSS JOIN - OUTER JOIN

### 3. INNER JOIN(중요)

- '내부 JOIN'이라고 함. JOIN조건에서 동일한 값이 있는 행만 반환한다.

- DEFAULT 옵션이므로 생략이 가능하지만, CROSS JOIN, OUTER JOIN과는 같이 사용할 수 없다.

- USING 조건절이나 ON조건절을 필수적으로 사용해야 한다.

SQL>> 
“사원 번호와 사원 이름, 소속부서 코드와 소속부서 이름을 출력하시오.” 
SELECT EMP.DEPTNO, EMPNO, ENAME, DNAME FROM EMP, DEPT 
WHERE EMP.DEPTNO = DEPT.DEPTNO; 
->(다음도 같은 코드) 
SELECT EMP.DEPTNO, EMPNO, ENAME, DNAME FROM EMP 
INNER JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO; 
->(다음도 같은 코드, INNER JOIN을 JOIN으로 써도 상관 없다. 디폴트값이 INNER JOIN) 
SELECT EMP.DEPTNO, EMPNO, ENAME, DNAME FROM EMP 
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO;

### 4. NATURAL JOIN(중요)

- 두테이블간의 동일한 이름을 갖는 모든 칼럼들에 대해 EQUI(=)JOIN을 수행한다 

- 추가로 USING조건절, ON조건절, WHERE절에서 JOIN조건을 정의할 수 없다 

- JOIN에 사용된 칼럼들은 같은 데이터 유형이어야 한다 

- ALIAS나 테이블명과 같은 접두사를 붙일 수 없다

SQL>> 
“사원 번호와 사원 이름, 소속부서 코드와 소속부서 이름을 출력하시오.” 
SELECT DEPTNO, EMPNO, ENAME, DNAME FROM EMP NATURAL JOIN DEPT;

### 5. USING 조건절(중요)

- 같은 이름을 가진 칼럼들 중에서 원하는 칼럼에 대해서만 선택적으로 =JOIN을 할 수 있다. 
- SQL Server에서는 지원하지 않는다 
- JOIN칼럼에 대해서는 ALIAS나 테이블이름과 같은 접두사를 붙일 수 없다 
  Oracle SQL>> 
  SELECT * FROM DEPT JOIN DEPT_TEMP USING (DEPTNO);

### 6. ON조건절(중요)

- 칼럼 명이 다르더라도 JOIN 조건을 사용할 수 있는 장점이 있다 
- WHERE 검색 조건은 충돌 없이 사용할 수 있다 
- ON 조건절에서 사용된 괄호는 옵션사항이다 
- **ALIAS나 테이블명과 같은 접두사를 사용해야한다(중요)**

#### 가. WHERE 절과의 혼용

SQL>> 
“부서코드 30인 부서의 소속 사원 이름 및 소속 부서 코드, 부서 코드, 부서 이름을 출력하시오.” 
SELECT E.ENAME, E.DEPTNO, D.DEPTNO, D.DNAME FROM EMP E 
JOIN DEPT D ON (E.DEPTNO = D.DEPTNO) WHERE E.DEPTNO = 30;

#### 나. ON조건절 + 데이터 검증 조건 추가

SQL>> 
“매니저 사원번호가 7698번인 사원들의 이름 및 소속 부서 코드, 부서 이름을 출력하시오.” 
SELECT E.ENAME, E.MGR, D.DEPTNO, D.DNAME FROM EMP E 
JOIN DEPT D ON (E.DEPTNO = D.DEPTNO AND E.MGR = 7698); 
->(다음도 같은 코드) 
SELECT E.ENAME, E.MGR, D.DEPTNO, D.DNAME FROM EMP E 
JOIN DEPT D ON (E.DEPTNO = D.DEPTNO) WHERE E.MGR = 7698;

#### 다. ON조건절 예제

SQL>> 
“팀과 스타디움 테이블을 팀ID로 JOIN하여 팀이름, 팀ID, 스타디움 이름을 찾아본다. 
STADIUM에는 팀ID가 HOMETEAM_ID라는 칼럼으로 표시되어 있다.” 
SELECT TEAM_NAME, TEAM_ID, STADIUM_NAME FROM TEAM 
JOIN STADIUM ON TEAM.TEAM_ID = STADIUM.HOMETEAM_ID ORDER BY TEAM_ID;

#### 라. 다중 테이블 JOIN

SQL>> 
“사원과 DEPT 테이블의 소속 부서명, DEPT_TEMP 테이블의 바뀐 부서명 정보를 찾아본다.” 
SELECT E.EMPNO, D.DEPTNO, D.DNAME, T.DNAME New_DNAME FROM EMP E 
JOIN DEPT D ON (E.DEPTNO = D.DEPTNO) JOIN DEPT_TEMP T ON (E.DEPTNO = T.DEPTNO);

### 7. CROSS JOIN

- CARTESIAN PRODUCT / “JOIN 조건이 없는 경우 생길 수 있는 모든 데이터의 조합” 
  SQL>> 
  “사원 번호와 사원 이름, 소속부서 코드와 소속부서 이름을 찾아본다.” 
  SELECT ENAME, DNAME FROM EMP CROSS JOIN DEPT ORDER BY ENAME;

### 8. OUTER JOIN(중요)

- JOIN 조건에서 동일한 값이 없는 행도(NULL값도) 출력된다. 
- USING 조건 절이나 ON 조건 절을 필수적으로 사용해야한다

![](C:\Users\jhkim\AppData\Roaming\marktext\images\4fe0ace2eca9752c21d5dc5ccb36302de8a69b88.PNG)

#### 가. LEFT OUTER JOIN

- 조인 수행 시 좌측 테이블에 해당하는 데이터를 먼저 읽은 후, 우측테이블에서 JOIN 대상 데이터를 읽어온다 
  SQL>> 
  “STADIUM에 등록된 운동장 중에는 홈팀이 없는 경기장도 있다. 
  STADIUM과 TEAM을 JOIN 하되 홈팀이 없는 경기장의 정보도 같이 출력하도록 한다.” 
  SELECT STADIUM_NAME, STADIUM.STADIUM_ID, SEAT_COUNT, HOMETEAM_ID, TEAM_NAME 
  FROM STADIUM LEFT OUTER JOIN TEAM ON STADIUM.HOMETEAM_ID = TEAM.TEAM_ID 
  ORDER BY HOMETEAM_ID; 
  —>(OUTER는 생략 가능)

#### 나. RIGHT OUTER JOIN

- LEFT OUTER JOIN와 반대로 우측 테이블이 기준이 되어 결과 생성

#### 다. FULL OUTER JOIN

- 합집합 개념으로 LEFT와 RIGHT를 모두 읽어 온다 
  SQL>> 
  UPDATE DEPT_TEMP SET DEPTNO = DEPTNO + 20; —>(먼저 업데이트)
  SELECT * FROM DEPT_TEMP; —>(업데이트한 모두를 읽어온다)

### 9. INNER vs OUTER vs CROSS JOIN 비교

![](C:\Users\jhkim\AppData\Roaming\marktext\images\d9184c40e2e76618bb8ff89916a63302d5c4a27f.PNG)

첫 번째, INNER JOIN의 결과는 다음과 같다. 
양쪽 테이블에 모두 존재하는 키 값이 B-B, C-C 인 2건이 출력된다. 

****

두 번째, LEFT OUTER JOIN의 결과는 다음과 같다. 
TAB1을 기준으로 키 값 조합이 B-B, C-C, D-NULL, E-NULL 인 4건이 출력된다. 

****

세 번째, RIGHT OUTER JOIN의 결과는 다음과 같다. 
TAB2를 기준으로 키 값 조합이 NULL-A, B-B, C-C 인 3건이 출력된다. 

****

네 번째, FULL OUTER JOIN의 결과는 다음과 같다. 
양쪽 테이블을 기준으로 키 값 조합이 NULL-A, B-B, C-C, D-NULL, E-NULL 인 5건이 출력된다. 

****

다섯 번째, CROSS JOIN의 결과는 다음과 같다. JOIN 가능한 모든 경우의 수를 표시하지만 단, OUTER JOIN은 제외한다. 

양쪽 테이블 TAB1과 TAB2의 데이터를 곱한 개수인 4 * 3 = 12건이 추출됨 
키 값 조합이 B-A, B-B, B-C, C-A, C-B, C-C, D-A, D-B, D-C, E-A, E-B, E-C 인 12건이 출력된다.

## 제 2절 집합 연산자

- 두개 이상의 테이블에서 조인을 사용하지 않고 연관된 데이터를 조회하는 방법 중 하나 
- 집합연산자는 2개 이상의 질의 결과를 하나의 결과로 만들어준다 
- SELECT절의 칼럼 수가 동일하고 동일 위치에 존재하는 칼럼의 데이터타입이 상호 호환 가능해야 한다

| 집합 연산자    | 연산자의 의미                                                                                                                                                        |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UNION     | 여러 개의 SQL문의 결과에 대한 합집합으로 결과에서 모든 중복된 행은 하나의 행으로 만든다.                                                                                                           |
| UNION ALL | 여러 개의 SQL문의 결과에 대한 합집합으로 중복된 행도 그대로 결과로 표시된다. 즉, 단순히 결과만 합쳐놓은 것이다. 일반적으로 여러 질의 결과가 상호 배타적인(Exclusive)일 때 많이 사용한다. 개별 SQL문의 결과가 서로 중복되지 않는 경우, UNION과 결과가 동일하다. |
| INTERSECT | 여러 개의 SQL문의 결과에 대한 교집합이다. 중복된 행은 하나의 행으로 만든다.                                                                                                                  |
| EXCEPT    | 앞의 SQL문의 결과에서 뒤의 SQL문의 결과에 대한 차집합이다. 중복된 행은 하나의 행으로 만든다.                                                                                                       |

![](assets/4da51480008e44462d12884c3b7f09363c4e5c4a.PNG)

## 제 3절 계층형 질의와 셀프 조인

### 1. 계층형 질의

- 테이블에 계층형 데이터가 존재하는 경우 데이터를 조회하기 위해서 계층형 질의(Hierarchical Query)를 사용한다. 
- 엔터티를 순환관계 데이터 모델로 설계할 경우 계층형 데이터가 발생한다. (예: 조직, 사원, 메뉴 등)

#### 가. Oracle 계층형 질의(중요)

```sql
SELECT ...
FROM 테이블
WHERE condition AND condition ...
START WITH condition
CONNECT BY [NOCYCLE] condition AND condition...
[ORDER SIBLINGS BY column, column, ...]
```

- 계층형 질의 구문

| 가상 칼럼              | 설명                                                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| LEVEL              | 루트 데이터이면 1, 그 하위 데이터이면 2이다. 리프 데이터까지 1씩 증가한다.                                                                            |
| CONNECT_BY_ISLEAF  | 전개 관정에서 해당 데이터가 리프 데이터이면 1, 그렇지 않으면 0이다.                                                                                 |
| CONNECT_BY_ISCYCLE | 전개 과정에서 자식을 갖는데, 해당 데이터가 조상으로서 존재하면 1, 그렇지 않으면 0이다. 여기서 조상이란 자신으로부터 루트까지의 경로에 존재하는 데이터를 말한다. CYCLE 옵션을 사용했을 때만 사용할 수 있다. |

- 계층형 질의에서 사용되는 가상 칼럼

#### 나. SQL Server 계층형 질의(중요)

1. CTE(Common Table Expression)를 재귀 호출

![](assets/aea195f920b83ab38f27c2e7f3108a0255b9c88f.PNG)

정리하자면 다음과 같다. 먼저, 앵커 멤버가 시작점이자 Outer 집합이 되어 Inner 집합인 재귀 멤버와 조인을 시작한다. 
이어서, 앞서 조인한 결과가 다시 Outer 집합이 되어 재귀 멤버와 조인을 반복하다가 조인 결과가 비어 있으면 
즉, 더 조인할 수 없으면 지금까지 만들어진 결과 집합을 모두 합하여 리턴한다.

2. 셀프 조인: “동일 테이블 사이의 조인”, 반드시 테이블 별칭(Alias)을 사용해야 한다.

## 제 4절 서브 쿼리

![](assets/4fe0ace2eca9752c21d5dc5ccb36302de8a69b88.PNG)

- “하나의 SQL문안에 포함되어있는 또다른 SQL문” ——> 
- 서브 쿼리는 메인 쿼리의 칼럼을 모두 사용할 수 있지만, 메인 쿼리는 서브 쿼리의 칼럼을 사용할 수 없다. 
- 서브쿼리를 괄호로 감싸서 사용한다. 단일행 또는 복수행 비교연산자와 함께 사용가능하다. ORDER BY를 사용하지 못한다

| 서브 쿼리 종류                | 설명                                                                                              |
| ----------------------- | ----------------------------------------------------------------------------------------------- |
| Un-Correlated(비연관) 서브쿼리 | 서브쿼리가 메인쿼리 칼럼을 가지고 있지 않는 형태의서브쿼리이다. 메인쿼리에 값(서브쿼리가 실행된 결과)을 제공하기 위한 목적으로 주로 사용한다.                |
| Correlated(연관) 서브쿼리     | 서브쿼리가 메인쿼리 칼럼을 가지고 있는 형태의 서브쿼리이다. 일반적으로 메인쿼리가 먼저 수행되어 읽혀진 데이터를 서브쿼리에 조건이 맞는지 확인하고자 할 때 주로 사용된다. |

- 동작하는 방식에 따른 서브쿼리 분류

| 서브쿼리 종류                       | 설명                                                                                                            |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Single Row 서브쿼리(단일 행 서브쿼리)    | 서브쿼리의 실행 결과가 항상 1건 이하인 서브쿼리를 의미한다. 단일 행 서브쿼리는 단일 행 비교 연산자와 함께 사용된다. 단일 행 비교 연산자에는 =,<,<=,>,>=,<> 이 있다.        |
| Multi Row 서브쿼리(다중 행 서브쿼리)     | 서브쿼리의 실행 결과가 여러 건인 서브쿼리를 의미한다. 다중 행 서브쿼리는 다중 행 비교 연산자와 함께 사용된다. 다중 행 비교 연산자에는 IN, ALL, ANY, SOME, EXISTS가 있다. |
| Multi Column 서브쿼리(다중 칼럼 서브쿼리) | 서브쿼리의 실행 결과로 여러 칼럼을 반환한다.  메인쿼리의 조건절에 여러 칼럼을 동시에 비교할 수 있다. 서브쿼리와 메인쿼리에서 비교하고자 하는 칼럼 개수와 칼럼의 위치가 동일해야 한다.      |

- 반환되는 데이터의 형태에 따른 서브쿼리 분류

****

### 1. 단일행 서브 쿼리

- 단일행 비교연산자와 함꼐 사용할 때는 서브쿼리의 결과 건수가 반드시 1건 이하여야 함

### 2. 다중행 서브 쿼리(중요)

- 실행 결과가 여러건임. IN, ALL, SOME, EXISTS

| 다중 행 연산자         | 설명                                                                                                                                                 |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| IN(서브쿼리)         | 서브쿼리의 결과에 존재하는 임의의 값과 동일한 조건을 의미한다. (Multiple OR 조건)                                                                                               |
| 비교연산자 ALL(서브쿼리)  | 서브쿼리의 결과에 존재하는 모든 값을 만족하는 조건을 의미한다. 비교 연산자로 ">"를 사용했다면 메인쿼리는 서브쿼리의 모든 결과 값을 만족해야 하므로, 서브쿼리 결과의 최대값보다 큰 모든 건이 조건을 만족한다.                             |
| 비교 연산자 ANY(서브쿼리) | 서브쿼리의 결과에 존재하는 어느 하나의 값이라도 만족하는 조건을 의미한다. 비교 연산자로 ">"를 사용했다면 메인쿼리는 서브쿼리의 값들 중 어떤 값이라도 만족하면 되므로, 서브쿼리의 결과의 최소값보다 큰 모든 건이 조건을 만족한다.(SOME 은 ANY와 동일함) |
| EXISTS(서브쿼리)     | 서브쿼리의 결과를 만족하는 값이 존재하는지 여부를 확인하는 조건을 의미한다. 조건을 [출처] 서브쿼리의 종류\| 작성자 찐 만족하는 건이 여러 건이라도 1건만 찾으면 더 이상 검색하지 않는다.                                        |

- **다중행 서브 쿼리 예제(중요)**

SQL>> 
“선수들 중에서 ‘정현수’라는 선수가 소속되어 있는 팀 정보를 출력하라!” 
SELECT REGION_NAME 연고지명, TEAM_NAME 팀명, E_TEAM_NAME 영문팀명 FROM TEAM 
WHERE TEAM_ID IN (SELECT TEAM_ID FROM PLAYER WHERE PLAYER_NAME = '정현수') 
ORDER BY TEAM_NAME;

### 3. 다중칼럼서브쿼리

- “서브 쿼리의 결과로 여러 개의 칼럼이 반환되어 메인 쿼리의 조건과 동시에 비교되는 것”

### 4. 연관서브쿼리

- “서브쿼리내에 메인쿼리칼럼이 사용된 서브 쿼리” EXISTS는 항상 연관서브쿼리로 사용”

### 5. 그밖에 위치에서 사용하는 서브 쿼리

#### 가. SELECT 절에 서브 쿼리 사용하기 -> 스칼라 서브쿼리(한 행, 한 칼럼만을 반환하는 서브 쿼리)(중요)

![](assets/d9184c40e2e76618bb8ff89916a63302d5c4a27f.PNG)

#### 나. FROM 절에서 서브 쿼리 사용하기 -> 인라인뷰, 동적뷰(Dynamic View)(중요)

- 인라인뷰에서는 ORDER BY절을 사용할 수 있다. 인라인뷰에 먼저 정렬을 수행하고 

- 정렬된 결과 중에서 일부데이터를 추출하는 것을 TOP-N 쿼리라고 한다

- **Oracle에서는 ROWNUM이라는 연산자를 통해 결과 중 일부데이터만 추출 가능(중요)**

#### 다. HAVING 절에서 서브쿼리 사용하기

#### 라. UPDATE문의 SET절에서 사용하기

#### 마. INSERT문의 VALUES절에서 사용하기

### 6. 뷰(중요)

- 테이블은 실제로 데이터를 가지고 있는 반면, 뷰는 실제데이터를 가지고 있지 않다.

| 장점  | 설명                                                                                      |
| --- | --------------------------------------------------------------------------------------- |
| 독립성 | 테이블 구조가 변경되어도 뷰를 사용하는 응용 프로그램은 변경하지 않아도 된다.                                             |
| 편리성 | 복잡한 질의를 뷰로 생성함으로써 관련 질의를 단순하게 작성할 수 있다. 또한 해당 형태의 SQL문을 자주 사용할 때 뷰를 이용하면 편리하게 사용할 수 있다. |
| 보안성 | 직원의 급여정보와 같이 숨기고 싶은 정보가 존재한다면, 뷰를 생성할 때 해당 칼럼을 빼고 생성함으로써 사용자에게 정보를 감출 수 있다.             |



## 제 5절 그룹함수

### 1. 데이터분석 개요

- ANSI/ISO SQL 표준은 데이터 분석을 위해서 다음 세 가지 함수를 정의하고 있다. 
- AGGREGATE FUNCTION, GROUP FUNCTION, WINDOW FUNCTION



### 2. ROLLUP함수(중요)

- ROLLUP에 지정된 Grouping Columns의 List는 Subtotal을 생성하기 위해 사용되어지며, 
  Grouping Columns의 수를 N이라고 했을 때 N+1 Level의 Subtotal이 생성된다. 
- 계층 구조이므로 인수 순서가 바뀌면 수행 결과도 바뀜. 가능한 Subtotal만 생성 
- GROUP BY의 확장된 형태 
  SQL>> 
  “부서명과 업무명을 기준으로 사원수와 급여 합을 집계한 일반적인 GROUP BY SQL 문장을 수행” 
  SELECT DNAME, JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" FROM EMP, DEPT 
  WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY DNAME, JOB;



### 3. CUBE 함수(중요)

- 결합 가능한 모든 값에 대하여 다차원 집계를 생성한다 
  SQL>> 
  “부서명과 업무명을 기준으로 사원수와 급여 합을 집계한 일반적인 GROUP BY SQL 문장을 수행” 
  SELECT CASE GROUPING(DNAME) WHEN 1 THEN 'All Departments' ELSE DNAME END AS DNAME, 
  CASE GROUPING(JOB) WHEN 1 THEN 'All Jobs' 
  ELSE JOB END AS JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" FROM EMP, DEPT 
  WHERE DEPT.DEPTNO = EMP.DEPTNO GROUP BY CUBE (DNAME, JOB) ;

### 4. GROUPING SETS 함수

- 원하는 부분의 소계만 손쉽게 추출할 수 있다. 인수는 평등한 관계이므로 인수의 순서 바뀌어도 결과는 같다.

![](assets/c9038f874071bb73ed5b87d3f290cbb94784f841.PNG)



## 제 6절 윈도우 함수

### 1. WINDOW FUNCTION 개요(중요)

- OVER문구가 키워드로 필수 포함된다 
- 분석 함수(ANALYTIC FUNCTION), 순위 함수(RANK FUNCTION) 
- WINDOWING함수 2가지 종류(BETWEEN 사용 타입, BETWEEN 미사용 타입) 
  SQL>> 
  SELECT WINDOW_FUNCTION (ARGUMENTS) 
  OVER ( [PARTITION BY 칼럼] [ORDER BY 절] [WINDOWING 절] ) FROM 테이블 명;



### 2. 그룹 내 순위 함수

#### 가. RANK 함수

#### 나. DENSE_RANK 함수(중요)

- 동일한 순위를 하나의 건수로 취급, 중간 순위를 안 비움

#### 다. ROW_NUMBER 함수(중요)

- 동일한 값이라도 고유한 순위를 부여한다는 점이 RANK,DENSE_RANK와 다르다. 
  SQL>> 
  “사원 데이터에서 급여가 높은 순서와 JOB 별로 급여가 높은 순서를 같이 출력한다.” 
  SELECT JOB, ENAME, SAL, RANK( ) 
  OVER (ORDER BY SAL DESC) ALL_RANK, RANK( ) 
  OVER (PARTITION BY JOB ORDER BY SAL DESC) JOB_RANK FROM EMP;

### 3. 일반집계 함수

- SUM 함수

- MAX함수

- MIN함수

- AVG함수

- COUNT함수



### 4. 그룹 내 행 순서 함수

- FIRST_VALUE함수 : 파티션별 윈도우에서 가장 먼저 나온 값

- LAST_VALUE함수 : 파티션별 윈도우에서 가장 나중에 나온 값

- LAG 함수(중요) : "현재 읽혀진 데이터의 이전 값을 알아내는 함수"

- LEAD 함수(중요) : "이후 값을 알아내는 함수"



### 5. 그룹 내 비율 함수

- RATIO_TO_REPORT 함수 : 전체 SUM(칼럼)값에 대한 행별 칼럼 값의 백분율을 소수점으로 구함

- PERCENT_RANK 함수 : 제일 먼저 나오는 것을 0으로, 제일 늦게 나오는 것을 1로 하여, 값이 아닌 행의 순서별 백분율을 구한다.

- CUME_DIST 함수 : 전체건수에서 현재 행보다 작거나 같은 건수에 대한 누적백분율

- NTILE 함수 : 전체 건수를 ARGUMENT 값으로 N등분한 결과



## 제 7절 DCL

### 1. DCL 개요

- 유저를 생성하고 권한을 제어할 수 있는 DCL(DATA CONTROL LANGUAGE)명령어



| 유저     | 역할                                                         |
| ------ | ---------------------------------------------------------- |
| SCOTT  | Oracle 테스트용 샘플 유저<br/>Default 패스워드 : TIGER                 |
| SYS    | DBA ROLE을 부여받은 유저                                          |
| SYSTEM | 데이터베이스의 모든 시스템 권한을 부여받은 DBA 유저<br/>Oracle 설치 완료 시에 패스워드 설정 |

### 2. 유저와 권한

- 유저생성과 시스템 권한 부여 : 롤(ROLE)을 이용하여 간편하고 쉽게 권한을 부여

- OBJECT에 대한 권한 부여 : 오브젝트 권한은 특정 오브젝트인 테이블, 뷰 등에 대한 SELECT, INSERT, DELETE, UPDATE 작업 명령어를 의미



### 3. ROLE을 이용한 권한 부여(중요)

- 많은 데이터베이스에서 유저들과 권한들 사이에서 중개 역할을 하는 ROLE을 제공한다. 
- 데이터베이스 관리자는 ROLE을 생성하고, ROLE에 각종 권한들을 부여한 후 
  ROLE을 다른 ROLE이나 유저에게 부여할 수 있다. 
- ROLE에 포함되어 있는 권한들이 필요한 유저에게는 해당 ROLE만을 부여함으로써 빠르고 정확하게 필요한 권한을 부여

![](assets/7114ce185537dae35acdd0eef8bbfc0f35bad83a.PNG)

![](assets/1733f458c6ceeb6a9003a58b2b7567916090baa7.PNG)



## 제 8절 절차형 SQL

### 1. 절차형 SQL 개요

- SQL에도 절차 지향적인 프로그램이 가능하도록 DBMS 벤더별로 
  PL(Procedural Language)/SQL(Oracle), SQL/PL(DB2), T-SQL(SQL Server) 등의 절차형 SQL을 제공하고 있다. 
- 절차형 SQL을 이용하면 SQL문의 연속적인 실행이나 조건에 따른 분기처리를 이용하여 특정 기능을 수행하는 
  저장 모듈을 생성할 수 있다.



### 2. PL/SQL 개요

- PL/SQL 특징
  
  - Oracle의 PL/SQL은 Block 구조로 되어있고 Block 내에는 DML 문장과 QUERY 문장, 
    그리고 절차형 언어(IF, LOOP) 등을 사용할 수 있으며, 절차적 프로그래밍을 가능하게 하는 트랜잭션 언어이다.

- PL/SQL 구조



![](assets/49b913e82a60ed55c9c00c00df9d5b386a650ce7.PNG)



### 3. T-SQL 개요

- T-SQL 특징
  
  - T-SQL은 근본적으로 SQL Server를 제어하기 위한 언어로서, T-SQL은 엄격히 말하면,  MS사에서 ANSI/ISO 표준의 SQL에 약간의 기능을 더 추가해 보완적으로 만든 것



### 4. Procedure의 생성과 활용

![](assets/f7fffb8b10ed2f2eba816e0c8d61c9fab18a8e4c.PNG)



### 5. User Dfined Function의 생성과 활용

- 절차형 SQL을 로직과 함께 데이터베이스 내에 저장해 놓은 명령문의 집합을 의미한다.



### 6. Trigger의 생성과 활용(중요)

- “특정한 테이블에 INSERT, UPDATE DELETE와 같은 DML문이 수행되었을 때, 
  데이터베이스에서 자동으로 동작하도록 작성된 프로그램” 
- 즉 사용자가 직접 호출하여 사용하는 것이 아니고 데이터베이스에서 자동적으로 수행하게 된다. 
  Trigger는 테이블과 뷰, 데이터베이스 작업을 대상으로 정의할 수 있으며, 
  전체 트랜잭션 작업에 대해 발생되는 Trigger와 각 행에 대해서 발생되는 Trigger가 있다. 
- Trigger는 데이터베이스에 의해 자동 호출되지만 결국 
  INSERT, UPDATE, DELETE 문과 하나의 트랜잭션 안에서 일어나는 일련의 작업들이라 할 수 있다. 
- Trigger는 데이터베이스 보안의 적용, 유효하지 않은 트랜잭션의 예방, 업무 규칙 자동 적용 제공 등에 사용될 수 있다.



### 7. 프로시저와 트리거의 차이(중요)

- 프로시저는 BEGIN ~ END 절 내의 COMMIT, ROLLBACK과 같은 트랜잭션 종료 명령어를 사용할 수 있지만, 데이터베이스 트리거는 BEGIN ~ END 절 내에 사용할 수 없다.



| 프로시저                   | 트리거                    |
| ---------------------- | ---------------------- |
| CREATE Procedure 문법사용  | CREATE Trigger 문법사용    |
| EXECUTE 명령어로 실행        | 생성 후 자동으로 실행           |
| COMMIT, ROLLBACK 실행 가능 | COMMIT, ROLLBACK 실행 안됨 |
