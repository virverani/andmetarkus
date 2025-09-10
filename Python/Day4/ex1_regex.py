# First exercise - find specific numbers

text_to_analyze = 'Minu kontonumber on 345678, aga vana konto oli 312345. Mõned näited, mida ei tohiks leida: 234567, 34567, 33445566, 39876, 399999, 3123457, 31234. Samuti on olemas 398765 ja 300001.'

import re

numbers_starting_with_3_and_len_6 = re.findall(r'\b3\d{5}\b', text_to_analyze)
print(numbers_starting_with_3_and_len_6)

# Second exercise - replace enter with space
text_to_analyze2 = """See on esimene rida.
See on teine rida.
Kolmas rida on siin.
Neljandal real on samuti tekst."""

replace_enters = re.sub(r'\n', ' ', text_to_analyze2)
print(replace_enters)