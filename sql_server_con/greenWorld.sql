USE TestGreenWorld;
go
CREATE SCHEMA test;
go

-- create tables
CREATE TABLE test.pump (
	p_id INT IDENTITY (1, 1) PRIMARY KEY,
	p_name VARCHAR (15)
);
CREATE TABLE test.criteria (
	c_id INT IDENTITY (1, 1) PRIMARY KEY,
	c_name VARCHAR (10) NOT NULL,
	c_start VARCHAR (20),
	c_end VARCHAR (20),
	c_w_id INT NOT NULL,
	c_status BIT,
	FOREIGN KEY (c_w_id) REFERENCES test.pump (p_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- good, now add column p_plant
ALTER TABLE test.pump
ADD p_plant VARCHAR (4);
--good


-- get all criteria history to a pump
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
  
  -- get running criteriato a pump
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