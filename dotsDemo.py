#Morgan Baughman
#10/5/17
#dotsdemo.py

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color


dot = CircleAsset(20,blackOutline,red) #Radius, outline, fill.

for i in range(10):
    Sprite(dot,(50 + 100*i ,50))
App().run()

