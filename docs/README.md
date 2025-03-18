# User Authentication & Authorization

## Project Description
[A startup company needs to build a user system supporting common functionalities like "registration and login." To enhance security and scalability, the company aims to ensure good engineering practices at the code level and validate critical logic through comprehensive unit testing.]

## Technology Stack
* Python3: 3.13.2
* Django: 5.1.7
* Database: Postgress 
# Why I choose Postgress (SQL DB)
    - SQL databases are ideal for applications requiring data integrity, structured queries, and transactional consistency. They enforce ACID compliance, making them reliable for banking, e-commerce, and secure data management. With powerful querying capabilities and robust security features, SQL databases ensure long-term stability and easier compliance with regulations like GDPR and HIPAA. While NoSQL is better for scalable, flexible, and real-time applications, SQL remains the preferred choice for structured, relational, and transaction-heavy systems.

## Setup and Installation
1.  Clone the repository:
    git clone [repository URL]
    cd [project directory]

2.  Create and activate a virtual environment:
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate      # On Windows

3.  Install dependencies:
    pip install -r requirements.txt

4.  Create database migrations:
    python3 manage.py makemigrations
    python3 manage.py migrate

5.  Create a superuser (if needed):
    python3 manage.py createsuperuser

## Running the Development Server
python3 manage.py runserver


# Running Tests
python3 manage.py test core


# Conclusion
This is a general design, if this was production I would focus alot more on minor details keeping the UI user-friendly and easy to interact with.

# Demo Video Link
[https://drive.google.com/file/d/18WrDxzuL5xmlOIbVFDAN4xoeEBqGiaEZ/view?usp=share_link](https://drive.google.com/file/d/18WrDxzuL5xmlOIbVFDAN4xoeEBqGiaEZ/view?usp=share_link)
