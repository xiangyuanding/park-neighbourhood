'''
    CS 5001
    Final project
    Fall 2022
    Xiangyuan DING 
    This file stores class TkinterWindow
'''
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from neighbourhood import Neighbourhood

TITLE="Facility-Neighbourhood"
USER_INPUT='please choose a facilicty'
LABEL="This program is made to show the distribution of park facilities in \nall neighbourhoods in Vancouver \n\nPlease select a facility and click \'continue\' to see the graph"
SIZE="400x300"
FIGSIZE=(15,7)
COMBOBOX_STATE="readonly"
BUTTON_DISABLE="disabled"
BUTTON_ACTIVE="active"
BUTTON_TEXT='continue'
BIND_EVENT="<<ComboboxSelected>>"
XLABEL="Number of {}"
YLABEL="Neighbourhoods"
YLABEL_ROTATION="horizontal"
TKINTER_STR="Tkinter window\nSize: {}\nTitle: {}"

class TkinterWindow():
    """
    class TkinterWindow, it represents a tkinter window that is used for asking user input
    """
    def __init__(self,facility_kinds,dataset):
        '''
        Description:
            class instances
        Parameter:
            self
            facility_kinds: list
            dataset: list
        Return:
            none
        Raise:
            TypeError if facility_kinds or dataset has wrong data type
            ValueError if the items in dataset are not Neighbourhood
        '''
        self.root=Tk()
        self.user_input=StringVar(value=USER_INPUT)
        self.label=ttk.Label(self.root,text=LABEL)
        if type(facility_kinds)!=list or type(dataset)!=list:
            raise TypeError
        if dataset!=[] and type(dataset[0])!=Neighbourhood:
            raise ValueError
        self.facility_kinds=facility_kinds
        self.dataset=dataset
        self.combobox=ttk.Combobox(self.root,state=COMBOBOX_STATE,textvariable=self.user_input,value=self.facility_kinds)
        self.button=ttk.Button(self.root,state=BUTTON_DISABLE,text=BUTTON_TEXT,command=self.draw_graph)
    
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
        return TKINTER_STR.format(SIZE,TITLE)
    
    def __eq__(self,other):
        '''
        Description:
            equivalent method
        Parameter:
            self
            other: TkinterWindow
        Return:
            bool
        Raise:
            TypeError if other is not a TkinterWindow
        '''
        if type(other)==TkinterWindow:
            return self.root==other.root
        else:
            raise TypeError
    
    def run(self):
        '''
        Description:
            runs the tkinter window, let user choose their facility
        Parameter:
            self
        Return:
            none
        Raise:
            none
        '''
        self.root.title(TITLE)
        self.root.geometry(SIZE)
        self.root.bind(BIND_EVENT,self.enable_button)
        self.label.pack()
        self.combobox.pack()
        self.button.pack()
        self.root.mainloop()
        
    def draw_graph(self):
        '''
        Description:
            a function that needs to be called when a button is clicked
        Parameter:
            self
        Return:
            none
        Raise:
            none
        '''
        user_input=self.user_input.get() 
        neighbourhood_dict=self.find_facilities_in_each_neighbourhood(user_input)
        neighbourhood_list=list(neighbourhood_dict.keys())
        facility_count=list(neighbourhood_dict.values())
        
        fig,ax=plt.subplots(figsize=FIGSIZE)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xlabel(XLABEL.format(user_input))
        plt.ylabel(YLABEL,rotation=YLABEL_ROTATION)
        ax.yaxis.set_label_coords(0,1)
        ax.barh(range(len(facility_count)),facility_count,tick_label=neighbourhood_list)
        plt.show()
        
    def find_facilities_in_each_neighbourhood(self,facility):    
        '''
        Description:
            find the the number of user input facilities in each neighbourhood, return a sorted dict
        Parameter:
            self
            facility: str
        Return:
            dict
        Raise:
            TypeError if the input facility is not str
        '''
        if type(facility)!=str:
            raise TypeError
        neighbourhood_dict={}
        for i in self.dataset:
            if facility in i.facilities:
                neighbourhood_dict[i.name]=i.facilities[facility]
            else:
                neighbourhood_dict[i.name]=0
        neighbourhood_dict=dict(sorted(neighbourhood_dict.items(),reverse=True,key=lambda value: value[0]))
        neighbourhood_dict=dict(sorted(neighbourhood_dict.items(),key=lambda value: value[1]))
        return neighbourhood_dict
        
    def enable_button(self,event):
        '''
        Description:
            an event that makes the button clickable
        Parameter:
            self
            event: event
        Return:
            none
        Raise:
            none
        '''
        self.button.configure(state=BUTTON_ACTIVE)  
        

