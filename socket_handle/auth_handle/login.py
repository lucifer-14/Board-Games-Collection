"""
return true if login success, else, false
"""

import socket_handle.send_request as S_REQ
import crypto_custom.bcrypt.bcrypt_verifier as b_verifier
import sql_handle.sql_connector as SQLC
import socket_handle.auth_handle.generate_session_id as SAGSI
import utils.config_handler as CONF_H

class Login():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.data = {"username": self.username, "password": self.password}
        

    def login_request(self) -> dict:
        """ Client side login request, sends request then receives response
        """
        SR = S_REQ.Send_Request()
        response = SR.send_req("POST", "/login", self.data)
        response_code = response['response-code']
        response_comment = response['response-comment']
        response_data = response['data']

        if response_data['is_login_success']:
            conf_h = CONF_H.Config_Handler()
            conf_h.set_config("CURRENT_SESSION", response_data['session_id'])
            conf_h.set_config("CURRENT_USERNAME", response_data['username'])
            conf_h.set_config("CURRENT_USER_ID", response_data['user_id'])
            pass

        return response_data
    

    def login_response(self) -> dict:
        """ Server side login response, generates response
        """

        response_code = 200
        response_comment = "Success"
        
        sql_connection = SQLC.SQL_Connector()
        query = "SELECT * FROM users WHERE username= %s"
        search = (self.username,)

        res = sql_connection.fetchone_query(query, search)

        if res:
            true_password = res[2]

            verify_res = self.login_verify(true_password)
            
            response_data = {"is_login_success": verify_res}

            if verify_res:
                session_id = SAGSI.generate_session_id()

                sql_connection = SQLC.SQL_Connector()
                query = "UPDATE users SET session_id = %s WHERE user_id = %s"
                values = (session_id, res[0])
                sql_connection.update_query(query, values)

                response_data.update({"comment": "Login success!"})
                response_data.update({"session_id": session_id})
                response_data.update({"username": res[1]})
                response_data.update({"user_id": res[0]})

            else:
                response_data.update({"comment": "Login failed!"})

        else:
            response_data = {"is_login_success": False, "comment": "Login failed!"}
    

        full_response_data = {"response-code": response_code, 
                            "response-comment": response_comment,
                            "data": response_data}
        
        return full_response_data


    def login_verify(self, true_password):
        
        bcrypt_verifier = b_verifier.Bcrypt_Verifier()
        verify_res = bcrypt_verifier.verify(true_password, self.password)
        
        return verify_res

