'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
'''

import unittest
from park import Park
from facility import Facility
from neighbourhood import Neighbourhood

PARK_1=Park("Ocean park","Downtown","01")
PARK_2=Park("Waterloo park","Downtown","02")
FACILITY_1=Facility("Basketball court",3,"27")
FACILITY_2=Facility("tennis court",10,"27")
FACILITY_3=Facility("table tennis",5,"21")
FACILITY_4=Facility("Basketball court",1,"21")
PARK_1.facilities=[FACILITY_1,FACILITY_2]
PARK_2.facilities=[FACILITY_3,FACILITY_4]
STR_TEST="""name: Downtown
parks: ['Ocean park', 'Waterloo park']
number of parks: 2
facilities:{'Basketball court': 4, 'tennis court': 10, 'table tennis': 5}
number of facilities:19
"""

class testNeighbourhood(unittest.TestCase):
    '''
    test suite for class Neighbourhood
    '''
    def test_Neighbourhood_init(self):
        '''
        Description:
            Test function for the __init__ function of class Neighbourhood
        Parameter:
            self
        Return:
            none
        Raise:
            none
        '''
        neighbourhood=Neighbourhood("Downtown",[PARK_1,PARK_2])
        self.assertEqual(neighbourhood.name,"Downtown")
        self.assertEqual(neighbourhood.park_list,[PARK_1,PARK_2])
    
    def test_neighbourhood_init_TypeError(self):
        with self.assertRaises(TypeError):
            neighbourhood=Neighbourhood(["West end"],[PARK_1,PARK_2])
        
        with self.assertRaises(TypeError):
            neighbourhood=Neighbourhood("West end","park_1, park_2")
        
    def test_neighbourhood_str(self):
        neighbourhood=Neighbourhood("Downtown",[PARK_1,PARK_2])
        self.assertEqual(str(neighbourhood),STR_TEST)
        
    def test_neighbourhood_eq(self):
        neighbourhood_1=Neighbourhood("Downtown",[PARK_2])
        neighbourhood_2=Neighbourhood("Downtown",[PARK_1])
        self.assertEqual(neighbourhood_1,neighbourhood_2)
        
    def test_neighbourhood_not_eq(self):
        neighbourhood_1=Neighbourhood("Downtown",[PARK_1,PARK_2])
        neighbourhood_2=Neighbourhood("Fairview",[PARK_1,PARK_2])
        self.assertNotEqual(neighbourhood_1,neighbourhood_2)
    
    def test_neighbourhood_eq_TypeError(self):
        with self.assertRaises(TypeError):
            neighbourhood_1=Neighbourhood("Downtown",[PARK_1,PARK_2])
            neighbourhood_2="Downtown"
            neighbourhood_1==neighbourhood_2
        
    def test_merge_facilities(self):
        neighbourhood=Neighbourhood("Downtown",[PARK_1,PARK_2])
        self.assertEqual(neighbourhood.facilities,{'Basketball court': 4, 'tennis court': 10, 'table tennis': 5})
    
    def test_merge_facilities_TypeError(self):
        with self.assertRaises(TypeError):
            neighbourhood=Neighbourhood("Fairview",[PARK_1,PARK_2])
            neighbourhood.park_list=PARK_1
            neighbourhood.merge_facilities()
    
    def test_merge_facilities_ValueError(self):
        with self.assertRaises(ValueError):
            neighbourhood=Neighbourhood("Fairview",["park_1","park_2"])
    
    def test_count_facilities(self):
        neighbourhood=Neighbourhood("Downtown",[PARK_1,PARK_2])
        self.assertEqual(neighbourhood.facilities_count,19)
        
    def test_count_facilities_TypeError(self):
        with self.assertRaises(TypeError):
            neighbourhood=Neighbourhood("Downtown",[PARK_1,PARK_2])
            neighbourhood.facilities="basketball"
            neighbourhood.count_facilities()
        
    
def main():
    '''
    Description:
        test suite for class Neighbourhood
    Raise:
        none
    '''
    unittest.main(verbosity = 3)
    
if __name__=="__main__":
    main()

