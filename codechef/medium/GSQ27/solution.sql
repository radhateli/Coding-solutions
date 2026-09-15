/* Debug this query to meet the following conditons
- Passenger gender - Female AND
- Flight destination - Delhi
*/

select * from flights
where Gender like '%Female%'
and Destination like '%Delhi%';