--Creates a table "users" if it doesn't exist
CREATE TABLE if NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255)
);
