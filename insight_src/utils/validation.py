import os  # Import the os module to interact with the operating system
import logging  # Import the logging module to log messages
import requests

# Configure logging
logger = logging.getLogger(__name__)  # Create a logger object


def validate_openai_env_vars():
    # List of required environment variables
    required_vars = ['OPENAI_API_KEY', 'OPENAI_API_VERSION', 'OPENAI_MODEL_NAME']

    # Check for missing environment variables
    missing_vars = [var for var in required_vars if var not in os.environ or not os.environ[var]]

    # If there are missing variables, raise an error
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
    else:
        # If all variables are set, log a confirmation message
        logger.info("All required OpenAI environment variables are set.")


def validate_cisco_env_vars():
    # List of required environment variables
    required_vars = ['CISCO_API_CLIENT_ID', 'CISCO_API_CLIENT_SECRET', 'CISCO_API_AUTH_HOST']

    # Check for missing environment variables
    missing_vars = [var for var in required_vars if var not in os.environ or not os.environ[var]]

    # If there are missing variables, raise an error
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
    else:
        # If all variables are set, log a confirmation message
        logger.info("All required OpenAI environment variables are set.")


import time  # Import the time module to work with timestamps


def validate_cisco_api_token(cisco_api_client_id: str = None, cisco_api_client_secret: str = None):
    """
    Helps to take Cisco Client Key, Cisco Client Secret and validate if they are valid
    :param cisco_api_client_id: Cisco API Client ID, if not provided will be taken from environment variable
    :param cisco_api_client_secret: Cisco API Client Secret, if not provided will be taken from environment variable
    :return:
    """
    CISCO_API_HOST = os.getenv("CISCO_API_AUTH_HOST") or "https://id.cisco.com/oauth2/default/v1/token"
    cisco_api_client_id = cisco_api_client_id or os.getenv("CISCO_API_CLIENT_ID")
    cisco_api_client_secret = cisco_api_client_secret or os.getenv("CISCO_API_CLIENT_SECRET")

    # Check if the token is still valid
    token_expires_at = os.getenv("CISCO_API_TOKEN_EXPIRES_AT")
    current_time = time.time()
    if token_expires_at and current_time < float(token_expires_at):
        logger.info("Using existing Cisco API token")
        return {
            "access_token": os.getenv("CISCO_API_BEARER_TOKEN"),
            "expires_in": os.getenv("CISCO_API_TOKEN_EXPIRES_IN"),
            "expires_at": os.getenv("CISCO_API_TOKEN_EXPIRES_AT")
        }

    # Perform the authentication call to Cisco API
    auth_url = f"{CISCO_API_HOST}"
    auth_data = {
        "grant_type": "client_credentials",
        "client_id": cisco_api_client_id,
        "client_secret": cisco_api_client_secret
    }
    response = requests.post(auth_url, data=auth_data)

    # Check if the authentication was successful
    if response.status_code == 200:
        auth_response = response.json()
        token = auth_response.get("access_token")
        expires_in = auth_response.get("expires_in")
        expires_at = current_time + int(expires_in)

        # Update environment variables
        os.environ["CISCO_API_BEARER_TOKEN"] = token
        os.environ["CISCO_API_TOKEN_EXPIRES_IN"] = str(expires_in)
        os.environ["CISCO_API_TOKEN_EXPIRES_AT"] = str(expires_at)

        logger.info("Successfully authenticated with Cisco API")
        return auth_response
    else:
        raise EnvironmentError(f"Failed to authenticate with Cisco API: {response.status_code} {response.text}")


def initialize():
    # Example usage
    try:
        # Validate the OpenAI environment variables
        validate_openai_env_vars()
        validate_cisco_env_vars()
    except EnvironmentError as e:
        # Log the error message if any environment variables are missing
        logger.error(e)
