import os

PRIVATE_KEY = (os.environ['PRIVATE_KEY']).replace("\\n", "\n")

json_dict = {
    "type": "service_account",
    "project_id": "vita-nail",
    "private_key_id": "6b48e48884edf8d400669bf2ddd650fa8698322a",
    "private_key": "-----BEGIN PRIVATE KEY-----\n" + rf'{PRIVATE_KEY}' + "\n-----END PRIVATE KEY-----\n",
    "client_email": "service@vita-nail.iam.gserviceaccount.com",
    "client_id": "109707024276837854466",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service%40vita-nail.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}
