import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS demo_data (
    s TEXT, 
    x INT,
    y INT 
)
'''
cursor.execute(create_table_query)

sample_data = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

for row in sample_data:
    insert_query = f'''INSERT INTO demo_data (s, x, y)
    VALUES {row};
    '''
    cursor.execute(insert_query)
conn.commit()

# HOW MANY ROWS (EXPECTING 3)
query1 = 'SELECT COUNT(s) FROM demo_data'
result = cursor.execute(query1).fetchone()
print(f'How many rows in the database?, {result}')

#HOW MANY ROWS WHERE X AND Y ARE AT LEAST 5 (EXPECT 2):
query2 ='''
SELECT COUNT(*)
FROM demo_data
WHERE(x >= 5 AND y >=5)
'''
result2 = cursor.execute(query2).fetchone()
print(f'How Many entries where x and y are greater than 5? {result2}')

#HOW MANY UNIQUE VALUES OF Y ARE THERE? (EXPECT 2)
query3 = '''
SELECT COUNT(DISTINCT y)
FROM demo_data
'''
result3 = cursor.execute(query3).fetchone()
print(f'How many unique values in the table for y? {result3}')

cursor.close()
conn.close()

'''
Result = zacks@LAPTOP-CVVHTDI0 MINGW64 ~/Desktop/Sprint_Challange
$ python part_1.py
How many rows in the database?, (3,)
How Many entries where x and y are greater than 5? (2,)
How many unique values in the table for y? (2,)
(Sprint_Challange) 
'''