/*Write a query to set the Department as 'HR', for the employee with employee_id 2 to the existing table employee. */
UPDATE employee 
SET Department = 'Hr'
WHERE employee_id = 2;

SELECT *
FROM employee;