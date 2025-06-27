import mysql.connector
try:
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "AkpaEunice22."
)

    cursor=db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    db.commit()

    cursor.close()
    db.close()
    print("Database 'alx_book_store' created succesfully!")

except mysql.connector.Error as err:
    print(f"Error:{err}")

