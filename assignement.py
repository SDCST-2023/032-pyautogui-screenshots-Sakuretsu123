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
    print('sword screen')
    pyautogui.alert('sword screen')
    m,n = pyautogui.locateCenterOnScreen('mainscreen.PNG', confidence = 0.9)
    

    pyautogui.moveTo(m,n)
    pyautogui.click()
    
    x, y = pyautogui.locateCenterOnScreen('bubble.PNG', confidence=0.8)
    pyautogui.alert(f"{x} {y}")

    pyautogui.moveTo(x-350,y)
    pyautogui.mouseDown()

    myList = [(x-190, y), (x-190, y+40), (x-500, y+40), (x-500, y)]

    for i in myList : 
        pyautogui.moveTo(i, duration = 0.5)
        

    pyautogui.mouseUp()

    merge = pyautogui.locateCenterOnScreen('mergetheswords.PNG', confidence=0.9)
    p, l = pyautogui.locateCenterOnScreen('buysword.PNG', confidence=0.9)
    
    if merge != None:
        pyautogui.moveTo(merge)
        pyautogui.click()
        pyautogui.moveTo(p +50, l)
        pyautogui.click(clicks = 5, duration= 1)
    
        
    
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


    rebirth()



    #collect the orbs
    #if merge icon is bright click on it
    #(+ if sword icon is bright click on it)
    #(after 2 seconds, go back to monster hunt)

    

def rebirth(): 
    i= 0
    i = i + 1
    if i == 1 :
        count = time.time()

    print('rebirth')
    now = time.time()
    if (count - now) > 5 : 
        x = pyautogui.locateCenterOnScreen('rebirthbutton.PNG', confidence=0.8)
        y = pyautogui.locateCenterOnScreen('rebirthtool.PNG', confidence=0.8)
        z = pyautogui.locateCenterOnScreen('yesbutton.PNG', confidence=0.8)
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
    
    while True:
        rebirth()