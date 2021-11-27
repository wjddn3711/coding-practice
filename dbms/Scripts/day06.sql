SELECT 	*
FROM 	EMPLOYEES e 
;
--1
SELECT 	e.FIRST_NAME ||' '||e.LAST_NAME AS name, 
		j.JOB_TITLE , 
		e.DEPARTMENT_ID , 
		d.DEPARTMENT_NAME 
FROM 	JOBS j 
	INNER JOIN EMPLOYEES e 
	ON j.JOB_ID = e.JOB_ID 
	INNER JOIN  DEPARTMENTS d 
	ON e.DEPARTMENT_ID = d.DEPARTMENT_ID 
WHERE 	e.DEPARTMENT_ID = 30
;
--2
SELECT 	e.FIRST_NAME ||' '||e.LAST_NAME AS name,
		j.JOB_TITLE ,
		e.DEPARTMENT_ID 
FROM 	EMPLOYEES e 
	INNER JOIN  DEPARTMENTS d
	ON 	e.DEPARTMENT_ID = d.DEPARTMENT_ID 
	INNER JOIN JOBS j 
	ON e.JOB_ID =j.JOB_ID
WHERE 	e.COMMISSION_PCT IS NOT null
;

--3
SELECT 	e.FIRST_NAME ||' '||e.LAST_NAME AS name,
		j.JOB_TITLE ,
		e.DEPARTMENT_ID ,
		d.DEPARTMENT_NAME 
FROM 	EMPLOYEES e 
	INNER JOIN  DEPARTMENTS d 
	ON 	e.DEPARTMENT_ID = d.DEPARTMENT_ID 
	INNER JOIN JOBS j 
	ON e.JOB_ID =j.JOB_ID 
WHERE 	d.LOCATION_ID = 2500
;		

--4
SELECT 	e.FIRST_NAME ||' '||e.LAST_NAME AS name,
		d.DEPARTMENT_NAME 
FROM 	EMPLOYEES e 
	INNER JOIN  DEPARTMENTS d 
	ON 	e.DEPARTMENT_ID = d.DEPARTMENT_ID 
WHERE 	e.FIRST_NAME ||' '||e.LAST_NAME LIKE '%A%'
ORDER BY e.FIRST_NAME ||' '||e.LAST_NAME
;	

--5
SELECT 	e.FIRST_NAME ||' '||e.LAST_NAME AS name,
		e.MANAGER_ID ,
		e2.FIRST_NAME ||' '||e2.LAST_NAME AS manager
FROM 	EMPLOYEES e 
	INNER JOIN EMPLOYEES e2 
	ON e.MANAGER_ID = e2.EMPLOYEE_ID 
;	

--6
SELECT 	e.FIRST_NAME ||' '||e.LAST_NAME AS name,
		d.DEPARTMENT_NAME 
FROM 	EMPLOYEES e 
	INNER JOIN  DEPARTMENTS d 
	ON 	e.DEPARTMENT_ID = d.DEPARTMENT_ID 
WHERE 	e.SALARY BETWEEN 3000 AND 5000
;	

--7
SELECT 	e.FIRST_NAME ||' '||e.LAST_NAME AS name,
		e.SALARY ,
		l.CITY 
FROM 	EMPLOYEES e 
	INNER JOIN  DEPARTMENTS d 
	ON 	e.DEPARTMENT_ID = d.DEPARTMENT_ID 
	INNER JOIN LOCATIONS l 
	ON 	d.LOCATION_ID = l.LOCATION_ID 
WHERE 	e.SALARY <=3000
ORDER BY SALARY 
;	

SELECT 	round(avg(SALARY),2)
FROM 	EMPLOYEES e 
;

SELECT 	FIRST_NAME ||' '||LAST_NAME AS NAME,
		EMPLOYEE_ID 
FROM 	EMPLOYEES e 
WHERE 	SALARY < (SELECT round(avg(salary)) FROM EMPLOYEES e2 )
;

SELECT 	LOCATION_ID 
FROM 	LOCATIONS l 
WHERE 	COUNTRY_ID = 'US'
;

SELECT 	*
FROM 	DEPARTMENTS d 
WHERE 	LOCATION_ID IN (1400,1500,1600,1700);
		

SELECT 	*
FROM 	DEPARTMENTS d 
WHERE 	LOCATION_ID IN (SELECT LOCATION_ID FROM LOCATIONS l WHERE COUNTRY_ID = 'US');

SELECT *
FROM 	EMPLOYEES e ;

--employee 테이블에서 Kochhar 의 (last_name)의 급여보다 많은 사원의 정보를 사원번호, 이름, 담당업무, 급여를 출력하
SELECT 	EMPLOYEE_ID ,
		FIRST_NAME ||' '||LAST_NAME AS NAME,
		JOB_ID ,
		SALARY 
FROM 	EMPLOYEES e 
WHERE 	SALARY > (SELECT SALARY FROM EMPLOYEES e2 WHERE LAST_NAME='Kochhar')
;

--employee 테이블에서 first,lastname 출력, 월급이 가장 작은 사원
SELECT 	FIRST_NAME ||' '||LAST_NAME AS NAME
FROM 	EMPLOYEES e 
WHERE 	SALARY = (SELECT min(SALARY) FROM EMPLOYEES e2 )
;

SELECT 	FIRST_NAME ||' '||LAST_NAME AS NAME,
		j.JOB_TITLE 
FROM 	EMPLOYEES e INNER JOIN JOBS j ON e.JOB_ID =j.JOB_ID 
WHERE 	SALARY = (SELECT max(SALARY) FROM EMPLOYEES e2 )
;

SELECT 	FIRST_NAME ||' '||LAST_NAME AS NAME,
		j.JOB_TITLE 
FROM 	EMPLOYEES e INNER JOIN JOBS j ON e.JOB_ID =j.JOB_ID 
WHERE 	SALARY > (SELECT avg(SALARY) FROM EMPLOYEES e2 )
;

SELECT 	SALARY 
FROM 	EMPLOYEES e 
GROUP BY SALARY ;
