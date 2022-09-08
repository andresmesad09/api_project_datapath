/*
 top_categories
 */
WITH count_by_category AS (
    SELECT c.category_name
    , count(DISTINCT o.order_id) AS count_of_orders
    FROM orders AS o
             INNER JOIN order_items AS oi
                        ON oi.order_item_order_id = o.order_id
             INNER JOIN products AS p
                        ON p.product_id = oi.order_item_product_id
             INNER JOIN categories AS c
                        ON c.category_id = p.product_category_id
    WHERE 1 = 1
      AND o.order_status = 'COMPLETE'
    GROUP BY c.category_name
)
SELECT *
FROM count_by_category
ORDER BY count_of_orders DESC
LIMIT 5;