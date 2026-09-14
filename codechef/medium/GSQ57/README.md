# GSQ57

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-14T14:01:39.518Z  

```sql
/*Write a query which does the following
- Delete the entire row of the customer with customer id 1.
- Output the entire table once the above action is performed. */

DELETE FROM customer 
WHERE Id = 1;

SELECT * FROM customer; 
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ57)