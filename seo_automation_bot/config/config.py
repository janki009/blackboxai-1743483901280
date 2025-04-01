import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        'TARGET_URL': os.getenv('TARGET_URL', 'https://example.com'),
        'SELENIUM_DRIVER_PATH': os.getenv('SELENIUM_DRIVER_PATH'),
        'MAX_RETRIES': int(os.getenv('MAX_RETRIES', '3')),
        'REQUEST_TIMEOUT': int(os.getenv('REQUEST_TIMEOUT', '30')),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO')
    }