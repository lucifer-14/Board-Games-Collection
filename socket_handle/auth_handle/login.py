"""
return true if login success, else, false
"""

import socket_handle.send_request as S_REQ
import crypto_custom.bcrypt.bcrypt_verifier as b_verifier

class Login():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.data = {"username": self.username, "password": self.password}
        

    def login(self):
        """ Client side login
        """
        SR = S_REQ.Send_Request()
        response = SR.send_req("POST", "/login", self.data)
        response_code = response['response-code']
        response_comment = response['response-comment']
        response_data = response['data']

        return response_data
    

    def login_verify(self, true_password):
        """ Server side login verification
        """
        bcrypt_verifier = b_verifier.Bcrypt_Verifier()
        verify_res = bcrypt_verifier.verify(true_password, self.password)
        
        return verify_res

