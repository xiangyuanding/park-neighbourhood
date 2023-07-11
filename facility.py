'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
    This file stores class Facility
'''

STR_METHOD='facility: {}\namount: {}\npark id: {}'

class Facility():
    '''
    class Facility, it represents a facility of a park in vancouver, and stores data of park facilities in it
    '''
    def __init__(self,facility_type,count,park_id):
        '''
        Description:
            class instances
        Parameter:
            self
            facility_type: str
            count: int
            park_id: str
        Return:
            none
        Raise:
            TypeError if init has wrong data type
        '''
        if type(facility_type)!=str or type(count)!=int or type(park_id)!=str:
            raise TypeError
        self.facility_type=facility_type
        self.count=count
        self.park_id=park_id
    
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
        return STR_METHOD.format(self.facility_type,self.count,self.park_id) 
    
    def __eq__(self,other):
        '''
        Description:
            equivalent method
        Parameter:
            self
            other: Facility
        Return:
            bool
        Raise:
            TypeError if other is not Facility
        '''
        if type(other)==Facility:
            return self.facility_type==other.facility_type
        else:
            raise TypeError
            