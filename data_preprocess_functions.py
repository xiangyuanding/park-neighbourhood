'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
    contains data preprocess functions that will be used in the main function of data_dashboard
'''

import requests
from neighbourhood import Neighbourhood
from park import Park
from facility import Facility
from tkinter import *
from tkinter import ttk

PARK_FACILITY="https://opendata.vancouver.ca/explore/dataset/parks-facilities/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
PARK="https://opendata.vancouver.ca/explore/dataset/parks/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"

NEIGHBOURHOOD_INDEX=11
PARK_ID_INDEX=3
PARK_FIRST_LINE="ParkID;Name;Official;Advisories;SpecialFeatures;Facilities;Washrooms;StreetNumber;StreetName;EWStreet;NSStreet;NeighbourhoodName;NeighbourhoodURL;Hectare;GoogleMapDest"
FACILITY_FIRST_LINE="FacilityCount;FacilityType;FacilityURL;ParkID;Name"
FACILITY_FIRST_ITEM=['FacilityCount','FacilityType','ParkID']
PARK_FIRST_ITEM=['ParkID','Name','NeighbourhoodName']

def get_file(filename):
    '''
    Description:
        get a csv file content from a url link
    Parameter:
        filename: str
    Return:
        str
    Raise:
        none
    '''
    try:
        file=requests.get(filename)
        file.raise_for_status()
    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError("Please check the url")
    except requests.exceptions.ConnectionError:
        raise requests.exceptions.ConnectionError("Please check your network")
    else:
        return file.text

def clean_facility_data(file):
    '''
    Description:
        clean the data of facility dataset, ignore some columns and return a nested list
    Parameter:
        file: str
    Return:
        list
    Raise:
        TypeError if wrong input type
        ValueError if wrong input data
    '''
    if type(file)!=str:
        raise TypeError
    file_list=[]    
    file_list=file.split("\r\n")
    if file_list!=[] and file_list[0]!=FACILITY_FIRST_LINE:
        raise ValueError
    for i in range(len(file_list)):
        line=file_list[i].split(";")
        file_list[i]=line[0:2]+line[PARK_ID_INDEX:PARK_ID_INDEX+1]
    file_list.pop()
    return file_list
    
def clean_park_data(file):
    '''
    Description:
        clean the park dataset, ignore some columns and return a nested list
    Parameter:
        file: str
    Return:
        list
    Raise:
        TypeError if wrong input type
        ValueError if wrong input data
    '''  
    if type(file)!=str:
        raise TypeError
    file_list=[]    
    file_list=file.split("\r\n")
    if file_list[0]!=PARK_FIRST_LINE:
        raise ValueError
    for i in range(len(file_list)):
        line=file_list[i].split(";")
        file_list[i]=line[0:2]+line[NEIGHBOURHOOD_INDEX:NEIGHBOURHOOD_INDEX+1]
    file_list.pop()
    return file_list

def put_data_in_facility_object(file_list):
    '''
    Description:
        put the list of data in the Facility object
    Parameter:
        file_list: list
    Return:
        list
    Raise:
        TypeError if wrong input type
        ValueError if wrong input data
    '''  
    if type(file_list)!=list:
        raise TypeError
    if file_list[0]!=FACILITY_FIRST_ITEM:
        raise ValueError
    facility_list=[]
    for i in range(1,len(file_list)):
        facility_list.append(Facility(file_list[i][1],int(file_list[i][0]),file_list[i][2]))
    return facility_list

def put_data_in_park_object(file_list):
    '''
    Description:
        put the list of data in the Park object
    Parameter:
        file_list: list
    Return:
        list
    Raise:
        TypeError if wrong input type
        ValueError if wrong input data
    '''  
    if type(file_list)!=list:
        raise TypeError
    if file_list[0]!=PARK_FIRST_ITEM:
        raise ValueError
    park_list=[]
    for i in range(1,len(file_list)):
        park_list.append(Park(file_list[i][1],file_list[i][2],file_list[i][0]))
    return park_list

def add_facility_to_parks(park_list,facility_list):
    '''
    Description:
        put the Facility objects in Park objects
    Parameter:
        facility_list: list
        park_list: list
    Return:
        list
    Raise:
        TypeError if wrong input type
        ValueError if wrong input data
    '''  
    if type(park_list)!=list or type(facility_list)!=list:
        raise TypeError
    if type(park_list[0])!=Park or type(facility_list[0])!=Facility:
        raise ValueError
    for i in facility_list:
        for j in range(len(park_list)):
            if i.park_id==park_list[j].park_id:
                park_list[j].facilities.append(i)
    return park_list

def add_parks_to_neighbourhoods(park_list):
    '''
    Description:
        put the Park objects in Neighbourhood objects
    Parameter:
        park_list: list
    Return:
        list
    Raise:
        TypeError if wrong input type
        ValueError if wrong input data
    '''
    if type(park_list)!=list:
        raise TypeError
    if type(park_list[0])!=Park:
        raise ValueError
    neighbourhood_dict={}
    neighbourhood_list=[]
    for i in park_list:
        if i.neighbourhood not in neighbourhood_dict:
            neighbourhood_dict[i.neighbourhood]=[i]
        else:
            neighbourhood_dict[i.neighbourhood].append(i)
    for i in neighbourhood_dict:
        neighbourhood_list.append(Neighbourhood(i,neighbourhood_dict[i]))
    return neighbourhood_list

def find_all_kinds_of_facilities(facility_list):
    '''
    Description:
        find all types of facilities and store them in a list
    Parameter:
        facility_list: list
    Return:
        list
    Raise:
        TypeError if facility_list is not a list
        ValueError if the items in facility_list are not Facility
    '''
    if type(facility_list)!=list:
        raise TypeError
    if type(facility_list[0])!=Facility:
        raise ValueError
    facility_kinds=[]
    for i in facility_list:
        if i.facility_type not in facility_kinds:
            facility_kinds.append(i.facility_type)
    return facility_kinds
