#python3 
import pyautogui
import time 

'''
sword merging simulator : https://www.crazygames.com/game/sword-merging-simulator
command to plan :


collect the orbs when 30/30 (click on the sword and left click to collect the orbs )
merge sword if possible

when orbs are not full, attack the monster by clicking on the skull 
attack the monster by clicking on it,

add sword at all time 


after 10 mins, rebirth : 
click on rebirth icon 
accept rebirth 
'''

def monsters_hunt(): 
    #while the screen thing is not 30/30 click on the monster
    #+ if sword icon is bright click on it
    bubble = pyautogui.locateCenterOnScreen('bubblemax.PNG', confidence=0.9)
    sword = pyautogui.locateCenterOnScreen('buysword.PNG', confidence=0.9)
    monster = pyautogui.locateCenterOnScreen('killthemonsters.PNG', confidence=0.9)
    while bubble == None: 
        if sword != None: 
            pyautogui.moveTo(sword)
            pyautogui.click()
        if sword == None: 
            x, y = pyautogui.position(monster)
            y = y -50
            pyautogui.moveTo(x, y)
            pyautogui.click()
    rebirth()

def swords_screen(): 
    print('sword screen')
    timer = time.time()
    p = pyautogui.locateCenterOnScreen('bubble.PNG', confidence=0.9)
    if p != None:
        x, y = pyautogui.position(p)
        y = y -200
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        myList = [(x+100, y), (x+100, y+40), (x-100, y+40), (x-100, y)]
        for i in myList : 
            pyautogui.moveTo(i)
    pyautogui.mouseUp()
    merge = pyautogui.locateCenterOnScreen('mergetheswords.PNG', confidence=0.9)
    if merge != None:
        pyautogui.moveTo(merge)
        pyautogui.click()
        time.sleep(2.5)
    now = time.time()
    if timer - now > 3:
        monsters_hunt()



    #collect the orbs
    #if merge icon is bright click on it
    #(+ if sword icon is bright click on it)
    #(after 2 seconds, go back to monster hunt)

    

def rebirth(): 
    print('rebirth')
    global counter 
    now = time.time()
    if (counter - now) > 600 : 
        x = pyautogui.locateCenterOnScreen('rebirthbutton.PNG', confidence=0.9)
        y = pyautogui.locateCenterOnScreen('rebirthtool.PNG', confidence=0.9)
        z = pyautogui.locateCenterOnScreen('yesbutton.PNG', confidence=0.9)
        pyautogui.moveTo(x)
        pyautogui.click()
        pyautogui.moveTo(y)
        pyautogui.click()
        pyautogui.moveTo(z)
        pyautogui.click()
    #if time.time - x > 600 
    #rebirth and follow instructions 
    

    swords_screen()

if __name__ == "__main__":
    pyautogui.confirm('run?')
    counter = time.time()
    rebirth()