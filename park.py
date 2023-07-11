'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
    This file stores class Park
'''

STR_METHOD="parkname: {}\npark id: {}\nneighbourhood: {}\nfacilities type: {}"


class Park():
    '''
    class Park, it represents a park in vancouver, and stores data of parks in it
    '''
    def __init__(self,name,neighbourhood,park_id):
        '''
        Description:
            class instances
        Parameter:
            self
            name: str
            neighbourhood: str
            park_id: str
        Return:
            none
        Raise:
            TypeError if init has wrong data type
        '''
        if type(name)!=str or type(neighbourhood)!=str or type(park_id)!=str:
            raise TypeError
        self.name=name
        self.park_id=park_id
        self.neighbourhood=neighbourhood
        self.facilities=[]
        
    def __str__(self):
        '''
        Description:
            str method of the class
        Parameter:
            self
        Return:
            str
        Raise:
            none
        '''
        return STR_METHOD.format(self.name,self.park_id,self.neighbourhood,len(self.facilities))
    
    def __eq__(self,other):
        '''
        Description:
            equivalent method
        Parameter:
            self
            other: Park
        Return:
            bool
        Raise:
            TypeError if other is not Park
        '''
        if type(other)==Park:
            return self.park_id==other.park_id
        else:
            raise TypeError