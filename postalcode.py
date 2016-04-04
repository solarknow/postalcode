# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 08:42:25 2016
This module presents validation and formatting of post codes for UK
@author: Mihir Sarwade
"""
import re, itertools

class postalcode(object):
    
    def __init__(self,code):
        self.code=code.upper()
    def __str__(self):
        return "Postal Code: "+self.code
    def isPlausible(self):
        "Returns True if test postalcode is a plausible code, not if it is an actual code"
        ##Initial Processing
        first=self.code.split()[0]

        try:
            last=self.code.split()[1]
        except IndexError:
            if len(self.code)>3:
                last=self.code[-3:]
            else:
                last=''

        lenfirst=len(first)
        ##Tests if code is alphanumeric 
        if not (first.isalnum() and last.isalnum()):
            return False
        
        ##Tests associated with the inward code
        if len(last)!=3: #Length
            return False
        if not (last[0].isdigit() and last[1].isalpha() and last[2].isalpha()):  #Format
                    return False
        elif re.search('[^CIKMOV]', last[1]) is None or re.search('[^CIKMOV]', last[2]) is None: #Letter choice
                 return False
        ##Tests associated with the outward code
        else:
            if lenfirst<2 or lenfirst>4: #Length
                return False
            if first[0].isdigit(): #Format: First character is always alpha
                return False
            #Tests for length 2 outward code
            if lenfirst==2:
                if re.search('[BEGLMNSW]',first[0]) is None: #Letter Choice
                    return False
                elif first[1].isalpha(): #Format: Second character is numeric
                    return False
                else: #Code is plausible
                    return True
            #Tests for length 3 outward code
            if lenfirst==3: #Length
                if re.search('[^QVX]', first[0]) is None: #Letter Choice
                    return False
                elif first[1].isalpha(): #Format: Second character can be either alphabetical or numeric
                    if re.search('[^IJZ]', first[1]) is None: #Letter Choice
                        return False
                    elif first[2].isalpha(): #Format: If second character is alpha, third MUST be numeric
                        return False
                    else:
                        return True #Code is plausible
                elif first[2].isalpha(): #Format: If second character is numerical, third character can be either alpha or numeric
                    if re.search('[ABCDEFGHJKSTUW]', first[2]) is None: #Letter Choice
                        return False
                    return True #Code is plausible
                else: #Format: Third character is numerical
                    return True #Code is plausible
            #Tests for length 4 outward code
            else: #Length
                if re.search('[^QVX]', first[0]) is None: #Letter Choice
                    return False
                elif first[1].isdigit(): #Format: Second character MUST be alpha
                    return False
                elif re.search('[^IJZ]', first[1]) is None: #Letter Choice
                    return False
                if first[2].isalpha(): #Format: third character MUST be numeric
                    return False
                elif first[3].isalpha(): #Format: fourth character can be either alpha or numeric
                    if re.search('[ABEHMNPRVWXY]',first[3]) is None: #Letter Choice
                        return False
                    else: #Format: fourth character is numeric
                        return True #Code is plausible
                else:
                    return True #Code is plausible
    def getCode(self):
        "Returns postal code"
        return self.code
    def getOutwardCode(self):
        "Returns postal outward code"
        return self.code.split()[0]
    def getInwardCode(self):
        "Returns postal inward code"
        return self.code.split()[1]
    def getArea(self):
        "Returns postal code area"
        oc=self.getOutwardCode()
        return "".join(itertools.takewhile(str.isalpha, oc))
    def getDistrict(self):
        "Returns postal district"
        return self.getOutwardCode()
    def getSector(self):
        "Returns postal sector"
        return ' '.join([self.getDistrict(),self.getInwardCode()[0]])
        
