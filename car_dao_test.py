from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from car_dao import CarDAO

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
    Test the create() method of the CarDAO class
    """
    session = get_db_session()

    car_record = CarDAO()

    data = {
        'make':"Tesla",
        'model': "Model X",
        'registration': "ABC123",
        'manufacture_year': 2018,
        'colour': "black"
    }

    result = car_record.create(session, data)

    print(result)

    session.close()


def test_find_by_id():
    """
    Test the find_by_id() method of the CarDAO class
    """
    session = get_db_session()

    car_record = CarDAO()

    car_id = 1

    result = car_record.find_by_id(session, car_id)

    print(result)

    session.close()


def test_find_all():
    """
    Test the find_all() method of the CarDAO class
    """
    session = get_db_session()

    car_record = CarDAO()

    result = car_record.find_all(session)

    print(result)

    session.close()    


def test_find_by_make():
    """
    Test the find_by_make() method of the CarDAO class
    """
    session = get_db_session()

    car_record = CarDAO()

    make = "tesla"

    result = car_record.find_by_make(session, make)

    print(result)

    session.close()  


def test_find_ids():
    """
    Test the find_ids() method of the CarDAO class
    """
    session = get_db_session()

    car_record = CarDAO()

    result = car_record.find_ids(session)

    print(result)

    session.close()    


def test_update():
    """
    Test the update() method of the CarDAO class
    """
    session = get_db_session()

    car_record = CarDAO()

    car_id = 1

    data = {}
    data['make'] = "Toyota"
    data['model'] = "Prius"
    data['registration'] = "XYZ999"
    data['manufacture_year'] = 2019
    data['colour'] = "red"

    result = car_record.update(session, car_id, data)

    print(result)

    session.close()    


def test_delete():
    """
    Test the delete() method of the CarDAO class
    """
    session = get_db_session()
        
    car_record = CarDAO()

    car_id = 1

    result = car_record.delete(session, car_id)

    print(result)

    session.close()          


if __name__ == "__main__":

    print("\nTesting ...")

    test_create()
    
    test_find_by_id()

    test_find_all()

    test_find_by_make()

    test_find_ids()

    test_update()

    test_delete()