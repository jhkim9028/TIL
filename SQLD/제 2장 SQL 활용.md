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
