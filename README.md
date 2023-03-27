# python-newsfeed

# Run Virtual Environment
. venv/bin/activate

# Run app
.python3 -m flask run

# MySQL shell command
mysql -u root -p
CREATE DATABASE python_news_db;
SHOW DATABASES;
SELECT * FROM users;
USE <database>
SELECT * FROM users;
SELECt * FROM votes;
SELECT id, title FROM posts;

# Run seeds
python3 seeds.py

# Run flask
python3 -m flask run