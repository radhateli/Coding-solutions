/* Debug this query to get the correct output */

SELECT DISTINCT passenger_name
FROM flights
WHERE gender = 'Male'
AND origin = 'Mumbai';