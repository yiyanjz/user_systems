# Design Document

## System Architecture

The system is built using Django, a Python web framework. It follows the Model-View-Template (MVT) architectural pattern. 
The system consists of two main apps: `users` and `api`.

[Client (Web Browser/Mobile App)] <--> [Load Balancer (Optional)] <--> [Web Server (Gunicorn/uWSGI)] <--> [Django Application]
                                                                                                    |
                                                                                                    v
                                                                                             [Database (PostgreSQL)]
                                                                                                    |
                                                                                                    v
                                                                                             [Cache (Redis/Memcached) - Optional]
                                                                                                    |
                                                                                                    v
                                                                                             [File Storage (Cloud Storage/Local)]
                                                                                                    |
                                                                                                    v
                                                                                             [Email Service (SMTP/SendGrid/etc.)]
                                                                                                    |
                                                                                                    v
                                                                                             [REST API (Django REST Framework)]


## Database Structure

The database uses PostgreSQL.

User
-------
id (PK)
username (Unique)
password

|
| 1:1
|
UserProfile
-----------
id (PK)
user_id (FK)
nickname
phone
dob
avatar
email
last_updated
date_created


* **UserProfile:** Stores user profile information (nickname, phone, dob, avatar).

## Key Technical Implementation Strategies

* **User Authentication:** Django's built-in authentication system is used, with password hashing.
* **API Design:** Django REST Framework is used to create a RESTful API.

## Security Policies

* **Password Storage:** Passwords are hashed using Django's password functions.
* **Input Validation:** Django forms are used for input validation to prevent common vulnerabilities.
* **HTTPS:** The application is deployed with HTTPS to ensure secure communication.

## Password Encryption Methods

Django's password function uses a strong hashing algorithm (PBKDF2) to encrypt passwords.

## JWT Configurations (If Applicable)
- csrf_token
