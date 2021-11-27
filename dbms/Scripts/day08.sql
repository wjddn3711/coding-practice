CREATE TABLE sample (
	deptNo	 number(20),
	deptName  varchar2(15),
	deploc  varchar2(15),
	deptManager  varchar2(10)
);

INSERT INTO sample values(10,'기획실','부산','홍길동');
INSERT INTO sample values(20,'전산실','서울','김말똥');
INSERT INTO sample(deptNo, deptName, deploc) values(30,'영업부실','광주');
INSERT INTO sample(deptNo, deptName, deploc) values(40,'영업실','공주');

UPDATE sample SET deptNo = 50
WHERE deptNo = 30;

UPDATE sample SET deploc = '인천'
WHERE deptName = '영업부';
DELETE sample WHERE deptname = '영업실';
DELETE sample WHERE deptname = '기획실';
DELETE sample WHERE deptname = '전산실';
DELETE sample WHERE deptname = '영업부실';
--DROP TABLE sample;

SELECT *
FROM SAMPLE ;
ROLLBACK;
COMMIT;