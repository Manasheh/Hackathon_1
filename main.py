import psycopg2
import config

print('1 to find volunteer')
print('2 to find organisatoin')


try:
    conn = psycopg2.connect(
        dbname=config.DATABASE,
        user=config.USERNAME,
        password=config.PASSWORD,
        host=config.HOSTNAME,
        port=config.PORT
    )
    # print("Successfully connected to the database!")

    cursor = conn.cursor()
    # cursor.execute('SELECT * FROM region')
    query = '''
INSERT INTO region(region_name) VALUES ('Tel-aviv')
'''
#     query = '''
#         DELETE FROM region WHERE region_id > 2
# '''
    cursor.execute(query)
    conn.commit()
    select_query = 'SELECT * FROM region'
    cursor.execute(select_query)
    # all_rows = cursor.fetchall()
    # for row in all_rows:
    #     print(row)  
    # cursor.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

finally:
    if conn:
        conn.close()
