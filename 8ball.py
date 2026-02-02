# magiczna kula generująca losowe odpowiedzi na pytania

import random

pytanie = input('Zadaj pytanie: ')

num = random.randint(1, 10)

if num == 1:
    odpowiedz = 'Zdecydowanie tak'
elif num == 2:
    odpowiedz = 'Prawdopodobnie tak'
elif num == 3:
    odpowiedz = 'Możliwe, że tak'
elif num == 4:
    odpowiedz = 'Nie wiem'
elif num == 5:
    odpowiedz = 'Nie wiem, ale może'
elif num == 6:
    odpowiedz = 'Nie, nie i jeszcze raz nie'
elif num == 7:
    odpowiedz = 'Zdecydowanie nie'
elif num == 8:
    odpowiedz = 'To nie jest dobre'
elif num == 9:
    odpowiedz = 'To bardzo złe'
else:
    odpowiedz = 'Bardzo złe'

print('Odpowiedź magicznej kuli: ' + odpowiedz)