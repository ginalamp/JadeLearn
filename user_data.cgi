# Collects user data and outputs it to a user.txt file
# user_data.cgi

import cgi
import sqlite3
import cgitb

def main():
    
    # Retrieve the fields from the form field storage
    fields = cgi.FieldStorage()
    
    # Get the values from the fields and assign them to a local variable
    name = fields.getvalue('name')
    surname = fields.getvalue('surname')
    age = fields.getvalue('age')
    sex = fields.getvalue('sex')
    race = fields.getvalue('race')
    prov = fields.getvalue('province')
    grade = fields.getvalue('grade')
    email = fields.getvalue('email')
    password = fields.getvalue('psw')
    
    sub1 = fields.getvalue('sub1')
    sub2 = fields.getvalue('sub2')
    sub3 = fields.getvalue('sub3')
    mark1 = fields.getvalue('mark1')
    mark2 = fields.getvalue('mark2')
    mark3 = fields.getvalue('mark3')
    gmark1 = fields.getvalue('gmark1')
    gmark2 = fields.getvalue('gmark2')
    gmark3 = fields.getvalue('gmark3')

    #Get interests checkbox values and assign to local variables
    sport_flag = code_flag = game_flag = cook_flag = "OFF"

    if form.getvalue('sport'):
        sport_flag = "ON"
    else:
        sport_flag = "OFF"
    if form.getvalue('code'):
        code_flag = "ON"
    else:
        code_flag = "OFF"
    if form.getvalue('game'):
        game_flag = "ON"
    else:
        game_flag = "OFF"
    if form.getvalue('cook'):
        cook_flag = "ON"
    else:
        cook_flag = "OFF"
    # Start to compose the webpage to be displayed
    print('Content-type: text/html\n\n')
    print('<html><head><title>User Sign Up</title></head><body><br><br><div style="text-align:center">')
    #Add data to user.txt file
    file = open("user.txt", "w")
    file.write(name +'\n')
    file.write(surname +'\n')
    file.write(age +'\n')
    file.write(sex +'\n')
    file.write(race +'\n')
    file.write(prov +'\n')
    file.write(grade +'\n')
    file.write(email +'\n')
    file.write(password +'\n')
    #user marks as well as  interests in one line seperated by comma space
    file.write(sub1 + '.' + mark1 + '.' gmark1 +', ')
    file.write(sub2 + '.' + mark2 + '.' gmark2 +', ')
    file.write(sub3 + '.' + mark3 + '.' gmark3 +'\n')

    file.write(sport_flag +', ')
    file.write(code_flag +', ')
    file.write(game_flag +', ')
    file.write(cook_flag +', ')

    print('<h>Welcome! Your account has been successfully added.</h><p><a href="Courses.html">Go to Courses page</a></p>')
        
    print('</div></body></html>')
    
main()
