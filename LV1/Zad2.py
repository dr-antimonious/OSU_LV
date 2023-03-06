# Zad 1.4.2

try:
    ocjena = float(input('Ocjena: '))
    if ocjena < 0.0 or ocjena > 1.0:
        print('Izvan intervala')
    elif ocjena >= 0.9:
        print('A')
    elif ocjena >= 0.8:
        print('B')
    elif ocjena >= 0.7:
        print('C')
    elif ocjena >= 0.6:
        print('D')
    elif ocjena < 0.6:
        print('F')

except:
    print('NaN')
