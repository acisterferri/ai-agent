import os
from google.cloud import secretmanager

def access_secret_version():
    # Create the Secret Manager client
    client = secretmanager.SecretManagerServiceClient()
    
    # Get the secret name from the environment variable
    secret_name = os.getenv("GCP_SECRET_NAME")

    # Access the latest version of the secret
    response = client.access_secret_version(name=secret_name)

    # Get the secret data
    secret_data = response.payload.data.decode('UTF-8')
    
    # Store the secret value in the environment variable
    os.environ["GOOGLE_API_KEY"] = secret_data