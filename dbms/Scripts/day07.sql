SELECT  JOB_ID ,COUNT(JOB_ID)
FROM 	EMPLOYEES e 
GROUP BY JOB_ID ;
HAVING 
;

--1. employee 테이블에서 급여의 평균보다 작은 사원의 사원번호, 이름, 담업무, 급여, 부번호
SELECT 	EMPLOYEE_ID ,
		FIRST_NAME ||' '||LAST_NAME AS name,
		JOB_ID ,
		SALARY ,
		DEPARTMENT_ID 
FROM 	EMPLOYEES e 
WHERE 	SALARY < (SELECT avg(SALARY) FROM EMPLOYEES e2 );

--2. 
SELECT 	DEPARTMENT_ID , min(SALARY)
FROM 	EMPLOYEES e 
GROUP BY DEPARTMENT_ID 
HAVING min(salary)> (SELECT min(SALARY) FROM EMPLOYEES e2 WHERE DEPARTMENT_ID=100)
;

--3
SELECT  MANAGER_ID
FROM 	EMPLOYEES e
GROUP BY MANAGER_ID 
HAVING 	count(EMPLOYEE_ID) = (SELECT max(count(*))
							FROM 	EMPLOYEES e3 
							GROUP BY MANAGER_ID) 
;

--4 
SELECT 	DEPARTMENT_ID ,
		count(DEPARTMENT_ID)
FROM 	EMPLOYEES e 
GROUP BY DEPARTMENT_ID 
HAVING COUNT(DEPARTMENT_ID) = (SELECT max(count(DEPARTMENT_ID)) FROM EMPLOYEES e2 GROUP BY DEPARTMENT_ID )
;

--5 
SELECT 	EMPLOYEE_ID ,
		FIRST_NAME ||' '||LAST_NAME AS name,
		SALARY 
FROM 	EMPLOYEES e  
WHERE 	JOB_ID = (SELECT JOB_ID FROM EMPLOYEES e3 WHERE EMPLOYEE_ID=123) 
AND SALARY > (SELECT SALARY FROM EMPLOYEES e2 WHERE EMPLOYEE_ID = 192);

-- 테이블 생
CREATE TABLE EMPLOYEES2 (
	emloyee_id	NUMBER(10) ,
	name 		varchar2(20),
	salary		number(7,2) NOT NULL 
);

-- 기존 테이블과 동일하게 작성
CREATE TABLE EMPLOYEES3
AS 
SELECT *
FROM employees2;

-- 컬럼추가
ALTER TABLE EMPLOYEES2 ADD(
	manager_id	varchar2(10)
);

ALTER TABLE EMPLOYEES2 MODIFY(
	manager_id	varchar2(20)
);

-- 컬럼 삭제
ALTER TABLE EMPLOYEES2 DROP COLUMN manager_id;

INSERT INTO EMPLOYEES2 VALUES(1, '테스트',3);

-- 데이터 비우기
TRUNCATE TABLE EMPLOYEES2;

-- 테이블 삭제
DROP TABLE EMPLOYEES3;







