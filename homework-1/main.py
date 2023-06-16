import csv
import psycopg2


with psycopg2.connect(host="localhost", database="north", user="postgres", password="alzy") as conn:
    with conn.cursor() as cur:
        """
        Загрузка данных из файла CSV в базу данных.
        """
        with open('north_data/customers_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                customer_id, company_name, contact_name = row
                cur.execute("INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                            (customer_id, company_name, contact_name))

        with open('north_data/employees_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                employee_id, first_name, last_name, title, birth_date, notes = row
                cur.execute("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)",
                            (employee_id, first_name, last_name, title, birth_date, notes))

        with open('north_data/orders_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                order_id, customer_id, employee_id, order_date, ship_city = row
                cur.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
                            (order_id, customer_id, employee_id, order_date, ship_city))

        cur.execute("SELECT * FROM customers, employees, orders")
        rows = cur.fetchall()
        for row in rows:
            print(row)

conn.close()