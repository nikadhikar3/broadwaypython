import sqlite3

# git config --global user.name "Nikhil Adhikari"
# git config --global user.email "nikadhikari3@gmail.com"
# create account on github
# create new repository in github
# git init
# git add .
# git commit -m "Your message"
# copy paste from git hub repository that you created 
# git remote add origin https://github.com/nikadhikar3/broadwaypython.git
# git branch -M main
# git push -u Origin main

# The function attempts to create a connection to a 
# SQLite database file named "user.sqlite3"

def create_connection():
    try:
        con = sqlite3.connect("user.sqlite3")
        return con
    except Exception as e:
        print("Error : " , e)  
        
        
# The `INSERT_STRINGS` variable is storing a multi-line string that 
# contains a menu of options for a user interface. 
INSERT_STRINGS = """
Enter the option:
    1. Create Table
    2. Read Csv File
    3. Dump users From csv Into users TABLE
    4. ADD new user INTO users TABLE
    5. QUERY all users from TABLE
    6. QUERY user by id from TABLE
    7. QUERY specified no. of records from TABLE
    8. DELETE all users
    9. DELETE user by id from TABLE
    10. UPDATE user 
    11. Press any key to Exit
    
    Enter your Choice :
"""

#changes



# The function `create_table` creates a table named `users` with 
# specific columns in a database connection.

def create_table(conn):
    
    CREATE_users_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      first_name CHAR(255) NOT NULL,
      last_name CHAR(255) NOT NULL,
      company_name CHAR(255) NOT NULL,
      address CHAR(255) NOT NULL,
      city CHAR(255) NOT NULL,
      county CHAR(255) NOT NULL,
      state CHAR(255) NOT NULL,
      zip REAL NOT NULL,
      phone1 CHAR(255) NOT NULL,
      phone2 CHAR(255) NOT NULL,
      email CHAR(255) NOT NULL,
      web text
    );
    """
    
    cur = conn.cursor()
    cur.execute(CREATE_users_TABLE_QUERY)
    print("User Table was created successfully.")



# Reads data from a CSV file named 'sample_users.csv' 
# and returns a list of tuples. The function opens the CSV file, 
# reads its contents, and stores the data in a list of tuples.
# It then prints the list of 
# users and the total number of rows (excluding the header).   
# Returns:
#     list[tuple]: A list of tuples containing the user data.

   
import csv
def read_csv():
    users = []
    with open("sample_users.csv","r") as f:
        data = csv.reader(f)
        for user in data:
            users.append(tuple(user))
    print(users)
    print(f"Total number of rows : {len(users[1:])}")
    return users[1:]
    

def insert_users(conn, users):
    user_add_query = """
    INSERT INTO users(
        first_name,
        last_name,
        company_name,
        address,
        city,
        county,
        state,
        zip,
        phone1,
        phone2,
        email,
        web
    )
    VALUES
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cur = conn.cursor()
    cur.executemany(user_add_query, users)
    conn.commit()
    print(f"{len(users)} Users were imported sucessfully. ")  
    

# Reads all the rows 
# from the 'users' table in the given database connection.  
# Args:
#     con (sqlite3.Connection): The database connection object.  
# Returns:
#     None      
# Prints:
#     - The details of each user in the 'users' table.
#     - The total number of users in the 'users' table.
def read_user_table(con):
    cur = con.cursor()
    cur.execute("Select * from users")
    users_list = cur.fetchall() 
    for user in users_list:
        print(user)
    print(f"Total number of users : {len(users_list)}")   
    


# Retrieves a user from the database by their ID.
# Args:
#     con (sqlite3.Connection): The database connection object.
#     user_id (int): The ID of the user to be retrieved.
# Returns:
#     None
# Prints:
#     - The details of the user with the specified ID.
   
def select_user_by_id(con, user_id):
    cur = con.cursor()
    query = "Select * from users where id = ?"
    user_by_id = cur.execute(query,(user_id,))
    for id_content in user_by_id:
        print(id_content)
    
       

#The main function is the entry 
# point of the program. It establishes a connection to the database, 
#prompts the user for input  

def main():
    con = create_connection()
    user_input = input(INSERT_STRINGS)
    if user_input == '1':
        create_table(con)
    elif user_input == '2':
        read_csv()
    elif user_input == '3':
        users = read_csv()
        insert_users(con, users)
    elif user_input == '4':
        pass
    elif user_input == '5':
        read_user_table(con)
    elif user_input == '6':
        input_id = input("Enter user id: ")
        select_user_by_id(con, input_id)
    elif user_input == '7':
        pass
    elif user_input == '8':
        pass
    elif user_input == '9':
        pass
    elif user_input == '10':
        pass
    else:
        print("Invalid input")

    
    
main()