'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
    This file stores class Neighbourhood
'''

from park import Park

STR_METHOD="name: {}\nparks: {}\nnumber of parks: {}\nfacilities:{}\nnumber of facilities:{}\n"

class Neighbourhood():
    '''
    class Neighbourhood, it represents a neighbourhood in vancouver, and stores data of parks and park facilities in it
    '''
    def __init__(self,name,park_list):
        '''
        Description:
            class instances
        Parameter:
            self
            name: str
            park_list: list
        Return:
            none
        Raise:
            TypeError if init has wrong data type
        '''
        if type(name)!=str or type(park_list)!=list:
            raise TypeError("name should be str, park_list should be list")
        self.name=name
        self.park_list=park_list
        self.facilities=self.merge_facilities()
        self.facilities_count=self.count_facilities()
    
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
        parks=[]
        for i in self.park_list:
            parks.append(i.name)
        return STR_METHOD.format(self.name,parks,len(self.park_list),self.facilities,self.facilities_count)
    
    def __eq__(self,other):
        '''
        Description:
            equivalent method
        Parameter:
            self
            other: Neighbourhood
        Return:
            bool
        Raise:
            TypeError if other is not Neighbourhood
        '''
        if type(other)==Neighbourhood:
            return self.name==other.name
        else:
            raise TypeError
        
    def merge_facilities(self):
        '''
        Description:
            merge the facilities of the parks to a dictionary
        Parameter:
            self
        Return:
            dict
        Raise:
            TypeError if the park_list is not a list
            ValueError if the elements in park_list are not Park objects
        '''
        if type(self.park_list)!=list:
            raise TypeError
        if self.park_list!=[] and type(self.park_list[0])!=Park:
            raise ValueError
        facility_dict={}
        for park in self.park_list:
            for facility in park.facilities:
                if facility.facility_type not in facility_dict:
                    facility_dict[facility.facility_type]=facility.count
                else:
                    facility_dict[facility.facility_type]+=facility.count
        return facility_dict
    
    def count_facilities(self):
        '''
        Description:
            count how many facilities are there in total
        Parameter:
            self
        Return:
            int
        Raise:
            TypeError if facilities is not a dict
        '''
        if type(self.facilities)!=dict:
            raise TypeError
        count=0
        for i in self.facilities:
            count+=self.facilities[i]
        return count