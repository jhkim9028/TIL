# 제1장 SQL 기본

## 제1절 관계형 데이터베이스 개요

### 1. 데이터베이스

- '특정 기업이나 조직 또는 개인이 필요에 의해 데이터를 일정한 형태로 저장한 것'

### 2. SQL(중요)

- SQL은 관계형데이터베이스에서 데이터 정의, 데이터 조작, 데이터 제어 를 하기 위해 사용하는 언어
  
  - 데이터 조작어(DML) - SELECT, INSERT, UPDATE, DELETE(NOT AUTO COMMIT)
  
  - 데이터 정의어(DDL) - CREATE, ALTER, DROP, RENAME(AUTO COMMIT)
  
  - 데이터 제어어(DCL) - GRANT, REVOKE
  
  - 트랜잭션 제어어(TCL) - COMMIT, ROLLBACK

- | 명령어의 종류                                      | 명령어                                  | 설명                                                                                                                        |
  | -------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
  | 데이터 조작어(DML: Data Manipulation Language)     | SELECT                               | 데이터베이스에 들어 있는 데이터를 조회하거나 검색하기 위한 명령어를 말하는 것으로 RETRIEVE 라고도 한다.                                                            |
  |                                              | INSERT<br/>UPDATE<br/>DELETE         | 데이터베이스의 테이블에 들어 있는 데이터에 변형을 가하는 종류의 명령어들을 말한다. 예를 들어 데이터를 테이블에 새로운 행을 집어넣거나, 원하지 않는 데이터를 삭제하거나 수정하는 것들의 명령어들은 DML이라고 부른다. |
  | 데이터 정의어(DDL : Data Definition Language)      | CREATE<br/>ALTER<br/>DROP<br/>RENAME | 테이블과 같은 데이터 구조를 정의하는데 사용되는 명령어들로 그러한 구조를 생성하거나 변경하거나 삭제하거나 이름을 바꾸는 데이터 구조와 관련된 명령어들을 DDL이라고 부른다.                          |
  | 데이터 제어어(DCL : Data Control Language)         | GRANT<br/>REVOKE                     | 데이터베이스에 접근하고 객채들을 사용하도록 권한을 주고 회수하는 명령어를 DCL이라고 부른다.                                                                      |
  | 트랜잭션 제어어(TCL : Transaction Control Language) | COMMIT<br/>ROLLBACK                  | 논리적인 작업의 단위를 묶어서 DML에 의해 조작된 결과를 작업단위(트랜잭션) 별로 제어하는 명령어를 말한다.                                                             |

### 3. TABLE

- 테이블은 하나 이상의 칼럼을 가져야 한다. 관계형 데이터베이스에서는 모든 데이터를 칼럼과 행의 2차원 구조로 나타낸다.

### 4. ERD(Entity Relationship Diagram)

- "관계의 의미를 직관적으로 표현할 수 있는 수단" / 구성요소 3개는 -> 엔티티, 관계, 속성
