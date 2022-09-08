/*
 top_10_clients
 */
SELECT
    c.customer_id
  , c.customer_fname || ' ' || c.customer_lname AS customer_name
  , COUNT(DISTINCT o.order_id)                  AS completed_orders
FROM orders AS o
         INNER JOIN customers AS c
                    ON c.customer_id = o.order_customer_id
WHERE 1 = 1
  AND o.order_status = 'COMPLETE'
GROUP BY c.customer_id, customer_name
ORDER BY completed_orders DESC
LIMIT 10;