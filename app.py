import sys
sys.path.append('./domain/availability/')

from list_all_destinations import ListAllDestinations

if __name__ == '__main__':
    soapheaders = {}
    list_all_destinations = ListAllDestinations(soapheaders)
    list_all_destinations.execute()

    print('Iniciou')
