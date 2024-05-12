import secrets
import string

def generate_session_id(length: int = 64) -> string:
    alphabet = string.ascii_letters + string.digits
    session_id = ''.join(secrets.choice(alphabet) for _ in range(length))
    return session_id


if __name__ == "__main__":
    # Generate a secure session ID
    secure_session_id = generate_session_id()
    print(type(secure_session_id))
    print("Secure Session ID:", secure_session_id)