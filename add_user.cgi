# add_user.cgi

import cgi
import sqlite3

# Create a connection object to the textbook database
db = sqlite3.connect('TextbookSalesDatabase.db')
    
def main():
    
    # Retrieve the fields from the form field storage
    fields = cgi.FieldStorage()
    
    # Get the values from the fields and assign them to a local variable
    name = fields.getvalue('name')
    surname = fields.getvalue('surname')
    username = fields.getvalue('username')
    password = fields.getvalue('password')
    
    # Start to compose the webpage to be displayed
    print('Content-type: text/html\n\n')
    print('<html><head><title>User Sign Up</title></head><body><br><br><div style="text-align:center">')
    
    try:
        # In the event of an error/exception with writing to the database, the transation rolls back otherwise it is committed and database is closed
        with db:
            db.execute('insert into User values (?,?,?,?)', (name, surname, username, password))
        print('<h>Account successfully added.</h><p><a href="login-page.html">Return to Login page</a></p>')
        
    # If an entry with this primary key already exists, then display the following
    except sqlite3.IntegrityError:
        print('<h>This account with this username already exists.<br>Login or sign up with a different username.</h><p><a href="login-page.html">Return to Login page</a></p>')
        
    # If any other error occurs, then display the following
    except:
        print('<h>An error occurred.<br>Account not added.</h><p><a href="login-page.html">Return to Login page</a></p>')
    print('</div></body></html>')
    
main()