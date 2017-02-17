# _*_ coding: utf-8 _*_
import sqlite3
from project import db 

from project._config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection: 
	c = connection.cursor()

	c.execute("""ALTER TABLE blog_posts RENAME TO old_posts""")

	db.create_all()

	c.execute("""SELECT title, subtitle, cover_path, date, body, views
		        FROM old_posts
		        ORDER BY post_id ASC""")

	data = [(row[0], row[1], row[2], row[3], row[4], u'محمد گلی', row[5]
		     ) for row in c.fetchall()]

	c.executemany("""INSERT INTO blog_posts (title, subtitle, cover_path, date, body, author, views)
		VALUES (?, ?, ?, ?, ?, ?, ?)""", data)

	c.execute("DROP TABLE old_posts")