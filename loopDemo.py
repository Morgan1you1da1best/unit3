#Morgan Baughman
#9/27/17
#loopDemo.py - how to use loops

"""
#print I love computer science 5 times
for i in range(0,5):
    print('I love computer science')
"""
"""
i = 1
while i <= 5:
    print('I love computer science')
    i = i+1
"""
"""
#print the numbers from 1 to 20
for i in range(1,21):
    print(i**3)
"""
"""
i = 1
while i <=20:
    print(i)
    i = i +1"""
"""
#print out the off numbers from 13 to 27
for i in range(13,28,2): #(starting number, ending number-1, number it goes up by)
    print(i)
"""
"""
#add up the numbers 1 to 5
total = 0
for i in range(1,6):
    total = total + i 
print(total)"""

total = 0
i = 0
while i <=5:
    total = total + i 
    i = i+1 #i+=1 is the same as i + i+1
print(total)
