# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:19:49 2021

@author: user
"""

data = """
Dorathy:Shake:dorathy.shake@email.com:22:psource1-150x132.jpg
Felix:Student:felix.student@email.com:34:IMG_3954-150x132.jpg
Samella:Mccallie:samella.mccallieemail.com:23:DSC_0564b-64x150.png
Sherell:Noguera:sherell.noguera@email.com:26:DSC_0226-150x64.jpg
Irwin:Isaacson:irwin.isaacson@stxnext.pl:46:9-132x150.jpg
Keneth:Chesley:keneth.chesley@email.com:14:DSC_0601_640-132x150.jpg
Katie::katie.corson@email.com:61:IMG_3748@a64.jpg
Jenell:Cimmino:jenell.cim'mino@email.com:34:sky2-64x64.jpg
Candra:Ricciardi:candra.ricciardi@em/ail.com:33:110-1020-128x128.png
Christeen:Gangestad:christeen.gangestad@email.com:-24:109-0930-64x150.png
"""
# znajdz wszystkie poprawne emaile
# format poprawnego emaila: nazwa@domena
# nazwa i domena może mieć tylko znaki z zakresu: A-Za-z._0-9


stringi= data.split(':')

import re
 
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(string):
 
    # pass the regular expression
    # and the string in search() method
    if(re.match(regex, string)):
        print(string)

for str in stringi :
        check(str)
 