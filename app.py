import os
from domain.availability.list_all_destinations import ListAllDestinations
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#NAME: user_name
#PASSWORD: user_password
#CODE:user_code
if __name__ == '__main__':
    print(os.getenv('NAME'))
    soapheaders = {}
    list_all_destinations = ListAllDestinations(soapheaders)
    list_all_destinations.execute()

    print('Iniciou')
