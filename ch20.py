import pyautogui
wh = pyautogui.size()
print(wh)

# Move to a specified position on the screen
# for i in range(10):
#     pyautogui.moveTo(100,100, duration=0.25)
#     pyautogui.moveTo(200,100, duration=0.25)
#     pyautogui.moveTo(200,200, duration=0.25)
#     pyautogui.moveTo(100,200, duration=0.25)


# Move a relative amount
# for i in range(10):
#     pyautogui.move(100,0,duration=0.25)
#     pyautogui.move(0,100,duration=0.25)
#     pyautogui.move(-100,0,duration=0.25)
#     pyautogui.move(0,-100,duration=0.25)

# Find mouse position
p = pyautogui.position()
print (p)

pyautogui.click(10,5)