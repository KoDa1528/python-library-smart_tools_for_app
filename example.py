# adding library
from smart_tools_for_app import *

window(600, 400)

btn = button(10, 10, 100, 50)

running = True
while running:
    print("App is running... press Ctrl+C to stop")
    if touch_on_button(btn):
        running = False

close_window()