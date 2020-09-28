import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
cursor = conn.cursor()

#What are the most expensive items in the database
query1 = '''
SELECT 
	ProductName,
	UnitPrice
FROM Product
ORDER BY 
	UnitPrice DESC
LIMIT 10;
'''
result = cursor.execute(query1).fetchall()
print(f'Ten Most Expensive Items {result}')

#What is the average age of employee at time of hiring
query2 = '''
SELECT 
	AVG(HireDate - BirthDate)
FROM Employee;
'''
result2 = cursor.execute(query2).fetchone()
print(f'What is the average age of employees at time of hire? {result2}')

#What are the 10 most expensive items in the database and their suppliers
query3='''
SELECT 
	p.ProductName,
	p.UnitPrice,
	s.CompanyName AS Supplier
FROM Product AS p 
JOIN Supplier AS s 
ON p.SupplierId = s.Id
ORDER BY 
	UnitPrice DESC
LIMIT 10;
'''
result3 = cursor.execute(query3).fetchall()
print(f'Ten Most Expensive Items and their supplier {result3}')

#What is the largest category by number of unique products 
query4 = '''
SELECT 
	COUNT(DISTINCT Product.ProductName) AS UniqueProducts,
	Category.CategoryName
FROM Product
JOIN Category
ON Product.CategoryId = Category.Id
GROUP BY Category.CategoryName
ORDER BY UniqueProducts DESC
LIMIT 1;
'''
result4 = cursor.execute(query4).fetchall()
print(f'What is the largest category by number of unique products? {result4}')

cursor.close()
conn.close()

#Results
'''$ python northwind.py
Ten Most Expensive Items [('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81), ('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55), ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3), ('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]
What is the average age of employees at time of hire? (37.22222222222222,)
Ten Most Expensive Items and their supplier [('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'), ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'), ('Mishi Kobe Niku', 97, 'Tokyo Traders'), ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'), ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'), ('Raclette Courdavault', 55, 'Gai pâturage'), ('Manjimup Dried Apples', 53, "G'day, Mate"), ('Tarte au sucre', 49.3, "Forêts d'érables"), ('Ipoh Coffee', 46, 'Leka Trading'), ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]
What is the largest category by number of unique products? [(13, 'Confections')]
(Sprint_Challange) 
'''