import pyautogui
import time

x1 = 250
y1 = 420

x2 = 276
y2 = 462

print("Le script démarre dans 10 secondes \n\nClique sur sea of thieves")
print("\nAppuyez sur 'Ctrl+C' pour arrêter le script.")
time.sleep(10)

n = 1
try:
    while True:
        pyautogui.press('esc')
        time.sleep(3)
        pyautogui.click(x=x1, y=y1, button='left', clicks=1)
        time.sleep(2)
        pyautogui.click(x=x2, y=y2, button='left', clicks=1)
        time.sleep(2)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('esc')
        print(f'\nNombre de refresh : {n}')
        time.sleep(50)
        n+=1
except KeyboardInterrupt:
    print("Script arrêté")

