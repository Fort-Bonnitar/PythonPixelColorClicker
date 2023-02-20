# Made by Fortbonnitar    Discord-  FORTBONNITAR#6584
# This is my first Python code written completely solo, that being said, theres probably some mistakes and ways to improve this code. Any notes are very welcome. Thanks!
# You are free to modify, use, and/or redistribute this code for any and all purposes, even commercial.
# Python 3.9.13
# APC (Auto Pixel Clicker) is a program that checks the color of pixels at given locations and if color matchs target color then it will auto click the pixel.
# I made this to work with the Magic Piano game  https://www.crazygames.com/game/magic-piano-tiles 






from pyautogui import * 
import time
import pyautogui 
import keyboard as kb
import win32api, win32con







# setting up default variables
first: Point = None
second: Point = None
third: Point = None
fourth: Point = None
target_color: list = None


# Returns Current Mouse Position As Point(THIS FUNCTION IS FOR TESTING PURPOSES, SO IT ISN'T CURRENTLY IMPLEMENTED)
def mouse_position_as_point() -> Point:
    """
    
    Gets the current postion of the mouse on the screen and returns it as a Point to be used to check for Target Color at
    """
    
    print('Press ENTER key to stop viewing the current mouse location as point')

    time.sleep(1.0)

    while kb.is_pressed('CTRL') == False:
        time.sleep(.1)
        x, y = pyautogui.position()
        r,g,b = pyautogui.pixel(x, y)
        print((x,y) + ":" + (r, g, b))

    
    

# Input First Mouse Position.
def input_first_point() -> Point:
    """
    Defines the first point to check in the piano tile rows for the target color
    """
    
    print('Press CTRL key to record mouse location as first')

    first = None

    while first == None:
        if kb.is_pressed('CTRL') == False:
            pass
            
        else:
            first = pyautogui.position()

    print('First point set to:')
    print(first)
    return first






# Input Second Mouse Position.
def input_second_point() -> Point:
    """
    
    defines second point of the corrisopnding piano tile row to click if target color detected
    """

    print('Press CTRL key to record mouse location as second')

    second: Point = None

    while second == None:
        if kb.is_pressed('CTRL') == False:
            pass
            
        else:
            second = pyautogui.position()

    print('Second point set to:')
    print(second)
    return second
    






# Input Third Mouse Position.
def input_third_point() -> Point:
    """
    
    defines third point of the corrisopnding piano tile row to click if target color detected
    """
    
    print('Press CTRL key to record mouse location as third')


    third: Point = None

    while third == None:
        if kb.is_pressed('CTRL') == False:
            pass
            
        else:
            third = pyautogui.position()


    print('Third point set to:')
    print(third)
    return third







# Input Fourth Mouse Position.
def input_fourth_point() -> Point :
    """
    
    defines fourth point of the corrisopnding piano tile row to click if target color detected
    """

    print('Press CTRL key to record mouse location as fourth')

    fourth: Point=None

    while fourth == None:
        if kb.is_pressed('CTRL') == False:
            pass
            
        else:
            fourth = pyautogui.position()

    print('Fourth point set to:')
    print(fourth)
    return fourth






# Set the target pixel color to check for all points.  
    
def set_target_pixel_color() -> list:
    """
    
    Sets the target color to check the pixels for, (promtps user to input values)
    """
    print('Press CTRL key to set color at mouse location as target color:  ')

    target_color = None

    while target_color == None:
        x, y = pyautogui.position()
        if kb.is_pressed('CTRL') == False:
            pass
            
        else:
            target_color = pyautogui.pixel(x, y)

    print('Target color set to :' + str(target_color))
    return target_color

    



# Sets the color variable
target_color = set_target_pixel_color



# Defines target color
def get_color(xy: Point) -> list:
    """
    
    Defines target color to search for
    """
    current_color = pyautogui.pixel(xy[0], xy[1])
    return current_color



# Defining Click Function
def click(selected_point: Point) -> None:
    """
    
    Clicks on given point on screen.
    """
    win32api.SetCursorPos(selected_point)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


      


# Starts settting the variables using the above functions
first: Point = input_first_point()

time.sleep(2.0)

second: Point = input_second_point()

time.sleep(2.0)

third: Point = input_third_point()

time.sleep(2.0)

fourth: Point = input_fourth_point()

time.sleep(2.0)

target_color: list = set_target_pixel_color()

time.sleep(2.0)


print('All Variables set, setting up clicking. Please wait......')

time.sleep(3.0)


#adding all points to a list
all_points: list = [first, second, third, fourth]



# prompt to press Enter when ready to start
print('Press ENTER to start auto-clicking.....')
while kb.is_pressed('ENTER') == False:
    pass


#delay
time.sleep(0.5)



# begin the auto_clicking
print('press q to stop auto-clicking')


while kb.is_pressed('q') == False:
    for each_point in all_points:
        if get_color(each_point) == target_color:
                click(each_point)
                print("clicked" + str(each_point))






    



    














        
    