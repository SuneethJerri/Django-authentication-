# Django Authentication System

Welcome to the Django Authentication System! This project provides a robust authentication system for web applications built using Django. By following these simple steps, you can run the application locally on your machine.

## Getting Started

### Clone the repository:
```bash
git clone https://github.com/SuneethJerri/Django-authentication-.git
```
- Install django:
```python
pip install django
```
- In terminal run the script:
```python
python manage.py runserver
```
The website consists of:
- home page
- login/signup pages
- profile page
- change username/password pages

## Email Verification

Email verification is a crucial security measure implemented in this system to enhance account creation and password-changing processes. Here's how it works:

- **Account Creation**: Users receive a randomly generated 4-6 digit code via email. This code must be entered during account creation to validate the provided email address.

- **Password Change**: For added security during password changes, users can receive a unique link or a random OTP via email. This authentication step ensures that only the account owner can initiate password changes.

By incorporating email verification, we ensure data integrity and enhance user safety.

