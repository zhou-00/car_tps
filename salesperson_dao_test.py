from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from salesperson_dao import SalespersonDAO

# Database location
DATABASE_URI = 'sqlite:///app.db'

def get_db_session():
    """
    Create a database session
    """
    engine = create_engine(DATABASE_URI, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session 


def test_create():
    """
    Test the create() method of the SalespersonDAO class
    """
    session = get_db_session()

    sp = SalespersonDAO()

    data = {
        'title': "Mr",
        'firstname': "Elon",
        'surname': "Musk",
        'position': "Mid-Level",
        'work_phone': "(02) 9999 9999",
        'email': "emusk@spacex.com"
    }

    result = sp.create(session, data)

    print(result)

    session.close()


def test_find_by_id():
    """
    Test the find_by_id() method of the SalespersonDAO class
    """
    session = get_db_session()

    sp = SalespersonDAO()

    salesperson_id = 1

    result = sp.find_by_id(session, salesperson_id)

    print(result)

    session.close()


def test_find_all():
    """
    Test the find_all() method of the SalespersonDAO class
    """
    session = get_db_session()

    sp = SalespersonDAO()

    result = sp.find_all(session)

    print(result)

    session.close()    


def test_find_by_surname():
    """
    Test the find_by_surname() method of the SalespersonDAO class
    """
    session = get_db_session()

    sp = SalespersonDAO()

    surname = "musk"

    result = sp.find_by_surname(session, surname)

    print(result)

    session.close()  


def test_find_ids():
    """
    Test the find_ids() method of the SalespersonDAO class
    """
    session = get_db_session()

    sp = SalespersonDAO()

    result = sp.find_ids(session)

    print(result)

    session.close()    


def test_update():
    """
    Test the update() method of the SalespersonDAO class
    """
    session = get_db_session()

    sp = SalespersonDAO()

    salesperson_id = 1

    data = {}
    data['title'] = "Dr"
    data['firstname'] = "Elon"
    data['surname'] = "Musk"
    data['position'] = "Senior"
    data['work_phone'] = "(02) 9999 1234"
    data['email'] = "emusk@tesla.com"

    result = sp.update(session, salesperson_id, data)

    print(result)

    session.close()    


def test_delete():
    """
    Test the delete() method of the SalespersonDAO class
    """
    session = get_db_session()
        
    sp = SalespersonDAO()

    salesperson_id = 1

    result = sp.delete(session, salesperson_id)

    print(result)

    session.close()          


if __name__ == "__main__":

    print("\nTesting ...")

    test_create()
    
    test_find_by_id()

    test_find_all()

    test_find_by_surname()

    test_find_ids()

    test_update()

    test_delete()