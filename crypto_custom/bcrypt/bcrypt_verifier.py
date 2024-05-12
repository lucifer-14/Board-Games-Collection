import bcrypt


class Bcrypt_Verifier:
    def __init__(self) -> None:
        pass

    def verify(self, stored: str, provided: str) -> bool:
        if bcrypt.checkpw(provided.encode('utf-8'), stored.encode('utf-8')):
            return True
        else:
            return False



if __name__ == "__main__":
    # Retrieve hashed_password from the database based on username/email
    stored_hashed_password = "$2b$12$TyrcyTzDCnXZeXOnctZWZe6yOyCPcda3rWpdiWH4BpZzytDNbEji2" # Retrieve from database

    # User provides a password during login
    provided_password = "hello"

    res = Bcrypt_Verifier().verify(stored_hashed_password, provided_password)
    if res:
        print("cor")
    else:
        print("incor")