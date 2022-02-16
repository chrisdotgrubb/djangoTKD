# djangoTKD

Download this project

1. Click green "Code" button
2. Download zip
3. extract zip somewhere, probably with your other projects

To set up django

1. go to the terminal in your project
2. create python virtual env
3. pip install -r requirements.txt

Then set up the django server to run, in same terminal, copy these commands

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver

Server should be running, go to http://localhost:8000/

If that all works, you should be able to view the website like a user would. You can sign up and login to use most of
the features. But you can do a few more things to test out the rest.

- Make an admin

1. python manage.py createsuperuser
2. http://localhost:8000/admin/

- Add some users

1. You can add user, their profiles, courses, and user messages manually in the admin. To have a profile, you need to
   first have a user to link it to. To have a message between users, you first need a message thread, and a sender a
   receiver. Messaging is easier to understand using the user-profile site, rather than in the admin.
2. Or if you to do it faster, you can open the file "scripts_for_shell.py" and copy and paste the lines into the shell.
   Don't just copy the whole file in there. Do it in pieces. Imports need to be done one line at a time, then each of
   the variables by themselves, then the function. Then call the function as many times as you want. You can copy/paste
   the whole last section that adds courses together.
3. python manage.py shell
4. create_user(50)
5. You can also show which instructors teach a certain class(only using the admin for now). But your choice is limited
   to only users who are instructors. You can use the admin, user profiles, is_instructor to make someone an instructor,
   so they show up in the choices.
6. You can mess with the templates to change what information is displayed. The courses, users, inbox, messages...
   aren't really displayed in pretty ways. They are just showing what information is there. With some 'if' and 'for'
   logic in the templates and a bit of styling, it could actually look nice.

Let me know if you have any questions. If something doesn't make sense, there is probably an easy explanation, just ask
me, as I may have made a typo or forgot a step.
  
  
