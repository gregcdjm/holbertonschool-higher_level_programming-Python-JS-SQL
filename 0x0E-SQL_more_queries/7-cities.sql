--bla bla
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
       state_id VARCHAR(256) NOT NULL,
       FOREIGN KEY(state_id) REFERENCES states(id)
);
