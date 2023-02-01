import uuid
import email_authenticator.model as model
import email_authenticator.email_client as email_client

class Authenticator:

    def __init__(self, email_server, email_address, sender_password, sender_name, datastore_table_name):
        email_client.init_client(email_server, email_address, sender_name, sender_password)
        if datastore_table_name:
            model.set_table_name(datastore_table_name)

    def generate_token(self)->str:
        return str(uuid.uuid4())

    def sign_up(self, email: str):
        token = self._generate_token_and_store_user(email)
        self._send_email(email, token)

    def login(self, email: str, token: str):
        if user := model.fetch_user(email, token):
            return user
        raise Exception()

    def _generate_token_and_store_user(self, email: str)->str:
        registered_user = model.fetch_user(email)
        token = self.generate_token()

        if not registered_user:
            model.store_user(email, token)
            return token
        
        registered_user[0].update({
            'token' : token
        })
        model.update_entity(registered_user[0])
        return token

    def _send_email(self, email: str, token: str)->str:
        email_client.send_email(email, html_content=token, subject="Welcome")
