import hashlib

# User database (example)
users = {
    'john': {
        'password': hashlib.sha256('password123'.encode()).hexdigest(),
        'roles': ['user'],
    },
    'admin': {
        'password': hashlib.sha256('admin123'.encode()).hexdigest(),
        'roles': ['user', 'admin'],
    }
}

# Function to authenticate user
def authenticate(username, password):
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == users[username]['password']:
            return True
    return False

# Function to authorize user roles
def authorize(username, role):
    if username in users and role in users[username]['roles']:
        return True
    return False

# Example usage
username = input("Enter your username: ")
password = input("Enter your password: ")

if authenticate(username, password):
    print("Authentication successful!")
    required_role = input("Enter the role you want to access: ")
    if authorize(username, required_role):
        print("Authorization granted!")
        # Perform authorized actions here
    else:
        print("You don't have the required authorization.")
else:
    print("Authentication failed!")
