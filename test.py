# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:57:36 2016

@author: sarwamih
"""
import unittest, string, random, re
from postalcode import postalcode

class TestPostCode(unittest.TestCase):
    num_iter=100
    def test_short_codes_without_space(self,n=num_iter):
        "Tests isPlausible with n short alphanumeric codes without expected space char i.e. len(codes)<6"
        charset=list(string.ascii_uppercase+string.digits)
        for _ in range(n):
            for i in range(1,6):
                p=postalcode(''.join(random.sample(charset,i)))
                self.assertFalse(p.isPlausible())
    def test_short_codes_with_space(self,n=num_iter):
        "Tests isPlausible with n short alphanumeric codes with expected space char i.e. len(codes)<6"
        charset=list(string.ascii_uppercase+string.digits)
        for _ in range(n):
            for i in range(1,5):
                code=random.sample(charset,i)
                if i>=2:
                    code+=' '
                    random.shuffle(code)
                p=postalcode(''.join(code))                    
                self.assertFalse(p.isPlausible())                
    def test_long_codes_without_space(self,n=num_iter):
        "Tests isPlausible with n long alphanumeric codes without expected space char i.e. len(codes)>8 but <16"
        charset=list(string.ascii_uppercase+string.digits)
        for _ in range(n):
            for i in range(9,16):
                p=postalcode(''.join(random.sample(charset,i)))
                self.assertFalse(p.isPlausible())
    def test_long_codes_with_space(self,n=num_iter):
        "Tests isPlausible with n long alphanumeric codes with expected space char i.e. len(codes)>8 but <16"
        charset=list(string.ascii_uppercase+string.digits)
        for _ in range(n):
            for i in range(8,15):
                code=random.sample(charset,i)
                code+=' '
                random.shuffle(code)
                p=postalcode(''.join(code))                 
                self.assertFalse(p.isPlausible())
    def test_plausible_len_alphacodes_without_space(self,n=num_iter):
        "Tests isPlausible with n plausible length alpha codes without expected space char i.e. len(codes)>5 but <9"
        charset=list(string.ascii_uppercase)
        for _ in range(n):
            for i in range(6,9):
                p=postalcode(''.join(random.sample(charset,i)))
                self.assertFalse(p.isPlausible())
    def test_plausible_len_alphacodes_with_space(self,n=num_iter):
        "Tests isPlausible with n plausible length alpha codes with expected space char i.e. len(codes)>5 but <9"
        charset=list(string.ascii_uppercase)
        for _ in range(n):
            for i in range(5,8):
                code=random.sample(charset,i)
                code+=' '
                random.shuffle(code)
                p=postalcode(''.join(code))                   
                self.assertFalse(p.isPlausible()) 
    def test_plausible_len_numcodes_without_space(self,n=num_iter):
        "Tests isPlausible with n plausible length numeric codes without expected space char i.e. len(codes)>5 but <9"
        charset=list(string.digits)
        for _ in range(n):
            for i in range(6,9):
                p=postalcode(''.join(random.sample(charset,i)))
                self.assertFalse(p.isPlausible())
    def test_plausible_len_numcodes_with_space(self,n=num_iter):
        "Tests isPlausible with n plausible length numeric codes with expected space char i.e. len(codes)>5 but <9"
        charset=list(string.digits)
        for _ in range(n):
            for i in range(5,8):
                code=random.sample(charset,i)
                code+=' '
                random.shuffle(code)
                p=postalcode(''.join(code))                    
                self.assertFalse(p.isPlausible())
    def test_plausible_format_alphacodes(self,n=num_iter):
        "Tests isPlausible with n plausible length alpha codes with expected space char i.e. code mirrors: AA AAA or AAA AAA or AAAA AAA"
        charset=list(string.ascii_uppercase)
        for _ in range(n):
            for i in range(6,9):
                p=postalcode(' '.join([''.join(random.sample(charset,i-4)),''.join(random.sample(charset,3))]))
                self.assertFalse(p.isPlausible())
    def test_plausible_format_numcodes(self,n=num_iter):
        "Tests isPlausible with n plausible length num codes with expected space char i.e. code mirrors: 11 111 or 111 111 or 1111 111"
        charset=list(string.digits)
        for _ in range(n):
            for i in range(6,9):
                p=postalcode(' '.join([''.join(random.sample(charset,i-4)),''.join(random.sample(charset,3))]))
                self.assertFalse(p.isPlausible())
    def test_plausible_format_alternate_subcodes_alphanumcodes(self,n=num_iter):
        "Tests isPlausible with n plausible length codes with expected space char, with alternating subcodes between numeric and alpha i.e. code mirrors: 11 AAA or AAA 111 or 1111 AAA, etc"
        charset1=list(string.ascii_uppercase)
        charset2=list(string.digits)
        for _ in range(n):
            direction=random.random()<0.5
            for i in range(6,9):
                if direction:
                    p=postalcode(' '.join([''.join(random.sample(charset1,i-4)),
                                           ''.join(random.sample(charset2,3))]))
                else:
                    p=postalcode(' '.join([''.join(random.sample(charset2,i-4)),
                                           ''.join(random.sample(charset1,3))]))
                self.assertFalse(p.isPlausible())
    def test_plausible_format_alternate_chars_alphanumcodes(self,n=num_iter):
        "Tests isPlausible with n plausible length codes with expected space char, with alternating chars between numeric and alpha i.e. code mirrors: 1A 1A1 or A1A 1A1 or A1A1 A1A, etc"
        charset1=list(string.ascii_uppercase)
        charset2=list(string.digits)
        for _ in range(n):
            direction=random.random()<0.5
            for i in range(6,9):
                if direction:
                    code=''
                    for j in range(i):
                        if j%2==0:
                            code+=random.sample(charset1,1)[0]
                        else:
                            code+=random.sample(charset2,1)[0]
                    p=postalcode(code)
                else:
                    code=''
                    for j in range(i):
                        if j%2==0:
                            code+=random.sample(charset2,1)[0]
                        else:
                            code+=random.sample(charset1,1)[0]
                    p=postalcode(code)
                self.assertFalse(p.isPlausible())
    def test_plausible_format_len2_outward(self,n=num_iter):
        "Tests isPlausible with n plausible codes with length 2 outward code in proper format, using appropriate character sets"
        pos1=list('BEGLMNSW')
        dig=list(string.digits)
        posin23=re.findall('[^CIKMOV]',string.ascii_uppercase)   
        for _ in range(n):
            p=postalcode(' '.join(
            [''.join([random.sample(pos1,1)[0],random.sample(dig,1)[0]]),
             ''.join([random.sample(dig,1)[0],''.join(random.sample(posin23,2))])]
             ))
            self.assertTrue(p.isPlausible())
    def test_plausible_format_len3_outward(self,n=num_iter):
        "Tests isPlausible with n plausible codes with length 3 outward code in proper format, using appropriate character sets"
        pos1=re.findall('[^QVX]',string.ascii_uppercase)
        pos2=re.findall('[^IJZ]',string.ascii_uppercase)
        pos3=list('ABCDEFGHJKSTUW')
        dig=list(string.digits)
        posin23=re.findall('[^CIKMOV]',string.ascii_uppercase)
        for _ in range(n):
            code=random.sample(pos1,1)[0]+random.sample(pos2,1)[0]
            if code[1].isalpha():
                code+=random.sample(dig,1)[0]
            else:
                code+=random.sample(pos3+dig)
            code=' '.join([code,
                           ''.join([random.sample(dig,1)[0],
                                    ''.join(random.sample(posin23,2))])])
            p=postalcode(code)
            self.assertTrue(p.isPlausible())
    def test_plausible_format_len4_outward(self,n=num_iter):
        "Tests isPlausible with n plausible codes with length 4 outward code in proper format, using appropriate character sets"
        pos1=re.findall('[^QVX]',string.ascii_uppercase)
        pos2=re.findall('[^IJZ]',string.ascii_uppercase)
        dig=list(string.digits)
        pos4=list('ABEHMNPRVWXY')
        posin23=re.findall('[^CIKMOV]',string.ascii_uppercase)
        for _ in range(n):
            code = random.sample(pos1,1)[0] + random.sample(pos2,1)[0] + random.sample(dig,1)[0] + random.sample(pos4+dig,1)[0]
            code=' '.join([code,
                           ''.join([random.sample(dig,1)[0],
                                    ''.join(random.sample(posin23,2))])])
            p=postalcode(code)
            self.assertTrue(p.isPlausible())
if __name__ == '__main__':
    unittest.main()