--bla bla
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities FROM hbtn_0d_usa(
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
       state_id VARCHAR(256) NOT NULL,
       score INT,
       FOREIGN KEY(state_id)
);
