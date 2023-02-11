# GCP Datastore and email-based User authentication
Easy datastore-based user authentication by email

# Example usage

Install the library
```bash
python -m pip install git+https://github.com/agonzalezl/datastore-based-user-authentication-by-email.git
```

Example with Flask:
```python
from flask import Flask, request
from email_authenticator import Authenticator

app = Flask(__name__)

email_server='<email_server>'
email_address='<email_address>'
sender_name='<sender_name>'
sender_password='<sender_password>'
table_name='users'
auth = Authenticator(email_server, email_address, sender_password, sender_name, table_name)

@app.route('/login', methods=['POST'])
def root():
    content = request.json
    auth.sign_up(content['email'])
    return "ok", 200

@app.route('/resource', methods=['GET'])
@auth.login_required
def root():
    return "ok", 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
```