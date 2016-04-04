# postalcode
--------------
## Summary
The British Postal System is aided by 6-8 character alphanumeric code. Each code carries four pieces of information:   
*Postal Area 
*Postcode District 
*Postcode Sector
*Postcode Unit (according [wikipedia] (https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting): generally represents a street, part of a street, a single address, a group of properties, a single property, a sub-section of the property, an individual organisation or a subsection of the organisation.

This module verifies arbitrary strings according to the rules specified in the above wikipedia article. 
In addition, it gives accessor methods to extract each of the four data mentioned before. E.g.
```
from postalcode import postalcode

code=postalcode('EC2A 4BX')
isCode=code.isPlausible()
postal_area=code.getPostalArea()
```
#Setup and use
-----------
There are two ways of making use of the library:
1. Copy postcode.py into your PYTHONPATH and import postalcode like in the above code snippet. THis allows you to make use of it in other modules.
2. Run it from the commanline e.g. python postalcode.py "EC2A 4BX".  
