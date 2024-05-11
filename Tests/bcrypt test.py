import bcrypt

# Hash a password
password = "room2"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print("Hashed Password:", hashed_password.decode('utf-8'))
print(len(hashed_password.decode('utf-8')))