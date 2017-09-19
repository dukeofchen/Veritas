import mysql.connector

# Connect to TT-RSS DB
try:
    cnx = mysql.connector.connect(user='wewokettrss', password='trevecca', host='mysql.wewoke.world', database='ttrssdb37')
    print('Connection Successful')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

ttrss = cnx.cursor(buffered=True)

# Create table and/or copy entries from TTRSS to sandbox
ttrss.execute('''
    UPDATE Entries
    SET categorized = 0, categories = NULL''')

cnx.commit()

ttrss.close()
