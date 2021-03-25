USE TestGreenWorld;
go
CREATE SCHEMA test;
go

-- create tables
CREATE TABLE test.pump (
	p_id INT IDENTITY (1, 1) PRIMARY KEY,
	p_name VARCHAR (15) NULL,
	p_plant VARCHAR (4) NULL
);
CREATE TABLE test.criteria (
	c_id INT IDENTITY (1, 1) PRIMARY KEY,
	c_name VARCHAR (10) NOT NULL,
	c_start DATETIME NOT NULL,
	c_end DATETIME NULL,
	c_w_id INT NOT NULL,
	c_status BIT,
	FOREIGN KEY (c_w_id) REFERENCES test.pump (p_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- good, now add column p_plant
ALTER TABLE test.pump
ADD p_plant VARCHAR (4);
--good


-- get all criterias ever present
/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) p.[p_id]
      ,p.[p_name]
      ,p.[p_plant]
	  ,c.c_id
	  ,c.c_name
	  ,c.c_status
	  ,c.c_w_id
	  ,c.c_start
	  ,c.c_end
  FROM [TestGreenWorld].[test].[pump] as p
  INNER JOIN TestGreenWorld.test.criteria c ON c.c_w_id = p.p_id
  and p.p_id = 1
  
  -- get running criteria
  /****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) p.[p_id]
      ,p.[p_name]
      ,p.[p_plant]
	  ,c.c_id
	  ,c.c_name
	  ,c.c_status
	  ,c.c_w_id
	  ,c.c_start
	  ,c.c_end
  FROM [TestGreenWorld].[test].[pump] as p
  INNER JOIN TestGreenWorld.test.criteria c ON c.c_w_id = p.p_id
  and p.p_id = 1
  and c_status =1

  -- get running cri where start > date for all pumps
  
SELECT TOP (1000) p.[p_id]
      ,p.[p_name]
      ,p.[p_plant]
	  ,c.c_id
	  ,c.c_name
	  ,c.c_status
	  ,c.c_w_id
	  ,c.c_start
	  ,c.c_end
  FROM [TestGreenWorld].[test].[pump] as p
  INNER JOIN TestGreenWorld.test.criteria c ON c.c_w_id = p.p_id
  --and p.p_id = 1
  and c.c_start > '2021-01-05 12:30'

  --

 -- get running cri where start is + 30 min from a date for all pumps
 -- db
 --c_id	c_name	c_start	c_end	c_w_id	c_status
--1	start	2021-01-01 12:00:00.000	2021-01-05 12:59:00.000	1	0
--2	run	    2021-01-05 13:00:00.000	NULL	1	1
--3	start	2021-01-05 13:10:00.000	NULL	2	1
--4	start	2021-01-04 00:00:00.000	NULL	3	0

SELECT TOP (1000) p.[p_id]
      ,p.[p_name]
      ,p.[p_plant]
	  ,c.c_id
	  ,c.c_name
	  ,c.c_status
	  ,c.c_w_id
	  ,c.c_start
	  ,c.c_end
  FROM [TestGreenWorld].[test].[pump] as p
  INNER JOIN TestGreenWorld.test.criteria c ON c.c_w_id = p.p_id
  where c.c_start > DATEADD(mi, 30, '2021-01-05 12:20') -- is 2021-01-05 12:50:00.000
  --and p.p_id = 1
  
-- returns
-- 1	P1	EAR	2	run	1	1	2021-01-05 13:00:00.000	NULL
-- 2	P2	EAR	3	start	1	2	2021-01-05 13:10:00.000	NULL

select DATEADD(mi, 30, '2021-01-05 12:20')
-- 2021-01-05 12:50:00.000
select DATEADD(mi, -30, '2021-01-05 12:20')
-- 2021-01-05 11:50:00.000

-- get running cri where start is + 30 min from a date for all pumps with var
DECLARE @dt datetime = '2021-01-05 12:20';

SELECT TOP (1000) p.[p_id]
      ,p.[p_name]
      ,p.[p_plant]
	  ,c.c_id
	  ,c.c_name
	  ,c.c_status
	  ,c.c_w_id
	  ,c.c_start
	  ,c.c_end
  FROM [TestGreenWorld].[test].[pump] as p
  INNER JOIN TestGreenWorld.test.criteria c ON c.c_w_id = p.p_id
  where c.c_start > DATEADD(mi, 30, @dt)
  --and p.p_id = 1