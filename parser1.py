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
filename='templ1.pdf'
filename='templ2.docm'
    
parsed = parser.from_file(filename)
print(parsed["metadata"])
print(parsed["content"])

cv1=parsed["content"]
cv1m=parsed["metadata"]
#Fields=OrderedDict()

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

def parsepdf(line_list):
    Fields=OrderedDict()
    for line in line_list:
            if 'ITSM tool ticket number' in line:
                s='ITSM tool ticket number'
                len1=len(s)
                r=line.rfind(s)
                Fields['ITSMttn'] = line[-r+len1:].strip()
            if 'Business area' in line:
                s='Business area'
                len1=len(s)
                r=line.rfind(s)
                Fields['Business_ares'] =line[-r+len1:].strip()
            if 'IT initiative' in line:
                if line_list.index(line) <18 :  
                    s='IT initiative'
                    len1=len(s)
                    r=line.rfind(s)
                    Fields['IT_initiative'] = line[-r+len1:].strip()
            if 'Date' in line:
                if line_list.index(line) <18 :
                    s='Date'
                    len1=len(s)
                    r=line.rfind(s)
                    
                    Fields['Date'] = line[-r+len1:].strip()
    
            if 'Release Test Plan' in line:
                if line_list.index(line) <26 :
                    r=line.rfind('Release Test Plan')
                    Fields['RTP'] = line_list[line_list.index(line)+1].strip()
                    Fields['RTP_ver'] = line_list[line_list.index(line)+3].strip()
                    
            if 'Approval date' in line:
                 if line_list.index(line) <44 :
                     x=line_list[line_list.index(line)+2].split()
                     Fields['Appr-date'] = x[0]
                     Fields['Appr-role'] = x[1:]   
                     x=line_list[line_list.index(line)+5].strip()
                     Fields['Appr-name'] = x
                     
                     
            if 'Document history' in line:
                  if line_list.index(line) <50:
                      Fields['Doc_Ver'] = line_list[line_list.index(line)+6].strip()
                      Fields['Doc_Date'] = line_list[line_list.index(line)+7].strip()               
                      Fields['Doc_Auth'] = line_list[line_list.index(line)+8].strip() 
                      Fields['Doc_Desc'] = line_list[line_list.index(line)+9].strip()
    return Fields     

def parsedocm(line_list):
    Fields=OrderedDict()
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
    return Fields       
                     

if filename.endswith('.docm'):
    Fields1=parsedocm(line_list)
elif filename.endswith('.pdf'):
    Fields1=parsepdf(line_list)

                 
                 
print("*******************")           
for key, value in Fields1.items():
    print(key, value)            