'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
'''

import unittest
from facility import Facility

STR_TEST="""facility: Basketball court
amount: 3
park id: 27"""

class testFacility(unittest.TestCase):
    '''
    test suite for class Facility
    '''
    def test_facility_init(self):
        '''
        Description:
            Test function for the __init__ function of class Facility
        Parameter:
            self
        Return:
            none
        Raise:
            none
        '''
        facility=Facility("Basketball court",3,"27")
        self.assertEqual(facility.facility_type,"Basketball court")
        self.assertEqual(facility.count,3)
        self.assertEqual(facility.park_id,"27")
    
    def test_facility_init_TypeError(self):
        with self.assertRaises(TypeError):
            facility=Facility(["basketball court"],3,"27")
        
        with self.assertRaises(TypeError):
            facility=Facility("Basketball court","3","27")
        
        with self.assertRaises(TypeError):
            facility=Facility("Basketball court",3,False)
    
    def test_facility_str(self):
        facility=Facility("Basketball court",3,"27")
        self.assertEqual(str(facility),STR_TEST)
        
    def test_facility_eq(self):
        facility_1=Facility("tennis court",10,"21")
        facility_2=Facility("tennis court",20,"17")
        self.assertEqual(facility_1,facility_2)
        
    def test_facility_not_eq(self):
        facility_1=Facility("tennis court",10,"21")
        facility_2=Facility("table tennis",10,"21")
        self.assertNotEqual(facility_1,facility_2)
    
    def test_facility_eq_TypeError(self):
        with self.assertRaises(TypeError):
            facility_1=Facility("Basketball court",3,"27")
            facility_2="Basketball court"
            facility_1==facility_2
        

def main():
    '''
    Description:
        test suite for class Facility
    Raise:
        none
    '''
    unittest.main(verbosity = 3)
    
if __name__=="__main__":
    main()

