import pymysql

# Connect to the database
conn = pymysql.connect(host='localhost',
                       user='demouser',
                       password='password',
                       database='demodb',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor,
                       connect_timeout=31536000)
# Start cursor
cur = conn.cursor()
conn.commit()

# Create new table
cur.execute("create table companies (\
    id int(11) not null auto_increment,\
    company_name VARCHAR(32),\
    country_hq VARCHAR(32),\
    certification_year VARCHAR(4),\
    industry VARCHAR(32),\
    countries VARCHAR(32) ,\
    url VARCHAR(256),\
    image_url VARCHAR(256),\
    PRIMARY KEY (`id`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin \
AUTO_INCREMENT=1")

# Insert new rows
cur.execute("insert into companies (\
    company_name, country_hq, certification_year, industry, countries, url, image_url )\
        values ('Company_A', 'Warsaw', '2010', 'Insurance', 'Poland, Spain',\
            'https://example.pl', 'https://example.pl/image_company_a')")

# Save changes
conn.commit()

# Query db with python
cur.execute("select * from companies")
rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:
    for row in rows:
        print(row)

# Close cursosr and connection
cur.close()
conn.close()
