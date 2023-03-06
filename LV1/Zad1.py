# Zad 1.4.1

radniSati = int(input('Radni sati: '))
satnica = float(input('Satnica: '))
print('Ukupno:', radniSati*satnica, 'eura')


def total_euro(sati, cijenaSata):
    return sati*cijenaSata


radniSati = int(input('Radni sati: '))
satnica = float(input('Satnica: '))
print('Ukupno:', total_euro(radniSati, satnica), 'eura')
