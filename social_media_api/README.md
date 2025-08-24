Social Media API – User Authentication

This is the initial setup of the Social Media API project. It includes:

Django + Django REST Framework setup

Custom user model (CustomUser) with bio, profile_picture, and followers

Token-based authentication

Endpoints for registration, login, and profile management

Setup Instructions

1. Clone the repo & install dependencies
git clone https://github.com/Mafuyeka/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
pip install django djangorestframework djangorestframework-simplejwt
pip install djangorestframework-authtoken

2. Run migrations
python manage.py makemigrations
python manage.py migrate

3. Create a superuser (optional, for admin access)
python manage.py createsuperuser

4. Start the development server
python manage.py runserver

Authentication Endpoints

All authentication is token-based.
Every time a user registers or logs in, they will receive an auth token.
This token must be included in request headers for protected endpoints:

Authorization: Token <your_token_here>

1. Register a New User

POST /api/accounts/register/

Example (cURL)
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"tshepiso","email":"tshepiso@example.com","password":"pass1234"}'

Response
{
  "user": {
    "id": 1,
    "username": "tshepiso",
    "email": "tshepiso@example.com"
  },
  "token": "9f71c33c3cbb4e5598a1e30b98f31b50"
}

2. Login a User

POST /api/accounts/login/

Example (cURL)
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"tshepiso","password":"pass1234"}'

Response
{
  "token": "9f71c33c3cbb4e5598a1e30b98f31b50",
  "user_id": 1,
  "username": "tshepiso"
}

3. View or Update Profile

GET/PUT /api/accounts/profile/ (auth required)

Example (GET Profile)
curl -X GET http://127.0.0.1:8000/api/accounts/profile/ \
  -H "Authorization: Token 9f71c33c3cbb4e5598a1e30b98f31b50"

Response
{
  "id": 1,
  "username": "tshepiso",
  "email": "tshepiso@example.com",
  "bio": null,
  "profile_picture": null,
  "followers": []
}

Example (Update Profile)
curl -X PUT http://127.0.0.1:8000/api/accounts/profile/ \
  -H "Authorization: Token 9f71c33c3cbb4e5598a1e30b98f31b50" \
  -H "Content-Type: application/json" \
  -d '{"bio": "I love coding and cooking!"}'

Response
{
  "id": 1,
  "username": "tshepiso",
  "email": "tshepiso@example.com",
  "bio": "I love coding and cooking!",
  "profile_picture": null,
  "followers": []
}

