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
for j in range(50): #prints the row 50 times
    for i in range(50): #prints one row of dots
        Sprite(dot,(50 + 50*i ,50 + 50*j))
App().run()

