from abc import ABC, abstractmethod

class RequestJson(ABC):
    '''Abstract class to ensure execute method implementation'''

    def __str__(self):
        return self.__class__.__name__

    def __init__(self, soapheaders):
        '''constructor with parameter to authentication'''
        self.soapheaders = soapheaders

    @abstractmethod
    def execute(self):
        '''Execute call in SOAP destination'''
