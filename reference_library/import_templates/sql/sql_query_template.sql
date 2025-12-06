-- === Basic SELECT template ===
SELECT
    *
FROM
    your_table
WHERE
    1 = 1
    -- AND column = 'value'
ORDER BY
    column ASC
LIMIT 50;


-- === INSERT example ===
INSERT INTO your_table (col1, col2, col3)
VALUES ('value1', 'value2', 'value3');


-- === UPDATE example ===
UPDATE your_table
SET column = 'new_value'
WHERE id = 123;


-- === DELETE example ===
DELETE FROM your_table
WHERE id = 123;
