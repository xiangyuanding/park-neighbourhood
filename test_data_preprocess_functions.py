'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
    test suite for data preprocess functions
'''

import unittest
from data_preprocess_functions import *
from requests import exceptions
from park import Park
from facility import Facility

PARK_URL="https://opendata.vancouver.ca/explore/dataset/parks/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
FACILITY_URL="https://opendata.vancouver.ca/explore/dataset/parks-facilities/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
FAKE_PARK_URL_1="https://endata.vancouver.ca/explore/dataset/parks/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
FAKE_PARK_URL_2="https://opendata.vancouver.ca/exp/dataset/parks/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
PARK_DATA_SAMPLE="ParkID;Name;Official;Advisories;SpecialFeatures;Facilities;Washrooms;StreetNumber;StreetName;EWStreet;NSStreet;NeighbourhoodName;NeighbourhoodURL;Hectare;GoogleMapDest\r\n1;Arbutus Village Park;1;N;N;Y;N;4202;Valley Drive;King Edward Avenue;Valley Drive;Arbutus-Ridge;https://vancouver.ca/news-calendar/arbutus-ridge.aspx;1.41;49.249783,-123.15525\r\n"
FACILITY_DATA_SAMPLE="FacilityCount;FacilityType;FacilityURL;ParkID;Name\r\n2;Softball;;2;Carnarvon Park\r\n1;Basketball Courts;;14;Coopers' Park"

class testDataPreprocessFunctions(unittest.TestCase):
    '''
    test suite for data preprocess functions
    '''
    def test_get_file(self):
        '''
        Description:
            Test function for get_file()
        Parameter:
            self
        Return:
            none
        Raise:
            none
        '''
        content=get_file(PARK_URL)
        self.assertEqual(content[0:20],"ParkID;Name;Official")
        self.assertEqual(content[-20:],";49.256978,-123.09\r\n")

        content=get_file(FACILITY_URL)
        self.assertEqual(content[0:20],"FacilityCount;Facili")
        self.assertEqual(content[-20:],";245;Trillium Park\r\n")
        
    def test_get_file_ConnectionError(self):
        with self.assertRaises(exceptions.ConnectionError):
            get_file(FAKE_PARK_URL_1)
          
    def test_get_file_HTTPError(self):
        with self.assertRaises(exceptions.HTTPError):
            get_file(FAKE_PARK_URL_2)
            
    def test_clean_facility_data(self):
        facility_data=clean_facility_data(FACILITY_DATA_SAMPLE)
        self.assertEqual(facility_data,[['FacilityCount', 'FacilityType', 'ParkID'], ['2', 'Softball', '2']])
        
    def test_clean_facility_data_TypeError(self):
        with self.assertRaises(TypeError):
            facility_data=clean_facility_data(True) 
        
    def test_clean_facility_data_ValueError(self):
        with self.assertRaises(ValueError):
            facility_data=clean_facility_data("2;Softball;;2;Carnarvon Park")

    def test_clean_park_data(self):
        park_data=clean_park_data(PARK_DATA_SAMPLE)
        self.assertEqual(park_data[1],['1', 'Arbutus Village Park', 'Arbutus-Ridge'])
        
    def test_clean_park_data_TypeError(self):
        with self.assertRaises(TypeError):
            park_data=clean_park_data(30)

    def test_clean_park_data_ValueError(self):
        with self.assertRaises(ValueError):
            park_data=clean_park_data("Arbutus Village Park;1;N;N;Y;N;4202;Valley Drive;King Edward Avenue;Valley Drive;Arbutus-Ridge;https://vancouver.ca/news-calendar/arbutus-ridge.aspx;1.41;49.249783,-123.15525\r\n")

    def test_put_data_in_facility_object(self):
        facility_list=put_data_in_facility_object([['FacilityCount', 'FacilityType', 'ParkID'], ['2', 'Softball', '2'],["1","Basketball","14"]])
        self.assertEqual(facility_list[0].facility_type,'Softball')
        self.assertEqual(facility_list[0].park_id,'2')
        self.assertEqual(facility_list[0].count,2)
        self.assertIsInstance(facility_list[0],Facility)
    
    def test_put_data_in_facility_object_TypeError(self):
        with self.assertRaises(TypeError):
            facility_list=put_data_in_facility_object({'2', 'Softball', '2'})
        
    def test_put_data_in_facility_object_ValueError(self):
        with self.assertRaises(ValueError):    
            facility_list=put_data_in_facility_object([["1","Basketball","14"]])
        
    def test_put_data_in_park_object(self):
        park_list=put_data_in_park_object([['ParkID', 'Name', 'NeighbourhoodName'], ['1', 'Arbutus Village Park', 'Arbutus-Ridge']])
        self.assertEqual(park_list[0].name,'Arbutus Village Park')
        self.assertEqual(park_list[0].park_id,'1')
        self.assertEqual(park_list[0].neighbourhood,'Arbutus-Ridge')
        self.assertIsInstance(park_list[0],Park)
        
    def test_put_data_in_park_object_TypeError(self):
        with self.assertRaises(TypeError):
            park_list=put_data_in_park_object("[['ParkID', 'Name', 'NeighbourhoodName'], ['1', 'Arbutus Village Park', 'Arbutus-Ridge']]")
        
    def test_put_data_in_park_object_ValueError(self):
        with self.assertRaises(ValueError): 
            park_list=put_data_in_park_object([['1', 'Arbutus Village Park', 'Arbutus-Ridge']])

    def test_add_facility_to_parks(self):
        park_1=Park("Water park","West end","17")
        park_2=Park("Ocean park","Downtown","21")
        facility_1=Facility("Basketball court",3,"17")
        facility_2=Facility("tennis court",10,"17")
        facility_3=Facility("table tennis",5,"21")
        facility_list=[facility_1,facility_2,facility_3]
        park_list=[park_1,park_2]
        park_list=add_facility_to_parks(park_list, facility_list)
        self.assertEqual(park_1.facilities[0],facility_1)
        self.assertEqual(park_1.facilities[1],facility_2)
        self.assertEqual(park_2.facilities[0],facility_3)
        
    def test_add_facility_to_parks_TypeError(self):
        with self.assertRaises(TypeError):
            park_1=Park("Water park","West end","17")
            add_facility_to_parks([park_1],"facility_1")
        
        with self.assertRaises(TypeError):
            facility_1=Facility("Basketball court",3,"17")
            add_facility_to_parks("park_1",[facility_1])
        
    def test_add_facility_to_parks_ValueError(self):
        park_1=Park("Water park","West end","17")
        facility_1=Facility("Basketball court",3,"17")
        with self.assertRaises(ValueError):
            add_facility_to_parks([facility_1],[park_1])
        
        with self.assertRaises(ValueError):
            add_facility_to_parks(["park_1"],[facility_1])
            
        with self.assertRaises(ValueError):
            add_facility_to_parks([park_1],["facility_1"])

    def test_add_parks_to_neighbourhoods(self):
        park_1=Park("Water park","West end","17")
        park_2=Park("Ocean park","Downtown","21")
        neighbourhood_list=add_parks_to_neighbourhoods([park_1,park_2])
        self.assertEqual(neighbourhood_list[0].name,"West end")
        self.assertEqual(neighbourhood_list[0].park_list[0],park_1)
        self.assertEqual(neighbourhood_list[1].name,"Downtown")
        self.assertEqual(neighbourhood_list[1].park_list[0],park_2)

    def test_add_parks_to_neighbourhoods_TypeError(self):
        park_1=Park("Water park","West end","17")
        with self.assertRaises(TypeError):
            add_parks_to_neighbourhoods(park_1)
            
    def test_add_parks_to_neighbourhoods_ValueError(self):
        park_1=Park("Water park","West end","17")
        with self.assertRaises(ValueError):
            add_parks_to_neighbourhoods([23,park_1])

    def test_find_all_kinds_of_facilities(self):
        facility_1=Facility("Basketball court",3,"17")
        facility_2=Facility("tennis court",10,"17")
        facility_3=Facility("table tennis",5,"21")
        facility_4=Facility("Basketball court",4,"30")
        facility_kinds=find_all_kinds_of_facilities([facility_1,facility_2,facility_3,facility_4])
        self.assertEqual(facility_kinds,["Basketball court","tennis court","table tennis"])

    def test_find_all_kinds_of_facilities_TypeError(self):
        with self.assertRaises(TypeError):
            find_all_kinds_of_facilities("Basketball court")
            
    def test_find_all_kinds_of_facilities_ValueError(self):
        with self.assertRaises(ValueError):
            find_all_kinds_of_facilities(["Basketball court","tennis court"])
            

def main():
    '''
    Description:
        test suite for data preprocess functions
    Raise:
        none
    '''
    unittest.main(verbosity = 3)
    
if __name__=="__main__":
    main()

