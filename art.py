#Define global list for all the 11 arts 
main_frame=[]
main_single_frame=[]
main_up_frame=[]
up_frame=[]
main_right_frame=[]
main_adding_right_frame=[]
adding_right_frame=[]
main_left_frame=[]
main_adding_left_frame=[]
adding_left_frame=[]          
bottom_frame=[]

def common():
    counter=0
    #The encoding="utf-8" parameter is used while reading the file to ensure that the text in the file is interpreted correctly.
    f=open("art.txt",'r',encoding="utf-8")          
    data=f.readline()
    
    while data !="":
        
    #strip the line to delete all white spaces
        data=data.rstrip()
        
    #Here """ serves as a seperatore between two different art forms       
        if data=='"""':
            counter+=1
            data=f.readline()
      
            l=len(data) - len(data.lstrip())
            data=data.strip()
            data=l*" "+data
            
     #Append the arts to their respective list. Here counter keeps track and serves as a seperator between two diffent art forms.   
        if counter ==1:
            main_frame.append(data)
        elif counter ==3:
            main_single_frame.append(data)
        elif counter ==5:
            main_up_frame.append(data)
        elif counter ==7:
            up_frame.append(data)
        elif counter ==9:
            main_right_frame.append(data)
        elif counter ==11:
            main_adding_right_frame.append(data)
        elif counter ==13:
            adding_right_frame.append(data)
        elif counter ==15:
            main_left_frame.append(data)
        elif counter ==17:
            main_adding_left_frame.append(data)
        elif counter ==19:
            adding_left_frame.append(data)               
        elif counter ==21:
            bottom_frame.append(data)
        data=f.readline()
    f.close()

#Each function displays the art form desired list. By calling these functions in the carousel program, the frames are set.
def fun_main_frame():
   for art in main_frame:
       print(art)
        
def fun_main_single_frame():
   for art in main_single_frame:
        print(art)
        
def fun_main_up_frame():
    for art in main_up_frame:
        print(art)
        
def fun_up_frame():
    for art in up_frame:
        print(art)
        
def fun_main_right_frame():
    for art in main_right_frame:
        print(art)
        
def fun_main_adding_right_frame():
    for art in main_adding_right_frame:
        print(art)
        
def fun_adding_right_frame():
    for art in adding_right_frame:
        print(art)
        
def fun_main_left_frame():
    for art in main_left_frame:
        print(art)
        
def fun_main_adding_left_frame():
    for art in main_adding_left_frame:
        print(art)
        
def fun_adding_left_frame():

    for art in adding_left_frame:
        print(art)
        
def fun_bottom_frame():

    for art in bottom_frame:
        print(art)



