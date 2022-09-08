/*
 top_5_clients_fraud
 */
SELECT
    c.customer_id
  , c.customer_fname || ' ' || c.customer_lname AS customer_name
  , COUNT(DISTINCT o.order_id)                  AS orders
FROM orders AS o
         INNER JOIN customers AS c
                    ON c.customer_id = o.order_customer_id
WHERE 1 = 1
  AND o.order_status = 'SUSPECTED_FRAUD'
GROUP BY c.customer_id, customer_name
HAVING COUNT(DISTINCT o.order_id) >= 3
ORDER BY orders DESC
LIMIT 5;