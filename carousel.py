#Coded by: Eshaan Krishna
#Reference: CMPUT-175 Refernce Study Material

from art import *
from circular_dlinked_list import *
import os
import json
import time

#Declare all constants

XC=1                            #Set the X-Cordinate.
YC=1                            #set the Y-Cordinate.
data=[]                         #The list of dictionaries from json is loaded into this list which runs common for all part of the code.
cdll=[]                         #The circular-doubly-linked-list runs common for all parts of the codes and get updated.   
CDLL_CAPACITY=5                 #The maximum size of the carousel

YES_CONTINUE=True               #The end of carousel tranversal

ANSI = {"CLEARLINE": "\033[0K", #for coloring text, RESET, CLEARLINE
        "ER1": "\033[90m",
        "ER2": "\033[91m",
        "RESET": "\033[0m"
        } 
def load_json():
    '''
    This function loads the json file, which is a list of dictionaries into data
    Input/Return: NA
    '''
    global data
    with open('emojis.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def find_emoji_by_name(emoji_name):
    '''
    This function finds the emoji character, and emoji class by the emoji name. If its not found, it returns None.
    Input:
        - emoji_name (str): The emoji name whose emoji charcter has to be displayed.
        - y (int): column number
    Returns:
        - emoji_class (str): The corresponding emoji class for the emoji name.
        - emoji_character (str): The corresponding emoji symbol for the emoji name
    '''
    global data
    for obj in data:
        if emoji_name in obj["emojis"]:
            emoji_class = obj["class"]
            emoji_character = obj["emojis"][emoji_name]
            return emoji_class, emoji_character
    return None, None

def validate_emoji_by_name(emoji_character):
    '''
    This function validates if the emoji character exists for an emoji_name. It validates until the correct emoji name is given by the user.
    Input:
        - emoji_character (str): The emoji name whose validation has to be done.
    Returns:
        - not_valid: Returns the result of validation, if the emoji exits or not.
    '''
    if emoji_character is not None:
        not_valid=False
    else:
        not_valid=True
    return not_valid

def find_emoji_by_character(emoji_character):
    '''
    This function finds the emoji name and emoji class for a particular emoji character/ symbol. If its not found, it returns None.
    Input:
        - emoji_character (str): The emoji character/ symbol whose emoji name has to be displayed.
    Returns:
        - emoji_class (str): The corresponding emoji class for the emoji character.
        - emoji_name (str): The corresponding emoji name for the emoji character.
    '''
    global data
    for obj in data:
        for name, char in obj["emojis"].items():
            if char == emoji_character:
                emoji_class = obj["class"]
                return emoji_class, name
    return None, None
    
def clear_screen():
    '''
    Clears the screen
    #Input/Output:NA
    '''
    if os.name == "nt": # for Windows
        os.system("cls")
    else: # for Mac/Linux
        os.system("clear")

   
def clear_line():
    '''
    Clears a line
    Input/Output:NA
    '''
    print(ANSI["CLEARLINE"], end='')
          
def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: NA
    '''
    print("\033[{1};{0}H".format(x, y), end='')
    
def display(X, Y, display_menu):
    '''
    This function displays the display menu with various option on the screen. The display menu options changes based on the functionality of the carousel.
    Input:
        - x (int): row number
        - y (int): column number
        - display_menu(list): contains the display menu options to perform desired operations.
    Returns: NA
    '''
    move_cursor(X, Y)
    print("Type any of the following commands to perform the action:")
    move_cursor(X, Y+1)
    for menu_line in display_menu:
        print(menu_line)
   
def take_input(X,Y,valid_list):
    '''
    This function takes the input key, corresponding to the options of display menu. It also validates input key.
    Input:
        - x (int): row number
        - y (int): column number
        - valid_list(list): contains a list of valid input keys corresponding to the options of display menu.
     Returns:
        - command(str): The input key opeation, that is to be performed is returned. This is selected from the valid_list. 
    '''

    not_valid=True
    move_cursor(X,Y)
    print('>> ', end='')
    move_cursor(X+3,Y)
    command=input().strip().lower()
    while not_valid:
        if command not in valid_list:
            move_cursor(X,Y)
            clear_line()
            print(ANSI["ER2"]+"Invalid menu option. Please choose a valid option from the Menu >> "+ANSI["RESET"], end="")
            move_cursor(X+67,Y)
            command=input().strip().lower()
            not_valid=True
        else:
            not_valid=False
    return command
    
def add_zero(X,Y):
    '''
    This function is used to add the first emoji symbol into the carousel.
    It adds the emoji charater into the carousel based on the emoji name input given by user.
    It adds the emoji character only after validation.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: NA
    '''
    global data
    global cdll
    global CDLL_CAPACITY
    not_valid=True
    move_cursor(X,Y)
    print('What do you want to add ? ')
    emoji_input=input().strip().lower()
    emoji_class, emoji_character=find_emoji_by_name(emoji_input)
    not_valid=validate_emoji_by_name(emoji_character)
    
    while not_valid:
        move_cursor(X,Y+1)
        clear_line()
        print(ANSI["ER2"]+"Invalid emoji name. Please enter a valid emoji name >> "+ANSI["RESET"],end="")
        move_cursor(X+55,Y+1)
        emoji_input=input().strip().lower()
        emoji_class, emoji_character=find_emoji_by_name(emoji_input)
        not_valid=validate_emoji_by_name(emoji_character)

        
    clear_screen()
    fun_bottom_frame()
    time.sleep(2)
    clear_screen()
    fun_main_single_frame()
    cdll=CircularDoublyLinkedList(CDLL_CAPACITY)
    cdll.add_at_beginning(emoji_character)
    move_cursor(X+29,Y)
    print(cdll.get_current())
    
def add_one_between(X,Y):
    '''
    This function is used to take the emoji name that is to be added into the carousel, when the carousel has one or more than one(subsequent) emoji characters in it.
    It also takes the position from main frame (left/right) where the emoji has to be added in the carousel. 
    It adds the emoji charater into the carousel based on the emoji name input given by user.
    It adds the emoji character only after validation.
    Input:
        - x (int): row number
        - y (int): column number
    Returns:
        - side (str): A string that suggest posiion (left/right) the emoji syambol has to be inserted.
        - emoji_character (str):The emoji character corresponding to the emoji name.
    '''
    global data
        
    not_valid=True
    move_cursor(X,Y)
    print('What do you want to add ? ')
    emoji_input=input().strip().lower()
    emoji_class, emoji_character=find_emoji_by_name(emoji_input)
    not_valid=validate_emoji_by_name(emoji_character)
    
    while not_valid:
        move_cursor(X,Y+1)
        clear_line()
        print(ANSI["ER2"]+"Invalid emoji name. Please enter a valid emoji name >> "+ANSI["RESET"],end="")
        move_cursor(X+55,Y+1)
        emoji_input=input().strip().lower()
        emoji_class, emoji_character=find_emoji_by_name(emoji_input)
        not_valid=validate_emoji_by_name(emoji_character)
        
    move_cursor(X,Y+2)
    print('Which side do you want to add ? (left/right:) ', end="")
    move_cursor(X+46,Y+2)
    side=input().strip().lower()
    not_valid=True
    while not_valid:
        if side not in ["left","right"]:
            move_cursor(X,Y+2)
            clear_line()
            print(ANSI["ER2"]+"Invalid side. Please enter either 'left' or 'right' >> "+ANSI["RESET"],end="")
            move_cursor(X+55,Y+2)
            side=input().strip().lower()
            not_valid=True
        else:
            not_valid=False

    return side,emoji_character 

def add_right_left_one(side,emoji_character,X,Y):
    '''
    This function is used to add the emoji character at the correct position (left/ right) when the carousel has only one emoji character in it. 
    It adds the emoji charater into the carousel based on the emoji name input given by user.
    It adds the emoji character only after validation.
    Input:
        - x (int): row number
        - y (int): column number
        - side (str): A string that suggest posiion (left/right) the emoji syambol has to be inserted.
        - emoji_character (str):The emoji character corresponding to the emoji name.
    Returns: NA
    '''
    global cdll
    Y=Y+2
    if side =="right":
        clear_screen()
        fun_adding_right_frame()
        time.sleep(2)
        
        clear_screen()
        fun_main_frame()
        cdll.add_right(emoji_character)
        
        set_left_right_frame_after(X,Y)
    else:
        clear_screen()
        fun_adding_left_frame()
        time.sleep(2)
        
        clear_screen()
        fun_main_frame()
        cdll.add_left(emoji_character)
        
        set_left_right_frame_after(X,Y)

def add_right_left_between(side, emoji_character, X,Y):
    '''
    This function is used to add the emoji character at the correct position (left/ right) when the carousel has more than one emoji character in it. 
    It adds the emoji charater into the carousel based on the emoji name input given by user.
    It adds the emoji character only after validation.
    Input:
        - x (int): row number
        - y (int): column number
        - side (str): A string that suggest posiion (left/right) the emoji syambol has to be inserted.
        - emoji_character (str):The emoji character corresponding to the emoji name.
    Returns: NA
    '''
    global cdll 
    if side =="right":
        clear_screen()
        fun_main_adding_right_frame()
        
        set_left_right_frame_before(X,Y) 
        cdll.add_right(emoji_character)            
        set_left_right_frame_after(X,Y)
        
    else:
        clear_screen()
        fun_main_adding_left_frame()
        
        set_left_right_frame_before(X,Y) 
        cdll.add_left(emoji_character)
        set_left_right_frame_after(X,Y)          

def del_one(X,Y):
    '''
    This function is used to del the emoji charcter from the carousel, when the carousel has only one emoji symbol in it.  
    Input:
        - x (int): row number
        - y (int): column number
    Returns: NA
    '''
    global cdll
    clear_screen()
    fun_up_frame()
    time.sleep(2)
    cdll.remove_current()
    clear_screen()

def del_between(X,Y):
    '''
    This function is used to del the emoji charcter from gthe carousel, when the carousel has more than one emoji symbol in it.  
    Input:
        - x (int): row number
        - y (int): column number
    Returns: NA
    '''
    global cdll
    clear_screen()
    fun_main_up_frame()
    
    previous_node=cdll.get_previous_node().data
    move_cursor(X+1,Y-14)
    print(previous_node)
    next_node=cdll.get_next_node().data
    move_cursor(X+57,Y-14)
    print(next_node)
    time.sleep(2)
    
    clear_screen()
    cdll.remove_current()
    
    if cdll.get_size()!=1:
        
        fun_main_frame()    
        set_left_right_frame_after(X,Y)
   
    else:
       fun_main_single_frame()
       move_cursor(X+29,Y-14)
       print(cdll.get_current())
 
def move_left(X,Y):
    '''
    This function is used to move the left emoji to the center frame. The operation is move left.   
    Input:
        - x (int): row number
        - y (int): column number
    Returns: NA
    '''
    global cdll
    clear_screen()
    fun_main_left_frame()
      
    set_left_right_frame_before(X,Y)
    cdll.go_left()
    set_left_right_frame_after(X,Y)
    
def move_right(X,Y):
    '''
    This function is used to move the right emoji to the center frame. The operation is move right.   
    Input:
        - x (int): row number
        - y (int): column number
    Returns: NA
    '''
    global cdll
    clear_screen()
    fun_main_right_frame()

    set_left_right_frame_before(X,Y)
    cdll.go_right()
    set_left_right_frame_after(X,Y)
   
def set_left_right_frame_before(X,Y):
    '''
    This function is used to set the left and right frame. The previous and next emojis from currect position is placed into the respective frame before the respective operation.
    This function is common for sll the operation.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: NA
    '''
    global cdll
    previous_node=cdll.get_previous_node().data
    move_cursor(X+1,Y-14)
    print(previous_node)
    next_node=cdll.get_next_node().data
    move_cursor(X+57,Y-14)
    print(next_node)

    time.sleep(2)
    clear_screen()
    fun_main_frame()
    
def set_left_right_frame_after(X,Y):
    '''
    This function is used to set the left and right frame. The previous and next emojis from currect position is placed into the respective frame after the respective operation.   
    This function is common for sll the operation.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: NA
    '''
    global cdll
    move_cursor(X+29,Y-14)
    print(cdll.get_current())
    
    previous_node=cdll.get_previous_node().data
    move_cursor(X+1,Y-14)
    print(previous_node)
    next_node=cdll.get_next_node().data
    move_cursor(X+57,Y-14)
    print(next_node)

def info(X,Y):
    '''
    This function is used to get the emoji class, emoji symbol/character and the emoji name of the emoji in the current frame.    
    Input:
        - x (int): row number
        - y (int): column number
    Returns: NA
    '''
    global data
    global cdll
    current=cdll.get_current()
    emoji_class, emoji_name=find_emoji_by_character(current)
    move_cursor(X,Y)
    print("Oject: ",emoji_name.capitalize())
    move_cursor(X,Y+1)
    print("Sym: ",current.capitalize())
    move_cursor(X,Y+2)
    print("Class: ",emoji_class.capitalize())
    move_cursor(X,Y+4)
    input(ANSI["ER1"]+"Click any button to continue: "+ANSI["RESET"])
    move_cursor(X,Y-1)
    clear_line()
    move_cursor(X,Y)
    clear_line()
    move_cursor(X,Y+1)
    clear_line()
    move_cursor(X,Y+2)
    clear_line()
    move_cursor(X,Y+4)
    clear_line()
   
def main():
    global YES_CONTINUE
    global cdll
    global CDLL_CAPACITY
    
    common()                            #sets the all art by calling common from art.py
    data=load_json()                    #load the list is dictionary from emojis.json
    cdll=CircularDoublyLinkedList(CDLL_CAPACITY)     #cirular doubly linked list assigned
    clear_screen()

    while YES_CONTINUE:
        
    #The add or q opearations are done when size is 0
        if cdll.get_size()==0:
            display_zero=["\t\tADD: Add an emoji frame", "\t\tQ: Quit the program"]
            display(XC,YC, display_zero)
            valid_list=["add",'q']
            command=take_input(XC,YC+3,valid_list)
            if command =='q':
                YES_CONTINUE=False
            else:
                add_zero(XC,YC+4)
                
        #All orperations are done except move left and move right when the size of carousel is 1
        elif cdll.get_size()==1:
            display_one=["\t\tADD: Add an emoji frame", "\t\tDEL: Delete current emoji frame","\t\tINFO: Retrive info about current emoji Frame","\t\tQ: Quit the program"]
            display(XC,YC+10,display_one)
            valid_list=["add",'q','del','info']
            command=take_input(XC,YC+15, valid_list)
            if command =='q':
                YES_CONTINUE=False
            elif command=="add":
                side, emoji_character=add_one_between(XC,YC+16)
                add_right_left_one(side, emoji_character, XC,YC+16)
            elif command=="info":
                info(XC,YC+16)
            elif command=="del":
                del_one(XC,YC+16)

        #All orperations are done except move left and move right when the size of carousel is between 2 and 4    
        elif cdll.get_size()>1 and cdll.get_size()< CDLL_CAPACITY:
            display_between=["\t\tL: Move left","\t\tR: Move right", "\t\tADD: Add an emoji frame", "\t\tDEL: Delete current emoji frame","\t\tINFO: Retrive info about current emoji Frame", "\t\tQ: Quit the program"]
            display(XC,YC+10,display_between)
            valid_list=["add",'q','del','info',"l","r"]
            command=take_input(XC,YC+17,valid_list)
            if command =='q':
                YES_CONTINUE=False
            elif command=="l":
                move_left(XC,YC+18)
            elif command=="r":
                move_right(XC,YC+18)    
            elif command=="info":
                info(XC,YC+18)
            elif command=="add":
                side, emoji_character=add_one_between(XC,YC+18)
                add_right_left_between(side, emoji_character, XC,YC+18)
            elif command=="del":
                del_between(XC,YC+18)
                
        #All orperations are done except add when the size of carousel has reached it maximum capacity
        elif cdll.get_size()== CDLL_CAPACITY:
            display_full= ["\t\tL: Move left", "\t\tR: Move right", "\t\tDEL: Delete current emoji frame", "\t\tINFO: Retrive info about current emoji Frame", "\t\tQ: Quit the program"]
            display(XC,YC+10,display_full)
            valid_list=['q','del','info',"l","r"]
            command=take_input(XC,YC+17,valid_list)
            if command =='q':
                YES_CONTINUE=False
            elif command=="l":
                move_left(XC,YC+18)
            elif command=="r":
                move_right(XC,YC+18)    
            elif command=="info":
                info(XC,YC+17)
            elif command=="del":
                del_between(XC,YC+18)
 
if __name__ == '__main__':
    main()


