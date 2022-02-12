# djangoTKD

Download this project
1. Click green "Code" button
2. Download zip
3. extract zip somewhere, probably with your other projects


To set up django
4. go to the terminal in your project
5. create python virtual env
6. pip install -r requirements.txt
  
Then set up the django server to run, in same terminal, copy these commands
7. python manage.py makemigrations
8. python manage.py migrate
9. python manage.py runserver
 
Server should be running, go to http://localhost:8000/
 
If that all works, you can do a couple more things to test it
make an admin
1. python manage.py createsuperuser
2. http://localhost:8000/admin/
  
add some users
3. you can add user, their profiles, and courses manually in the admin
4. or if you to do it faster, you can open the file "scripts_for_shell.py" and copy and paste the lines into the shell
dont jst copy the whole file in there. do it in pieces. imports need to be done one line at a time, then each of the variables, and functions by themselves
    
    
let me know if you have any questions. if something doesn't make sense, there is probably an easy explanation, just ask me, as I may have made a typo or forgot some point
  
  
