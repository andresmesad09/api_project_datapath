SELECT
    d.department_name
  , SUM(oi.order_item_subtotal) AS income
FROM orders AS o
         INNER JOIN order_items AS oi
                    ON oi.order_item_order_id = o.order_id
         INNER JOIN products AS p
                    ON p.product_id = oi.order_item_product_id
         INNER JOIN categories AS c
                    ON c.category_id = p.product_category_id
         INNER JOIN departments AS d
                    ON d.department_id = c.category_department_id
WHERE 1 = 1
  AND o.order_status = 'COMPLETE'
GROUP BY d.department_name
ORDER BY income DESC;