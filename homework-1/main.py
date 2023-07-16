"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from csv import DictReader

PATH = ['north_data/customers_data.csv', 'north_data/employees_data.csv', 'north_data/orders_data.csv']


def main():
    try:
        with psycopg2.connect(host='localhost', database='north', user='postgres', password='12345') as conn:
            with conn.cursor() as cur:
                for path in PATH:
                    for dict_ in DictReader(open(path, encoding='cp1251')):
                        if path == 'north_data/customers_data.csv':
                            dict_['company_name'] = dict_['company_name'].replace("'", '"')
                            cur.execute(f"INSERT INTO customers VALUES(\'{dict_['customer_id']}\', "
                                        f"\'{dict_['company_name']}\', \'{dict_['contact_name']}\');")
                        if path == 'north_data/employees_data.csv':
                            cur.execute(f"INSERT INTO employees VALUES(\'{dict_['employee_id']}\', "
                                        f"\'{dict_['first_name']}\', \'{dict_['last_name']}\',"
                                        f"\'{dict_['title']}\',\'{dict_['birth_date']}\',"
                                        f"\'{dict_['notes']}\');")
                        if path == 'north_data/orders_data.csv':
                            cur.execute(f"INSERT INTO orders VALUES(\'{dict_['order_id']}\', "
                                        f"\'{dict_['customer_id']}\', \'{dict_['employee_id']}\',"
                                        f"\'{dict_['order_date']}\',\'{dict_['ship_city']}\');")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
