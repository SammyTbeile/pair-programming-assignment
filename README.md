# pair-programming-assignment

Practice with Development Technologies: Homework 2

Natalia Jacobowitz nbj2105
Sammy Tbeile st2918

Team S.S. ASE

https://github.com/SammyTbeile/pair-programming-assignment

We used Python and Flask to create a webapp to introduce the pair of students working on the assignment.

The project:
The WebApp has multiple screens. The first screen is the directory of the two students titled "The Best Programming Duo”. Each is linked to the students’ personal page. This is formatted with HTML and has a link to the student's LinkedIn. The index screen also has login and register buttons. We added this feature to test our ability to create it and practice making a database. From the login and register pages you can use the “back button” to go back to the home page/ 1st screen. The login page will redirect as well.
We kept the project fairly simple thus it’s only a few pages and has a basic login/ register function (that admittedly doesn’t do anything).

Modules:
We used the flask module “flask_login” to aid in the login capability. We use MongoDB for our database. This saves the login information.

How we learned:
ADI created a tutorial on flask which we used to learn the framework. ( http://learn.devfe.st/webdev/ ). We felt that it was simple enough to use and we foresee the project to run smoothly while using flask.

Challenges:
The biggest challenge we ran into was figuring out all the dependencies for the different modules. A gotcha that we ran into was when developing the login feature, we didn’t originally realize that we needed to be running mongod (or pointing to a db in that directory).

Pylint for static analysis:
Running Pylint returned a few errors. The errors were because of flask keywords like “app” which are unavoidable with flask. For the team project we will need to set up a config file to ignore these errors or we will try to find another static analysis tester with more flask support.

Test cases:
Click on link for sammy (notice URL path change), go back, click on link for natalia (again notice URL path change), go back to the home page, try registering, and then try logging in. All should work as expected.

Dependencies:
flask
Requests
flask_mongoengine
flask_login
wtforms

How to run:
Run mongo with mongod --dbpath <path to project directory>
Run our app (and install dependencies) with fab build
Run just our app with fab serve
Run our tests with fab test
