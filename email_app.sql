

CREATE DATABASE email_app_db;
USE email_app_db;
-- user table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);
ALTER TABLE users ADD COLUMN email VARCHAR(100) UNIQUE;
select* from users;
DROP TABLE users;

DROP TABLE users;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);






-- emails table
CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_id INT NOT NULL,
    recipient_id INT NOT NULL,
    subject VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    is_private BOOLEAN DEFAULT FALSE,
    expiry_date DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE emails;

-- Then recreate the corrected table emails
CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_email VARCHAR(100) NOT NULL,
    recipient_email VARCHAR(100) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    is_private BOOLEAN DEFAULT FALSE,
    expiry_date DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE emails;

SELECT * FROM emails;
select* from users;

CREATE TABLE IF NOT EXISTS emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_id INT NOT NULL,
    recipient_id INT NOT NULL,
    subject VARCHAR(255),
    body TEXT,
    is_private BOOLEAN DEFAULT FALSE,
    expiry_date DATETIME DEFAULT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE emails;

-- id emails table
CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_id INT NOT NULL,
    recipient_id INT NOT NULL,
    subject VARCHAR(255),
    body TEXT,
    is_private BOOLEAN DEFAULT FALSE,
    expiry_date DATETIME DEFAULT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

USE email_app_db;
select*from emails;


CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_email VARCHAR(100) NOT NULL,
    recipient_email VARCHAR(100) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    is_private BOOLEAN DEFAULT FALSE,
    expiry_date DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN DEFAULT FALSE
);

select*from emails;
DROP TABLE emails;

CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_id INT NOT NULL,
    recipient_id INT NOT NULL,
    subject VARCHAR(255),
    body TEXT,
    is_private BOOLEAN DEFAULT FALSE,
    expiry_date DATETIME NULL,
    FOREIGN KEY (sender_id) REFERENCES users(id),
    FOREIGN KEY (recipient_id) REFERENCES users(id)
);
select*from emails;
DELETE FROM emails;




