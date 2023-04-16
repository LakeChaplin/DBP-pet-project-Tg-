import psycopg2
import random

def connect_db():
    conn = psycopg2.connect(
        host='localhost',
        port='5433',
        database='for_pet_project',
        user='postgres'
    )
    return conn

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute('''CREATE TABLE IF NOT EXISTS posts
                   (id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    date TEXT NOT NULL,
                    url TEXT NOT NULL,
                    rating TEXT NOT NULL);''')
        conn.commit()

def insert_post(conn, title, author, date, url, rating):
    sql = """INSERT INTO posts(title, author, date, url, rating)
         VALUES(%s, %s, %s, %s, %s) RETURNING id;"""
    with conn, conn.cursor() as cur:
        cur.execute(sql, (title, author, date, url, rating))
        post_id = cur.fetchone()[0]
    return post_id

def show_all_posts(conn):
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM posts')
        rows = cur.fetchall()
        for row in rows:
            print(row)

def get_random_post(conn):
    """Return a random post from the database."""
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM posts ORDER BY RANDOM() LIMIT 1;")
        post = cur.fetchone()

    if post:
        post_id, title, author, date, url, rating = post
        return {
            'id': post_id,
            'title': title,
            'author': author,
            'date': date,
            'url': url,
            'rating': rating
        }
    else:
        return None

def close_connection(conn):
    conn.close()





    # # execute a query to check if the table was created successfully
    # cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    # tables = cur.fetchall()
    # print(tables)

# # Show all columns in DB
# with conn.cursor() as cur:
#     cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'posts'")
#     rows = cur.fetchall()
#     for row in rows:
#         print(f"Column name: {row[0]}, data type: {row[1]}")
    

# # !!!! drop the table !!!!!
# with conn.cursor() as cur:
#     cur.execute("DROP TABLE IF EXISTS posts;")
#     conn.commit()

    # # drop column body
    # with conn.cursor() as cur:
    #     cur.execute("ALTER TABLE posts DROP COLUMN body;")
    # conn.commit()
