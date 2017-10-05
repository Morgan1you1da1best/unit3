#Morgan Baughman
#10/5/17
#warmUp10.py

 
from ggame import *

red = Color(0xFF0000,1)
yellow = Color(0xFFCC33,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(200,50,blackOutline,red) #Width, height, outline, fill.
blackRectangle = RectangleAsset(200,50,blackOutline,black) #Width, height, outline, fill.
yellowRectangle = RectangleAsset(200,50,blackOutline,yellow) #Width, height, outline, fill.

for j in range(5): #prints the row 50 times
    for i in range(10): #prints one row of dots
        Sprite(blackRectangle, (200 + 300*i,50 + 250*j))
        Sprite(yellowRectangle, (200 + 300*i,150 +250*j))
        Sprite(redRectangle, (200 + 300*i,100 + 250*j))

App().run()