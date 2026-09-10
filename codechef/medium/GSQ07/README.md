# GSQ07

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### How to insert to a table

Write a query to add the below mentioned employee details to the 'employee' table.

```
  Employee_id - 6, 
  Employee_Name - 'Brandon Kim', 
  Department - 'Operations'

```

Refer to the  **employee**  table created in the previous problem.

```
┌─────────────┬────────────────┬────────────┐
│ Employee_id │ Employee_Name  │ Department │
├─────────────┼────────────────┼────────────┤
│ 1           │ Kayla Thompson │ Sales      │
│ 2           │ Ethan Chen     │ Operations │
│ 3           │ Julia Lee      │ Hr         │
│ 4           │ Marcus Garcia  │ Product    │
│ 5           │ Samantha Park  │ Operations │
└─────────────┴────────────────┴────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-10T14:19:42.098Z  

```sql
/* Write a query to add the below mentioned employee details to the EMPLOYEE table.
Employee id: 06, Employee Name: Brandon Kim, Department: Operations
*/
INSERT INTO employee VALUES (6, 'Brandon Kim', 'Operations');
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ07)