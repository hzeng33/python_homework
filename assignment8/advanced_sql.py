import sqlite3

# Task 1: Complex JOINs with Aggregation
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query = """
SELECT o.order_id,
       SUM(p.price * l.quantity) AS total_price
FROM orders AS o
JOIN line_items AS l ON o.order_id = l.order_id
JOIN products AS p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id LIMIT 5;
"""

cursor.execute(query)
results = cursor.fetchall()
print("The total price of each of the first 5 orders: \n")
print(results)
print()

conn.close()


# Task 2: Understanding Subqueries
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query = """
SELECT c.customer_name, AVG(totalOrders.total_price) AS average_total_price
FROM customers AS c
LEFT JOIN (
    SELECT o.customer_id AS customer_id_b, SUM(l.quantity * p.price) AS total_price
    FROM orders AS o 
    JOIN line_items AS l ON o.order_id = l.order_id 
    JOIN products AS p ON l.product_id = p.product_id
    GROUP BY o.order_id
) AS totalOrders ON c.customer_id = totalOrders.customer_id_b
GROUP BY c.customer_id
ORDER BY c.customer_name;
"""

cursor.execute(query)
results = cursor.fetchall()
print("The average price of each customer's order: \n")
print(results)
print()

conn.close()


# Task 3: An Insert Transaction Based on Data
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

try:
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = ?", ('Perez and Sons',))
    customer_id = cursor.fetchone()[0]
    
    cursor.execute("SELECT employee_id FROM employees WHERE first_name=? AND last_name=?", ('Miranda', 'Harris'))
    employee_id = cursor.fetchone()[0]
    
    cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, DATE('now'))", (customer_id, employee_id))
    order_id = cursor.lastrowid
    
    for product_id in product_ids:
        cursor.execute("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)", (order_id, product_id, 10))
    
    conn.commit()
except Exception as e:
    conn.rollback()  # Rollback transaction if there's an error
    print("Error:", e)
    
query = """
SELECT l.line_item_id, p.product_name, l.quantity
FROM line_items AS l
JOIN products AS p ON l.product_id = p.product_id
WHERE l.order_id = ?
"""
cursor.execute(query, (order_id,))
result = cursor.fetchall()
print("Result from task 3: \n")
print(result)
print()

conn.close()


# Task 4: Aggregation with HAVING
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query = """
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
FROM employees AS e
JOIN orders AS o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) > 5;
"""

cursor.execute(query)
result = cursor.fetchall()
print("Result from task 4: \n")
print(result)
print()
conn.close()