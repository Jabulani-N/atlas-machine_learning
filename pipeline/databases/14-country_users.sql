-- creates a table expanding on task 13's
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country VARCHAR(2) NOT NULL DEFAULT 'US'
);
