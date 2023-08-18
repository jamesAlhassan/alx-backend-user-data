#!/usr/bin/env python3
""" End-to-end integration test"""

import requests

BASE_URL = 'http://localhost:5000'
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """ Test for validating user registration """
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(f'{BASE_URL}/users', data=data)

    msg = {"email": email, "message": "user created"}

    assert response.status_code == 200
    assert response.json() == msg

def log_in_wrong_password(email: str, password: str) -> None:
    """ Test for validating log in with wrong password """
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(f'{BASE_URL}/sessions', data=data)

    assert response.status_code == 401

def log_in(email: str, password: str) -> str:
    """ Test for validating succesful log in """
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(f'{BASE_URL}/sessions', data=data)

    msg = {"email": email, "message": "logged in"}

    assert response.status_code == 200
    assert response.json() == msg

    session_id = response.cookies.get("session_id")

    return session_id
