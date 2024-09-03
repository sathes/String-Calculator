import re

class NegativeNumberError(Exception):
    """
    Custom exception for negative number inputs.
    """
    pass

def add_extracted_numbers(s):
    """
    Extracts all positive and negative numbers from a string and returns their sum  
    if no negative numbers are present and ignore larger then 1000.
    Raises a NegativeNumberError if negative numbers are present.    
    """
    # This regex will match both positive and negative numbers
    if s:
        total = 0
        negative_numbers = []
        numbers = re.findall(r'-?\d+', s)
        for num in numbers:
            num_int = int(num)
            if num_int < 0:
                negative_numbers.append(num)
            elif num_int <= 1000 :
                total = total + num_int
        if negative_numbers:
            raise NegativeNumberError("Negative numbers are not allowed : {}".format(negative_numbers))
        return total
    else:
        return 0
    
    
        
""""
s = "e3d??43jd-jd??7f5i10000inv23f0,1\n"
#s = "e3d??43jd-jd??7f-5i10000inv23f0,1\n"
#s = ''
#s = '1,3'
z =add_extracted_numbers(s)
print(z)
"""