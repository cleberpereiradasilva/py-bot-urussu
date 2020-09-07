from contractor import request_json

class ListAllDestinations(request_json.RequestJson):
    '''Class to make request in ListAllDestinations and return a json'''

    def execute(self):
        '''Execute call in SOAP destination'''        
