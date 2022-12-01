#!/usr/bin/python3
import qi
import sys

'''
This class creates a qi session using the ip and port parameters provided as input to costructor
'''
class Session:
    '''
    The costructor creates a qi session object. It then uses the ip and port parameters to connect the object to Pepper OS
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self._session = qi.Session()
        self._connect()
    
    '''
    This method uses the session object to connect to Pepper OS. If an exception occurs, the application is killed.
    '''
    def _connect(self):
        try:
            self.session.connect("tcp://" + self.ip + ":" + str(self.port))
        except RuntimeError:
            print("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port) + ".\n "
                                                                                                 "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)

    '''
    This method reconnect the session object to Pepper OS
    @return: Returns the session object
    '''
    def reconnect(self):
        self._connect()
        return self.session
    
    '''
    Getter for the session object
    '''
    @property
    def session(self):
        return self._session
    
    '''
    This method returns the NaoQi service given as parameter.
    @param service_name: The name of the NaoQi service in form of string
    @return: Returns the service object
    '''
    def get_service(self, service_name: str):
        return self.session.service(service_name)
