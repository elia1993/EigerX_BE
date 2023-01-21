SELECT d.NAME department_name,COUNT(E.DEPT_ID) employee_count
FROM department d LEFT OUTER JOIN employee e ON d.ID = e.DEPT_ID
GROUP BY D.NAME
ORDER BY employee_count desc, d.NAME
