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
    def isPlausible(test):
        "returns True if test postalcode is a plausible code, not if it is an actual code"
        first=test.split()[0]
        last=test.split()[1]
        lenfirst=len(first)
        if not (first.isalnum() and last.isalnum()):
            return False
        if len(last)!=3:
            return False
        if not (last[0].isdigit() and last[1].isdigit() and 
                last[2].isdigit()):
                    return False
        elif re.search('[^CIKMOV]', last[1]) is None or re.search('[^CIKMOV]', last[2]) is None:
                 return False
        else:
            if lenfirst<2 or lenfirst>4:
                return False
            if first[0].isdigit():
                return False
            if lenfirst==2:
                if re.search('[BEGLMNSW]',first[0]) is None:
                    return False
                elif not first[1].isdigit():
                    return False
            if lenfirst==3:
                if re.search('[^QVX]', first[0]) is None:
                    return False
                if not first[1].isdigit():
                    if re.search('[^IJZ]', first[1]) is None or not first[2].isdigit():
                        return False
                elif not first[2].isdigit():
                    if re.search('[ABCDEFGHJKSTUW]', first[2]) is None:
                        return False
            else:
                if re.search('[^QVX]', first[0]) is None:
                    return False
                if first[1].isdigit():
                    return False
                elif re.search('[^IJZ]', first[1]) is None:
                        return False
                if not first[2].isdigit():
                    return False
                elif not first[3].isdigit():
                    if re.search('[ABEHMNPRVWXY]',first[3]) is None:
                        return False
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
        return "".join(itertools.takewhile(not str.isdigit, oc))
    def getDistrict(self):
        "Returns postal district"
        return self.getOutwardCode()
    def getSector(self):
        "Returns postal sector"
        return ' '.join([self.getDistrict(),self.getInwardCode[0]])
        