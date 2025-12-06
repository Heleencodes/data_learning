SELECT name FROM sqlite_master WHERE type='table';
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER
);

SELECT name FROM sqlite_master WHERE type='table';

INSERT INTO employees (name, salary) VALUES
('Sophie', 50000),
('Mark', 65000),
('Heleen', 999999);
SELECT * FROM employees;
DELETE FROM employees;  
SELECT * FROM employees;

INSERT INTO employees (name, salary) VALUES
('Betsie', 500),
('Klaas', 650),
('Jeroen', 999);
SELECT * FROM employees;
