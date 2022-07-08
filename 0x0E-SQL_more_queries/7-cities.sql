--bla bla
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
CREATE TABLE IF NOT EXISTS cities (
       id INT,
       state_id VARCHAR(256) NOT NULL,
       score INT,
       FOREIGN KEY(state_id)
);

INSERT INTO cities (id, name, score)
VALUES
	(1, "John", 10),
       	(2, "Alex", 3),
       	(3, "Bob", 14),
       	(4, "George", 8);
