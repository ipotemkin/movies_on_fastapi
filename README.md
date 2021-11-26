Movies storage API on Flask
=======

Usage
------

Look at the SWAGGER welcome page

Authorization rules:
-----
Without authorization, you can see:
1. All users – just for a test
2. Add a new user

For other endpoints you need an authorization either as a user or an amdin.

Endpoints only available for admins:
1. ALL PATCH and DELETE commands
2. POST for /movies/<mid>
3. POST for /directors/<did>
4. POST for /genres/<gid>

After authorization, you get two tokens:
- access token valid during 5 minutes and
- refresh token valid during 1 day

You can use your refresh token only once to get a new pair of tokens

Test users:
-------
1. name: 'vasya', password: 'my_little_pony', role: 'user'
2. name: 'oleg', password: 'SkySmart', role: 'user'
3. name: 'oleg2', password: 'SkyPro', role: 'admin'

Dependencies
-------

1. Flask
2. Flask-SQLAlchemy
3. Flask-RESTX
4. PyDantic
5. Flask-PyDantic
6. PyJWT