'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
    test suite for class TkinterWindow
'''

import unittest
from park import Park
from facility import Facility
from neighbourhood import Neighbourhood
from tkinter_window import TkinterWindow

PARK_1=Park("Ocean park","Downtown","01")
FACILITY_1=Facility("Basketball court",3,"27")
FACILITY_2=Facility("tennis court",10,"27")
PARK_1.facilities=[FACILITY_1,FACILITY_2]
NEIGHBOURHOOD_1=Neighbourhood("Fairview",[PARK_1])

PARK_2=Park("Waterloo park","Downtown","02")
FACILITY_3=Facility("table tennis",5,"21")
FACILITY_4=Facility("Basketball court",1,"21")
PARK_2.facilities=[FACILITY_3,FACILITY_4]
NEIGHBOURHOOD_2=Neighbourhood("West end",[PARK_2])

STR_TEST="""Tkinter window
Size: 400x300
Title: Facility-Neighbourhood"""


class testTkinterWindow(unittest.TestCase):
    '''
    test suite for class TkinterWindow
    '''
    def test_TkinterWindow_init(self):
        '''
        Description:
            Test function for the __init__ function of class TkinterWindow
        Parameter:
            self
        Return:
            none
        Raise:
            none
        '''
        tkinter_window=TkinterWindow(["Basketball","Beaches","tennis court"],[NEIGHBOURHOOD_1])
        self.assertEqual(tkinter_window.facility_kinds,["Basketball","Beaches","tennis court"])
        self.assertEqual(tkinter_window.dataset,[NEIGHBOURHOOD_1])

    def test_TkinterWindow_init_TypeError(self):
        with self.assertRaises(TypeError):
            tkinter_window=TkinterWindow("Basketball,Beaches,tennis court",[NEIGHBOURHOOD_1])
        
        with self.assertRaises(TypeError):
            tkinter_window=TkinterWindow(["Basketball","Beaches","tennis court"],"Downtown")
    
    def test_TkinterWindow_init_ValueError(self):
        with self.assertRaises(ValueError):
            tkinter_window=TkinterWindow(["Basketball","Beaches","tennis court"],["Downtown"])
    
    def test_TkinterWindow_str(self):
        tkinter_window=TkinterWindow(["Basketball","Beaches","tennis court"],[NEIGHBOURHOOD_1])
        self.assertEqual(str(tkinter_window),STR_TEST)

#We are not going to test the __eq__ method since it involves Tk() object iin Tkinter
    def test_TkinterWindow_eq_TypeError(self):
        with self.assertRaises(TypeError):
            tkinter_window_1=TkinterWindow(["Basketball","Beaches","tennis court"],[NEIGHBOURHOOD_1])
            tkinter_window_2="TkinterWindow"
            tkinter_window_1==tkinter_window_2
                    
    def test_find_facilities_in_each_neighbourhood(self):
        tkinter_window=TkinterWindow(["Basketball","Beaches","tennis court"],[NEIGHBOURHOOD_1,NEIGHBOURHOOD_2])
        neighbourhood_dict=tkinter_window.find_facilities_in_each_neighbourhood('tennis court')
        self.assertEqual(neighbourhood_dict,{"Fairview":10,"West end":0})

    def test_find_facilities_in_each_neighbourhood_TypeError(self):
        with self.assertRaises(TypeError):
            tkinter_window=TkinterWindow(["Basketball","Beaches","tennis court"],[NEIGHBOURHOOD_1,NEIGHBOURHOOD_2])
            tkinter_window.find_facilities_in_each_neighbourhood(["tennis court"])

def main():
    '''
    Description:
        test suite for class TkinterWindow
    Raise:
        none
    '''
    unittest.main(verbosity = 3)
    
if __name__=="__main__":
    main()

