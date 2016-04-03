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
        "returns True if test postalcode is a plausible code, not if it is an actual code"
        first=self.code.split()[0]
        try:
            last=self.code.split()[1]
        except IndexError:
            if len(self.code)>3:
                last=self.code[-3:]
            else:
                last=''
        lenfirst=len(first)
        if not (first.isalnum() and last.isalnum()):
            #return 1
            return False
        if len(last)!=3:
            #return 2
            return False
        if not (last[0].isdigit() and last[1].isalpha() and last[2].isalpha()):
                    #return 3
                    return False
        elif re.search('[^CIKMOV]', last[1]) is None or re.search('[^CIKMOV]', last[2]) is None:
                 #return 4
                 return False
        else:
            if lenfirst<2 or lenfirst>4:
                #return 5
                return False
            if first[0].isdigit():
                #return 6
                return False
            if lenfirst==2:
                if re.search('[BEGLMNSW]',first[0]) is None:
                    #return 7
                    return False
                elif first[1].isalpha():
                    #return 8
                    return False
                else:
                    return True
            if lenfirst==3:
                if re.search('[^QVX]', first[0]) is None:
                    #return 9
                    return False
                elif first[1].isalpha():
                    if re.search('[^IJZ]', first[1]) is None:
                        #return 10
                        return False
                    elif first[2].isalpha():
                        return False
                    else:
                        return True
                elif first[2].isalpha():
                    if re.search('[ABCDEFGHJKSTUW]', first[2]) is None:
                        #return 11
                        return False
                    return True
                else:
                    return True
            else:
                if re.search('[^QVX]', first[0]) is None:
                    #return 12
                    return False
                elif first[1].isdigit():
                    #return 13
                    return False
                elif re.search('[^IJZ]', first[1]) is None:
                    #return 14
                    return False
                if first[2].isalpha():
                    #return 15
                    return False
                elif first[3].isalpha():
                    if re.search('[ABEHMNPRVWXY]',first[3]) is None:
                        #return 16
                        return False
                    else:
                        return True
                else:
                    #return 9000
                    return True
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
        
