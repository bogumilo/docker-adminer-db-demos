import psycopg2

# Instantiate connection to db
conn = psycopg2.connect(
    database='demodb',
    user='admin',
    password='password',
    host='0.0.0.0'
)

# Start cursor
cur = conn.cursor()

# Create new table
cur.execute("create table if not exists companies (\
    id serial not null,\
    company_name VARCHAR(32),\
    country_hq VARCHAR(32),\
    certification_year VARCHAR(4),\
    industry VARCHAR(32),\
    countries VARCHAR(32) ,\
    url VARCHAR(256),\
    image_url VARCHAR(256))")


# Insert new rows
cur.execute("insert into companies (\
    company_name, country_hq, certification_year, industry, countries, url, image_url )\
        values ('Company_A', 'Warsaw', '2010', 'Insurance', 'Poland, Spain',\
            'https://example.pl', 'https://example.pl/image_company_a')")

# Query db with python
cur.execute("select * from companies")
rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:
    for row in rows:
        print(row)

# Close cursor and connection
cur.close()
conn.close()
