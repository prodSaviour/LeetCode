# Write your MySQL query statement below
select p.product_name, t.year, t.price from sales t join product p on t.product_id=p.product_id;