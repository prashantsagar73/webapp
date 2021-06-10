# Blog-app using django and react 

TL;DR: Django, DRF, DRF SimpleJWT with React Frontend with following features.
1. JWT authenitication
2. Admin pannel in both djago & React
3. User can ude CURD oprations through react admin pannel
4. socila login 


Test user: `sagar@gmail.com` and pw `sagar`.

---
### Introduction

This repository is an example of using React on the front end comminicating with Django thorigh api, Django Rest Framework and DRF SimpleJWT applications.

---
### Usage

#### Backend (Django) Instructions.


1. `cd ~/core` to get your terminal/cmd into the server directory.
2. To run the server, create a virtual environment `virtualenv venv && source source/bin/activate`, install packages `pip install -r requirements.txt` -- the requirements.txt file is inside the server subdirectory -- and do `python manage.py migrate && python manage.py runserver`.
    - Again, make sure when you do this, you are inside the server directory on your terminal/cmd.
    - On Windows, you should do `venv\Scripts\activate` instead of `source bin/activate`
3. If you're writing for an example repository, please create
a new directory labeled with the name of the framework (e.g. jwt-ios),
and add its `.gitignore`. Please use the
[github/gitignore](https://github.com/github/gitignore) repository.
Provide detailed instructions if necessary.

A default user with the username `sagar@gmail.com` and password `sagar` have been created.

or you can also create superuserthrough terminal/cmd
`python manage.py createsuperuser`


---

This repository does not come with throttling, but **it is
highly recommended that you add throttling to your entire
project.** You can use a third-party package called
Django-ratelimit or DRF's internal throttling mechanism.
Django-ratelimit is more extensive -- covering Django views,
as well -- and thus more supported by SimpleJWT.

#### Frontend (jwt-react) React instructions.

1. `cd ~/drf/react-drf` to get your terminal/server into the frontend (react) folder.

2. `npm install` to install all of the dependencies for the front end application.

3. `npm start` and you should be good to go, ensure that your backend is running on port `http://localhost:8000`, if you run it on another port/ip please change the `BASE_URL` in `auth.js`

4. Use `npm test` if you'd like to run the test which tests the api/ folder currently.

## Thankyou
