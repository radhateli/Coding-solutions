# GSQ14

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-14T13:31:30.898Z  

```sql
/* Write a query to create a table employee with the mentioned constraints on the columns : 
employee_id - PRIMARY KEY, 
employee_Name -UNIQUE, 
department -NOT NULL CHECK (department IN ('Sales', 'Finance', 'Operations')) */

CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    employee_Name TEXT UNIQUE,
    department TEXT NOT NULL CHECK (
        department IN ('Sales', 'Finance', 'Operations')
    )
);
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ14)