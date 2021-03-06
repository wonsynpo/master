/*
查找所有已经分配部门的员工的last_name和first_name
CREATE TABLE `dept_emp` (
`emp_no` int(11) NOT NULL,
`dept_no` char(4) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));


CREATE TABLE `employees` (
`emp_no` int(11) NOT NULL,
`birth_date` date NOT NULL,
`first_name` varchar(14) NOT NULL,
`last_name` varchar(16) NOT NULL,
`gender` char(1) NOT NULL,
`hire_date` date NOT NULL,
PRIMARY KEY (`emp_no`));

输出描述：
last_name	first_name	dept_no
Facello		Georgi			d001


select employees.last_name,employees.first_name,dept_emp.dept_no
from employees,dept_emp
where employees.emp_no=dept_emp.emp_no;

不能要order by,根据题目要求来吧
*/
select employees.last_name,employees.first_name,dept_emp.dept_no
from employees,dept_emp
where employees.emp_no=dept_emp.emp_no; and
dept_emp.dept_no is not null;