import bcrypt

# Retrieve hashed_password from the database based on username/email
stored_hashed_password = "$2b$12$i6y5BO4.gune5GWMpU4yEeY9dT/p0D9.fMul.pZHEgXRSsFVXH482" # Retrieve from database

# User provides a password during login
provided_password = "dummy4"

# Verify the password
if bcrypt.checkpw(provided_password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
    print("Password is correct!")
else:
    print("Password is incorrect!")