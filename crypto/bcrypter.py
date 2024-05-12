import bcrypt


class bcrypter:
    def __init__(self) -> None:
        pass

    def crypt(self, password) -> str:

        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

if __name__ == "__main__":
    res = bcrypter().crypt("hello")
    print("Hashed Password:", res)
    print(len(res))
    print(type(res))