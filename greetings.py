
#greetings Script 
def main():
    print('Hello World')

if __name__ == '__main__':
    main()

#input/output
name = 'Jordan'
age = '29'

print('Very nice to meeet you! My name is', name, 'and I am', age, 'years old')

#Formatted string literals 
print(f'Very nice to meet you, {name}!')

#uppercase 
print(f'{name.upper()}, are you {age}?')

#str.format()
print('howdy do, {}!'.format(name))

#expressions 
sum_of_two_numbers = 4 + 2 
print(sum_of_two_numbers)

#casting
temp = str(97.5)
print(type(temp))

#if 
score = 80

if score >= 80:
    print('you passed')

#else 
score1 = 70 

if score1 >= 80:
    print('you passed') 
else: 
    print('you didnt pass')

#elif
score3 = 60

if score3 >= 80: 
    print('good job, you passed.')
elif score3 > 65:
    print('yohu passed, but barely.')
else:
    print('you failed.')

#Loops
nums = [1,2,3,4,5]

for num in nums:
    print(num + 1)

#for loops in range()
for i in range(3):
    print(i)

#Nested for loops 
teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
    for name in team:
        print(name)

#While Loops 
i = 1 
while i < 6:
    print(i)
    i += 1

#duplicate prints
for r in range(10):
    print('welcome')