import psycopg2
import csv
import conf
hostname = conf.hostname
database = conf.database
username = conf.username
pwd = conf.pwd
port_id = conf.port_id

conn = None
cur = None
num = 4

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
    
    cur = conn.cursor()

    table = [
        """
        CREATE TABLE IF NOT EXISTS contacts(
            name VARCHAR(50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            phone_number VARCHAR(20) NOT NULL
        )
        """
    ]
    for statement in table:
        cur.execute(statement)
    conn.commit()
    pref = input('Please , type (1) if you want to use input format or type (2) if you wnat to open csv file:')
    if pref == '1':
        name = input("Enter the name:")
        surname = input("Enter the second name:")
        phone_number = input("Enter phone number:")
        '''Insert contacts'''
        cur.execute("INSERT INTO contacts (name,surname , phone_number) VALUES (%s , %s , %s)" , (name , surname , phone_number))
        conn.commit()
        # # update data
        # condition_value = input("Enter the phone number of the contact you want to update:")
    
        # cur.execute("""
        # UPDATE contacts
        # SET name = %s, surname = %s , phone_number = %s
        # WHERE phone_number = %s;
        # """ , (name, surname,   phone_number , condition_value))
        # conn.commit()
    
        # '''delete contact'''
        # delete_value = input("Surname of the contact to delete:")
        # cur.execute("DELETE FROM contacts WHERE surname = %s" , (delete_value,))
        # conn.commit()

        # '''querying data fetchone!!!!!'''
        # cur.execute("SELECT name,surname FROM contacts ORDER BY name")
        # row = cur.fetchone()
        # print(row)
        # '''querying data fetchall!!!!'''
        # cur.execute("SELECT name, phone_number FROM contacts ORDER BY name")
        # rows = cur.fetchall()
        # print("The number of parts: ", cur.rowcount)
        # for row in rows:
        #     print(row)
        # '''querying data fetchmany!!!'''
        # cur.execute("SELECT name , phone_number FROM contacts ORDER BY phone_number")
        # rows1 = cur.fetchmany(num)
        # for row in rows1:
        #     print(row)

    if pref == '2':
        with open('name.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader) 
            for row in reader:
                name , surname , phone_number = row
                cur.execute("INSERT INTO contacts (name, surname, phone_number) VALUES (%s, %s, %s)", row)
            conn.commit()
    
        
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()