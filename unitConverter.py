#Morgan Baughman
#9/28/17
#unitConverter.py - COnverting Units of stuff

print('choose a convertion.')
print('a) Kilotmeters to Miles')
print('b) Kilograms to Pounds')
print('c) Liters to Gallons.')
print('d) Celsius to Fahrenheit')
convertionopt = (input('choose a convertion: '))
value = float(input('Enter value: '))

a = value/0.621371
b = value/2.20462
c = value/0.264172
d = value/32

print('Kilotmeters to Miles' , a)
print('Kilograms to Pounds' , b)
print(value, 'Liters =', c ,'Gallons')
print( value, 'Celsius =', d, 'Fahrenheit' )