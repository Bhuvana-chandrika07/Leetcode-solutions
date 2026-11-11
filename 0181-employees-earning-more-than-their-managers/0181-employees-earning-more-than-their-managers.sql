SELECT utk.name AS Employee
 FROM Employee utk,Employee MGR
WHERE utk.managerId=MGR.id AND utk.salary>MGR.salary
