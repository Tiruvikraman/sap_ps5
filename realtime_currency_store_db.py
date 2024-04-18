import psycopg2
from psycopg2 import sql
from bs4 import BeautifulSoup
import requests

def create_connection():
    try:
        connection = psycopg2.connect(
            dbname="sap_ps5",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        
        drop_table_sql = """
        DROP TABLE IF EXISTS currency_table
        """
        cursor.execute(drop_table_sql)
        connection.commit()
        
        create_table_sql = """
        CREATE TABLE currency_table (
            no int,
            currency TEXT,
            name TEXT,
            symbol TEXT,
            value TEXT,
            inr TEXT
            );
                """
        cursor.execute(create_table_sql)
        connection.commit()
        
        return connection
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)
        return None

def insert_currency_data(connection,i, currency, army, value):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO currency_table (no,name, inr, value) VALUES (%s,%s, %s, %s)"
        cursor.execute(sql, (i,currency, army, value))
        connection.commit()
        
    except psycopg2.Error as e:
        print("Error inserting data:", e)

def format_table():
      
    # Establish connection
    connection = psycopg2.connect(
        dbname="sap_ps5",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()
    
    sql = '''DELETE FROM currency_table
    WHERE no IN (
        1, 3, 4, 5, 6, 7, 9, 11, 12, 13, 15, 16, 17, 19, 20, 22,
        23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        41, 42, 43, 44, 45, 47, 48, 49, 52
    );
    ALTER TABLE currency_table DROP COLUMN no;
    UPDATE currency_table SET currency = 'AUD' WHERE name = 'Australian Dollar';
    UPDATE currency_table SET currency = 'CAD' WHERE name = 'Canadian Dollar';
    UPDATE currency_table SET currency = 'CNY' WHERE name = 'Chinese Yuan Renminbi';
    UPDATE currency_table SET currency = 'EUR' WHERE name = 'Euro';
    UPDATE currency_table SET currency = 'IDR' WHERE name = 'Indonesian Rupiah';
    UPDATE currency_table SET currency = 'JPY' WHERE name = 'Japanese Yen';
    UPDATE currency_table SET currency = 'SGD' WHERE name = 'Singapore Dollar';
    UPDATE currency_table SET currency = 'THB' WHERE name = 'Thai Baht';
    UPDATE currency_table SET currency = 'GBP' WHERE name = 'British Pound';
    UPDATE currency_table SET currency = 'USD' WHERE name = 'US Dollar';
    UPDATE currency_table SET symbol = '$' WHERE name = 'Australian Dollar';
    UPDATE currency_table SET symbol = '$' WHERE name = 'Canadian Dollar';
    UPDATE currency_table SET symbol = '¥' WHERE name = 'Chinese Yuan Renminbi';
    UPDATE currency_table SET symbol = '€' WHERE name = 'Euro';
    UPDATE currency_table SET symbol = 'Rp' WHERE name = 'Indonesian Rupiah';
    UPDATE currency_table SET symbol = '¥' WHERE name = 'Japanese Yen';
    UPDATE currency_table SET symbol = '$' WHERE name = 'Singapore Dollar';
    UPDATE currency_table SET symbol = '฿' WHERE name = 'Thai Baht';
    UPDATE currency_table SET symbol = '£' WHERE name = 'British Pound';
    UPDATE currency_table SET symbol = '$' WHERE name = 'US Dollar';
    '''
    
    cursor.execute(sql)
    
    connection.commit()
    
    cursor.close()
    connection.close()
    return 0

def main():
    connection = create_connection()
    if connection is None:
        return
    
    response = requests.get('https://www.x-rates.com/table/?from=INR&amount=1')
    soup = BeautifulSoup(response.text, 'html.parser')
    currency_table = soup.find('table', class_='tablesorter ratesTable').find('tbody')
    currency_rows = currency_table.find_all('tr')
    i=1
    for currency_row in currency_rows:
        columns = currency_row.find_all('td')
        currency = columns[0].get_text()
        inr = columns[1].get_text()
        value = columns[2].get_text()
        
        insert_currency_data(connection,i, currency, inr, value)
        i+=1
    print('Data inserted successfully')
    connection.close()
  format_table()

if __name__ == "__main__":
    main()
