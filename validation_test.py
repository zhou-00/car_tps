# ##############
# Import classes
# ##############
from validation import Validation

# ##########
# Test cases
# ##########

def test_is_numeric(validation):
    """ Test the is_numeric() validation function. """
    print("\n1.Testing is_numeric()") 
    
    # True
    assert (validation.is_numeric(10))

    # False
    assert (not validation.is_numeric(10.002))
    assert (not validation.is_numeric("abc"))
    assert (not validation.is_numeric("10abc"))

def test_is_alphabetic(validation):
    """ Test the is_alphabetic() validation function. """
    print("\n2. Testing is_alphabetic()")

    # True
    assert (validation.is_alphabetic("abc"))

    # False
    assert (not validation.is_alphabetic(10))    
    assert (not validation.is_alphabetic(10.002)) 
    assert (not validation.is_alphabetic("10abc"))

def test_is_alphanumeric(validation):
    """ Test the is_alphanumeric() validation function. """
    print("\n3. Testing is_alphanumeric()")

    # True
    assert (validation.is_alphanumeric(10))  
    assert (validation.is_alphanumeric("abc")) 
    assert (validation.is_alphanumeric("10abc")) 

    # False 
    assert (not validation.is_alphanumeric(10.02))
    assert (not validation.is_alphanumeric("_")) 
    assert (not validation.is_alphanumeric(" "))
    assert (not validation.is_alphanumeric(".")) 

def test_is_phone_number(validation):
    """ Test the is_phone_number() validation function. """
    print("\n4. Testing is_phone_number()")

    # True
    assert (validation.is_phone_number("02 9999 9999")) 

    # False
    assert (not validation.is_phone_number("(02) 9999 9999"))
    assert (not validation.is_phone_number("0299999999"))
    assert (not validation.is_phone_number("02-9999-9999"))
    assert (not validation.is_phone_number("02.9999.9999"))
    assert (not validation.is_phone_number("+61 2 9999 9999"))
    assert (not validation.is_phone_number("0413 888 888"))

def test_is_email(validation):
    """ Test the is_email() validation function. """
    print("\n5. Testing is_email()")

    # True
    assert (validation.is_email("xyz@abc.def"))
    assert (validation.is_email("xyz@abc.def.com"))

    # False
    assert (not validation.is_email("xyz@abcdef"))
    assert (not validation.is_email("xyzabcdef"))
    assert (not validation.is_email("@abcdef"))

def test_is_registration(validation):
    """ Test the is_registration() validation function. """
    print("\n6. Testing is_registration()")

    # True
    assert (validation.is_registration("ABC123"))
    assert (validation.is_registration("1JJ2KK"))

    # False
    assert (not validation.is_registration("AB1234"))
    assert (not validation.is_registration("ABCD123"))
    assert (not validation.is_registration("ABC"))
    assert (not validation.is_registration("111111"))

    pass

def test_is_manufacture_year(validation):
    """ Test the is_mamufacture_year() validation function. """
    print("\n7. Testing is_manufacture_year()")

    #True
    assert (validation.is_manufacture_year("2005"))

    # False
    assert (not validation.is_manufacture_year("1900"))
    assert (not validation.is_manufacture_year("This year"))
    assert (not validation.is_manufacture_year("2000+"))
    pass
        

if __name__ == '__main__':
    
    print("\nTesting ...")

    # Instantiate a validation object
    validation = Validation()

    test_is_numeric(validation)

    test_is_alphabetic(validation)

    test_is_alphanumeric(validation)

    test_is_phone_number(validation)

    test_is_email(validation)

    test_is_registration(validation)

    test_is_manufacture_year(validation)