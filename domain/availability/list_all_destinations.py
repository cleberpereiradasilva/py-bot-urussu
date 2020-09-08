from domain.availability.contractor.request_json import RequestJson

class ListAllDestinations(RequestJson):
    '''Class to make request in ListAllDestinations and return a json'''

    def execute(self):
        '''Execute call in SOAP destination'''        
        print("Send request...")
