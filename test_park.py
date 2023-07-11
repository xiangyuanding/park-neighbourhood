'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
    test suite for class Park
'''

import unittest
from park import Park

STR_TEST="""parkname: Ocean park
park id: 01
neighbourhood: Downtown
facilities type: 0"""

class testPark(unittest.TestCase):
    '''
    test suite for class Park
    '''
    def test_park_init(self):
        '''
        Description:
            Test function for the __init__ function of class Park
        Parameter:
            self
        Return:
            none
        Raise:
            none
        '''
        park=Park("Ocean park","Downtown","01")
        self.assertEqual(park.name,"Ocean park")
        self.assertEqual(park.neighbourhood,"Downtown")
        self.assertEqual(park.park_id,"01")
    
    def test_park_init_TypeError(self):
        with self.assertRaises(TypeError):
            park=Park([1,2,3],"Ocean park","25")
        
        with self.assertRaises(TypeError):
            park=Park("Downtown",True,"25")
        
        with self.assertRaises(TypeError):
            park=Park("Downtown","Ocean park",25)
    
    def test_park_str(self):
        park=Park("Ocean park","Downtown","01")
        self.assertEqual(str(park),STR_TEST)
        
    def test_park_eq(self):
        park_1=Park("Water park","West end","17")
        park_2=Park("Animal park","Downtown","17")
        self.assertEqual(park_1,park_2)
        
    def test_park_not_eq(self):
        park_1=Park("Water park","West end","17")
        park_2=Park("Water park","West end","03")
        self.assertNotEqual(park_1,park_2)
    
    def test_park_eq_TypeError(self):
        with self.assertRaises(TypeError):
            park_1=Park("Ocean park","Downtown","01")
            park_2="Basketball Park"
            park_1==park_2
            

def main():
    '''
    Description:
        test suite for class Park
    Raise:
        none
    '''
    unittest.main(verbosity = 3)
    
if __name__=="__main__":
    main()

