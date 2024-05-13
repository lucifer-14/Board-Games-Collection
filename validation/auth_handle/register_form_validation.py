import re
import sql_handle.sql_connector as SQLC

class Register_Form_Validation:
    def __init__(self, username: str, email: str, password: str, re_password: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.re_password = re_password

    
    def username_rules(self) -> tuple:
        pattern = r'^[a-zA-Z0-9_]+$'

        if not self.username:
            return (False, "Username shouldn't be blank.")

        if not re.match(pattern, self.username):
            return (False, "Username shouldn't contain special characters.")
        
        return (True, "")

    
    def email_rules(self) -> tuple:

        if not self.email:
            return (False, "Email shouldn't be blank.")
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(pattern, self.email):
            return (False, "Please enter a valid email address.")

        return (True, "")
        
        
    def validate_username(self) -> tuple:

        rules_res = self.username_rules()
        print(self.username, rules_res)

        if not rules_res[0]:
            return rules_res

        sql_connection = SQLC.SQL_Connector()

        query = "SELECT * FROM users WHERE username = %s"
        search = (self.username,)

        res = sql_connection.fetchone_query(query, search)

        if res:
            return (False, "Username already exists!")
        
        return (True, "")


    def validate_email(self) -> tuple:

        rules_res = self.email_rules()

        if not rules_res[0]:
            return rules_res

        sql_connection = SQLC.SQL_Connector()
        
        query = "SELECT * FROM users WHERE email = %s"
        search = (self.email,)
        
        res = sql_connection.fetchone_query(query, search)

        if res:
            return (False, "Email already exists!")
        
        return (True, "")


    def validate_password(self) -> tuple:
        # Minimum length requirement
        if not self.password:
            return (False, "Password shouldn't be blank.")
        
        if not self.re_password:
            return(False, "Re-type password shouldn't be blank.")
        
        if self.password != self.re_password:
            return(False, "Passwords must be the same.")
        

        if len(self.password) < 6:
            return (False, "Password must have at least 6 characters.")
        

        # # Complexity requirement (mix of uppercase, lowercase, numbers, and special characters)
        # if not re.search(r'[A-Z]', self.password) or \
        # not re.search(r'[a-z]', self.password) or \
        # not re.search(r'\d', self.password) or \
        # not re.search(r'[@#$%^&+=]', self.password):
        #     return (False, "Password must have mixture of uppercase, lowercase, numbers and special characters.")

        
        # # No common or easily guessable patterns
        # common_patterns = ['password', '123456', 'qwerty', 'abc123']
        # if any(pattern in self.password.lower() for pattern in common_patterns):
        #     return (False, "Password is too common")
        
        
        # # No repeated characters or sequential patterns
        # if re.search(r'(.)\1{2}', password) or \
        # any(ord(password[i]) == ord(password[i+1])-1 == ord(password[i+2])-2 for i in range(len(password)-2)):
        #     return False
        

        # Passed all checks, password is valid
        return (True, "")


    def validate(self) -> tuple:

        res, comment = self.validate_username()
        if not res:
            return (res, comment)
        
        res, comment = self.validate_email()
        if not res:
            return (res, comment)
        
        res, comment = self.validate_password()
        if not res:
            return (res, comment)
        
        return (True, "Validation Success!")
        
        