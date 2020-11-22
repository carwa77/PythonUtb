#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ett program som var multiplikation
# Antingen välja en tabell eller slumpa båda

# slumpa ett tal
import random 
tal1=random.randint(1,9)
print(tal1)

tal2=random.randint(1,9)
print(tal2)


# Skriv ut talet
tal3 = tal1*tal2
print('vad äee'+str(43)+'vad tysan åör' +str(1000))
print('åäö')
# Läs in svaret
tal4 = int(input("Svar?"))
if tal4 == tal3:
    print('Rätt')
else:
    print('fel')
