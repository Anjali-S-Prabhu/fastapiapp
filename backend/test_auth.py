import requests
import json

BASE_URL = "http://localhost:8000"

# Test 1: Register a user
print("=" * 50)
print("TEST 1: Register User")
print("=" * 50)

register_data = {
    "name": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "role": "Candidate"
}

response = requests.post(
    f"{BASE_URL}/auth/register",
    json=register_data,
    headers={"Content-Type": "application/json"}
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

# Test 2: Login with correct credentials
print("\n" + "=" * 50)
print("TEST 2: Login with Correct Credentials")
print("=" * 50)

login_data = {
    "email": "test@example.com",
    "password": "testpass123"
}

response = requests.post(
    f"{BASE_URL}/auth/login",
    json=login_data,
    headers={"Content-Type": "application/json"}
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

# Test 3: Login with wrong password
print("\n" + "=" * 50)
print("TEST 3: Login with Wrong Password")
print("=" * 50)

login_data = {
    "email": "test@example.com",
    "password": "wrongpassword"
}

response = requests.post(
    f"{BASE_URL}/auth/login",
    json=login_data,
    headers={"Content-Type": "application/json"}
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

# Test 4: Malformed request (missing password)
print("\n" + "=" * 50)
print("TEST 4: Malformed Request (Missing Password)")
print("=" * 50)

login_data = {
    "email": "test@example.com"
}

response = requests.post(
    f"{BASE_URL}/auth/login",
    json=login_data,
    headers={"Content-Type": "application/json"}
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
