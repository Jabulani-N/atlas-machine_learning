-- creates a table expanding on task 13's
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    coutnry VARCHAR(2) DEFAULT 'US' CHECK (coutnry REGEXP '^[A-Z]{2}$');
);
