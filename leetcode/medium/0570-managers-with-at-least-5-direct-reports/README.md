# Managers with at Least 5 Direct Reports

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Table: `Employee`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.

```

 

Write a solution to find managers with at least  **five direct reports**.

Return the result table in  **any order**.

The result format is in the following example.

 

 **Example 1:** 

```
Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+

```

## Solution

**Language:** SQL  
**Runtime:** 373 ms (beats 38.20%)  
**Memory:** 0B (beats 100.00%)  
**Submitted:** 2026-07-15T10:17:31.606Z  

```sql
# Write your MySQL query statement below
SELECT a.name 
FROM Employee as a
JOIN Employee as b 
ON a.id = b.managerId 
GROUP BY a.id
HAVING COUNT(b.id)>=5;
```

---

[View on LeetCode](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/)