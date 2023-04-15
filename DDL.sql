use Globant;
GO
drop table if exists departments;
CREATE TABLE departments (
	id INT NOT NULL PRIMARY KEY, 
	department VARCHAR(255)
);
GO
drop table if exists jobs;
CREATE TABLE jobs (
	id INT NOT NULL PRIMARY KEY, 
	job  VARCHAR(255) 
);
GO
drop table if exists hired_employees;
CREATE TABLE hired_employees (
	id INT NOT NULL PRIMARY KEY, 
	name VARCHAR(255) , 
	datetime VARCHAR(255),
	department_id INT FOREIGN KEY REFERENCES departments(id),
	job_id INT FOREIGN KEY REFERENCES jobs(id)
);