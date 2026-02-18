# Write your MySQL query statement below
DELETE FROM person
WHERE id NOT IN (
    SELECT keep_id
    FROM (
        SELECT MIN(id) AS keep_id
        FROM person
        GROUP BY email
    ) AS t
);