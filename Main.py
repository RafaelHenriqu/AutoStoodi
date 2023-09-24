import pyautogui as p #Importando o pyautogui 
min=0.5
max=1

def loop():
    p.click(1584,953,duration=max)

p.click(832,326,duration=max)
p.click(997,207,duration=max)
for i in range(0,10):
    loop()




