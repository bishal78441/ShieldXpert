import mysql.connector

# Replace the placeholder values with your actual database credentials
host = 'localhost'
user = 'root'
password = ''
database = 'antivirus'

try:
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if conn.is_connected():
        print(f"Connected to MySQL database '{database}'")

        # Create a cursor to execute SQL statements
        cursor = conn.cursor()

        # Your code for database operations goes here
        user_name = 'hi'
        feedback_subject = 'hello'
        feedback_text = 'huhu'

        # Use placeholders in the SQL statement
        sql_insert = '''
            INSERT INTO feedbackk (Name, Subject, Feedback)
            VALUES (%s, %s, %s)
        '''
        # Execute the SQL statement with actual values
        cursor.execute(sql_insert, (user_name, feedback_subject, feedback_text))

        # Commit the changes
        conn.commit()

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # Close the database connection when done
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection closed")
