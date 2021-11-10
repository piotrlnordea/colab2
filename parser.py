# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:29:56 2021

@author: piotr
"""

import tika
import re
from tika import parser

from collections import OrderedDict

#parsed = parser.from_file('templ2.docm')
#parsed = parser.from_file('gcop1.pdf')

filename='templ1.docm'


parsed = parser.from_file(filename)
print(parsed["metadata"])
print(parsed["content"])

cv1=parsed["content"]
cv1m=parsed["metadata"]
Fields=OrderedDict()
def cleaned(resumeText):
    resumeText1=resumeText.strip()
    resumeText2 = re.sub(' +', ' ', resumeText1)  # remove extra whitespace
    
    line_list = resumeText2.split("\n")


    number_of_lines = len(line_list)
    print("lines in cv",number_of_lines) 
    
    
    
    for line in line_list:
        res = re.split('[;,\s]+', line)
  
    
    return resumeText2

cv1c =  cleaned(cv1)
print(cv1c)
line_list = cv1c.split("\n")
print("search")
for line in line_list:
        if 'ITSM tool ticket number' in line:
            Fields['ITSMttn'] = line_list[line_list.index(line)+1].strip()
        if 'Business area' in line:
                Fields['Business_ares'] = line_list[line_list.index(line)+1].strip()
        if 'IT initiative' in line:
            if line_list.index(line) <18 :           
                Fields['IT_initiative'] = line_list[line_list.index(line)+1].strip()
        if 'Date' in line:
            if line_list.index(line) <18 :
                Fields['Date'] = line_list[line_list.index(line)+1].strip()

        if 'Release Test Plan ' in line:
            if line_list.index(line) <26 :
                Fields['RTP'] = line_list[line_list.index(line)+1].strip()
                Fields['RTP_ver'] = line_list[line_list.index(line)+2].strip()
                
        if 'Approval date' in line:
             if line_list.index(line) <44 :
                 Fields['Appr-date'] = line_list[line_list.index(line)+5].strip()
                 Fields['Appr-role'] = line_list[line_list.index(line)+6].strip()               
                 Fields['Appr-name'] = line_list[line_list.index(line)+8].strip() 
                 
                 
        if 'Document history' in line:
              if line_list.index(line) <50:
                  Fields['Doc_Ver'] = line_list[line_list.index(line)+6].strip()
                  Fields['Doc_Date'] = line_list[line_list.index(line)+7].strip()               
                  Fields['Doc_Auth'] = line_list[line_list.index(line)+8].strip() 
                  Fields['Doc_Desc'] = line_list[line_list.index(line)+9].strip()
                 
                 
                 
                 
print("*******************")           
for key, value in Fields.items():
    print(key, value)            