#Morgan Baughman
#10/17/17
#quiz3.py 

for i in range(-5,6):
    print(i)

i = 16
while i<=31:
    i = i + 2
    print(i)
    
total = 0
for i in range(13,332,2):
    total = total + i
print(total)

while True:
    word = input('Enter a word: ')
    if 'z' in word:
        break
