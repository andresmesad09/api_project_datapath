/*
 top_products
 */
SELECT
    p.product_name
  , COUNT(DISTINCT o.order_id)  AS completed_orders
  , SUM(oi.order_item_subtotal) AS income
FROM orders AS o
         INNER JOIN order_items AS oi
                    ON oi.order_item_order_id = o.order_id
         INNER JOIN products AS p
                    ON p.product_id = oi.order_item_product_id
WHERE 1 = 1
  AND o.order_status = 'COMPLETE'
GROUP BY p.product_name
ORDER BY completed_orders DESC
LIMIT 10;