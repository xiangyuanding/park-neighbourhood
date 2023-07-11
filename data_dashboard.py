'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
    This program is written to combine the park data and park facility data to analyze the park facilities in all neighbourhoods in vancouver 
'''

from data_preprocess_functions import *
from tkinter_window import *

def main():
    '''
    Description:
        run all the data analysis process
    Raise:
        none
    '''
    try:
        file=get_file(PARK_FACILITY)
        file_list=clean_facility_data(file)
        facility_list=put_data_in_facility_object(file_list)
        facility_kinds=find_all_kinds_of_facilities(facility_list)
        facility_kinds.sort()
        
        file=get_file(PARK)
        file_list=clean_park_data(file)
        park_list=put_data_in_park_object(file_list)
        park_list=add_facility_to_parks(park_list,facility_list)
        
        neighbourhood_list=add_parks_to_neighbourhoods(park_list)
        tkinter_window=TkinterWindow(facility_kinds, neighbourhood_list)
        tkinter_window.run()
        
    except TypeError:
       print("please check the type of the parameter")
    except ValueError:
       print("please check the type of the elements in the list")
    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError("Please check the url")
    except requests.exceptions.ConnectionError:
        raise requests.exceptions.ConnectionError("Please check your network")

if __name__=="__main__":
    main()

