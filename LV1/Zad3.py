# Zad 1.4.3

numbers = list()

while 1:
    try:
        temp = input('Unesi broj: ')
        if temp == 'Done':
            break
        numbers.append(float(temp))
    except:
        print('NaN')

print('Kolicina brojeva: ', len(numbers))
numbers.sort()
print(numbers)
print('Average: ', sum(numbers)/len(numbers))
print('Max: ', max(numbers))
print('Min: ', min(numbers))
