from schema import Car

class CarDAO():

    def create(self, session, data):
        """
        Create a new record in the database.

        Instantiate an object of class Car, and then pass this object to
        the session.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
            data: dictionary object containing car data
 
        Return: dictionary containing success message and car ID if successful.
        """

        print("\nCreating a car record...")
        print(data)

        car = Car(make = data['make'], 
                    model = data['model'], 
                    registration = data['registration'],
                    manufacture_year = data['manufacture_year'],
                    colour= data['colour']
                    )

        session.add(car)
        session.commit()

        result = {}  
        result['message'] = 'Car added successfully!'
        inserted_car_id = car.car_id
        result['car_id'] = inserted_car_id

        return result

    
    def find_by_id(self, session, car_id):
        """
        Find an existing record in the database by its ID.

        Create a query based on car ID and pass this to the
        session.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
            car_id: primary key of the Car schema
 
        Return: dictionary containing matching car record if successful.
        """

        print("\nFinding a car ...")
        print(car_id)

        car_record = session.query(Car).get(car_id) 

        result = {}

        if not car_record:
            result['message'] = "Car NOT found"
        else:
            d = {}
            d['car_id'] = car_record.car_id
            d['make'] = car_record.make
            d['model'] = car_record.model
            d['registration'] = car_record.registration
            d['manufacture_year'] = car_record.manufacture_year
            d['colour'] = car_record.colour

            result['car'] = d

        return result

    
    def find_by_make(self, session, make):
        """
        Find car record(s) in the database by make.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
            make: make of car(s) to find (e.g. Mazda, Toyota)
 
        Return: dictionary containing matching car record(s) if found.
        """ 

        print("\nFinding car(s) by make ...")
        print(make)

        result = {}

        rows = session.query(Car) \
               .filter(Car.make.like(make)) \
               .order_by(Car.car_id).all()   

        if not rows:
            result['message'] = "No cars found!"
        else:
            list_cars = []
            for x in rows:
                d = {}
                d['car_id'] = x.car_id
                d['make'] = x.make
                d['model'] = x.model
                d['registration'] = x.registration
                d['manufacture_year'] = x.manufacture_year
                d['colour'] = x.colour
                list_cars.append(d)
                pass     

            result['cars'] = list_cars
           
        return result

    
    def find_all(self, session):
        """
        Find all car record(s) in the database.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
 
        Return: dictionary containing all car records if successful.
        """

        print("\nFinding all cars ...")

        result = {}

        rows = session.query(Car).all()

        if not rows:
            result['message'] = "No cars found!"
        else:
            list_cars = []
            for x in rows:
                d = {}
                d['car_id'] = x.car_id
                d['make'] = x.make
                d['model'] = x.model
                d['registration'] = x.registration
                d['manufacture_year'] = x.manufacture_year
                d['colour'] = x.colour
                list_cars.append(d)
                pass  

            result['cars'] = list_cars
            
        return result

    
    def find_ids(self, session):
        """
        Find IDs of all car(s) in the database.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
 
        Return: dictionary containing list of all existing car IDs.
        """

        print("\nFinding all car ids ...")

        result = {}
 
        rows = session.query(Car).all()

        if not rows:
            result['message'] = "No cars found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.car_id)
                pass               

            result['car_ids'] = list_ids
        
        return result


    def update(self, session, car_id, data):
        """
        Update a record in the database.

        Query the database to get the car record by its ID, and if found,
        update according to new values and commit the updated record to the
        database.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
            car_id: primary key of the Car schema
            data: dictionary object containing car data
 
        Return: dictionary containing success message and
            updated car record if successful.
        """

        print("\nUpdating car ...")
        print(car_id)
        print(data)

        result = {}

        car_record = session.query(Car).get(car_id)

        if not car_record:
            result['message'] = "Car NOT found!"
        else:
            car_record.make = data['make']
            car_record.model = data['model']
            car_record.registration = data['registration']
            car_record.manufacture_year = data['manufacture_year']
            car_record.colour = data['colour']

            session.commit()

            result['message'] = "Car updated!"     

        return result


    def delete(self, session, car_id):
        """
        Delete a record from the database.
        
        Query the database to get the car record by it ID, and if found,
        delete the record from the database.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
            car_id: primary key of the Car schema
 
        Return: dictionary containing success message if successful.
        """

        print("\nDeleting car record ...")
        print(car_id)
 
        result = {}

        car_record = session.query(Car).get(car_id)

        if not car_record:
            result['message'] = "Car NOT found!"
        else:
            session.delete(car_record)         
            session.commit()

            result['message'] = "Car deleted!"   

        return result
