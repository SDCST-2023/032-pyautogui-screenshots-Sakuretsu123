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


def swords_screen(): 
    time.sleep(1)
    print('sword screen')
    m,n = pyautogui.locateCenterOnScreen('mainscreen.PNG', confidence = 0.9)
    

    pyautogui.moveTo(m,n)
    pyautogui.click()
    
    x, y = pyautogui.locateCenterOnScreen('bubble.PNG', confidence=0.8)
    

    pyautogui.moveTo(x-350,y)
    pyautogui.mouseDown()

    myList = [(x-190, y), (x-190, y+40), (x-500, y+40), (x-500, y)]

    for i in myList : 
        pyautogui.moveTo(i, duration = 0.3)
        

    pyautogui.mouseUp()

    merge = pyautogui.locateCenterOnScreen('mergetheswords.PNG', confidence=0.9)
    p, l = pyautogui.locateCenterOnScreen('buysword.PNG', confidence=0.9)
    
    if merge != None:
        pyautogui.moveTo(p +50, l)

        pyautogui.click()
        time.sleep(0.1)
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()

        pyautogui.moveTo(merge)
        pyautogui.click()
    
        
    
    monsters_hunt()

def monsters_hunt(): 
    #while the screen thing is not 30/30 click on the monster
    #+ if sword icon is bright click on it
    print('monster-screen')
    

    m,n = pyautogui.locateCenterOnScreen('monsterscreen.PNG', region=(420,470,580,625), confidence = 0.8)
    countdown = 0
    

    pyautogui.moveTo(m,n)
    pyautogui.click()

    x, y  = monster = pyautogui.locateCenterOnScreen('killthemonster.PNG', confidence=0.9)

    while countdown != 10: 
        countdown += 1
        if monster != None: 
            pyautogui.moveTo(x +100, y)
            pyautogui.click(clicks = 700)
    time.sleep(1.2)


    rebirth()



    #collect the orbs
    #if merge icon is bright click on it
    #(+ if sword icon is bright click on it)
    #(after 2 seconds, go back to monster hunt)
def counting(): 
    global count 
    count = time.time()
    

def rebirth(): 

    print('rebirth')
    now = time.time()
    if (now - count) > 120 : 
        time.sleep(15)
        x, y = pyautogui.locateCenterOnScreen('rebirthtool.PNG' , confidence=0.9)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        l, m = pyautogui.locateCenterOnScreen('rebirthbutton.PNG',  confidence=0.9)
        pyautogui.moveTo(l, m)
        pyautogui.click()
        o, p = pyautogui.locateCenterOnScreen('yesbutton.PNG', confidence=0.9)
        pyautogui.moveTo(o, p)
        pyautogui.click()
        counting()

    #if time.time - x > 600 
    #rebirth and follow instructions 
    

    swords_screen()


if __name__ == "__main__":
    counting()
    pyautogui.confirm('run?')
    
    while True:
        rebirth()
        