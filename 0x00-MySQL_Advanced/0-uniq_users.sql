-- Create table users script
-- Columns (id (int, auto increment, not null), email(varchar(255)), name(varchar(255))
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255),
);
