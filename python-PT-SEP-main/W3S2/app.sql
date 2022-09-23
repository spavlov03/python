USE w3s1_demo;
-- INSERT INTO users (name,email,password) VALUES ('John Doe','j@j.com','123456');
-- INSERT INTO users (name,email,password) VALUES ('Jane Doe','d@d.com','123456');
-- INSERT INTO users (name,email,password) VALUES ('Jack Bauer','b@b.com','123456');
-- INSERT INTO users (name,email,password) VALUES ('James Bond','jb@jb.com','123456');
-- SET SQL_SAFE_UPDATES = 1;

-- UPDATE 

UPDATE users SET name = "NEW NAME" WHERE id = 1;
UPDATE users SET name = "will Doe", email="w@w.com", password="123456" WHERE id = 2;
SELECT * FROM users;
INSERT INTO posts (content,user_id) VALUES ('My name is Bond,James Bond!',4),("I'm Jack Bauer the CTU Director",3);
SELECT * FROM posts;

SELECT * FROM users LEFT JOIN posts ON posts.user_id = users.id;
SELECT * FROM posts LEFT JOIN users ON posts.user_id = users.id;
SELECT * FROM users JOIN posts ON posts.user_id = users.id;
INSERT INTO posts (content,user_id) VALUES ('test12',3);
SELECT * FROM posts LEFT JOIN users ON posts.user_id = users.id WHERE users.name = "Jack Bauer";


INSERT INTO likes (post_id,user_id) VALUES(2,1),(3,4),(3,3);
SELECT * FROM likes;
