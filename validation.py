# ########
# Packages
# ########
import re
import datetime
from datetime import datetime

# ################
# Validation Class
# ################

class Validation():
    """
    Validation class to check input is in valid form.
    """  

    def is_numeric(self, val):
        """
        Check if input is numeric

        Parameters (apart from self):
            val: input to be validated
 
        Return: True if valid, otherwise False
        """
        val = str(val)
        if val.isnumeric():
            print("Numeric")
            return True
        else:
            print("Not numeric")
            return False  

    def is_alphabetic(self, val):
        """
        Check if input is alphabetic

        Parameters (apart from self):
            val: input to be validated
 
        Return: True if valid, otherwise False
        """
        val = str(val)
        if val.isalpha():
            print("Alphabetic")
            return True
        else:
            print("Not alphabetic")
            return False  

    def is_alphanumeric(self, val):
        """
        Check if input is alphanumeric

        Parameters (apart from self):
            val: input to be validated
 
        Return: True if valid, otherwise False
        """
        val = str(val)
        if val.isalnum():
            print("Alphanumeric")
            return True
        else:
            print("Not alphanumeric")
            return False  

    def is_phone_number(self, val):
        """
        Check if input phone number follows correct format

        The correct format should contain only numbers and spaces
        and follow Australian landline phone no format,
        e.g. 02 9999 9999.

        Parameters (apart from self):
            val: input to be validated
 
        Return: True if valid, otherwise False
        """
        val = str(val)

        if re.match(r'(^\d{2} \d{4} \d{4})', val):
            print("Valid phone number")
            return True
        else:
            print("Invalid phone number")
            return False  

    def is_email(self, val):
        """
        Check if input email follows correct format

        The correct format should contain only one @ sign,
        and contain at least one . after the @. However
        it cannot end in a symbol or a number.

        Parameters (apart from self):
            val: input to be validated
 
        Return: True if valid, otherwise False
        """
        val = str(val)

        if re.match(r'[\w.-]+@([\w-]+\.)+[a-z]+', val):
            print("Valid email")
            return True
        else:
            print("Invalid email")
            return False

    def is_registration(self, val):

        """
        Check if input registration follows correct format

        The correct format should follow the current Victorian
        format for car registration.

        Parameters (apart from self):
            val: input to be validated
 
        Return: True if valid, otherwise False
        """

        val = str(val)
        
        # 6 characters long, alphanumeric
        # No whitespaces or other symbols

        # old_reg: NNN111
        old_reg = re.match(r'[A-Za-z]{3}\d{3}', val)

        # new_reg: 1NN1NN
        new_reg = re.match(r'(\d[A-Za-z]{2}){2}', val)

        if (new_reg or old_reg):
            print("Valid registration")
            return True
        else:
            print("Invalid registration")
            return False

    def is_manufacture_year(self, val):
        """
        Check if input manufacture year follows correct format

        Also checks if manufacture year is from the correct 
        time range (1950-now).

        Parameters (apart from self):
            val: input to be validated
 
        Return: True if valid, otherwise False
        """
        val = str(val)

        current_year = int(datetime.today().year)

        if val.isnumeric() and (int(val) > 1950) and (int(val) <= current_year):
            print("Valid manufacture year")
            return True

        else:
            print("Invalid manufacture year")
            return False
        
    pass

# ###########
# Main method
# ###########

if __name__ == '__main__':
    pass