from schema import Salesperson

class SalespersonDAO():

    def create(self, session, data):
        """
        Create a new record in the database.

        Instantiate an object of class Salesperson, and then pass
        this object to the session.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
            data: dictionary object containing salesperson data
 
        Return: dictionary containing success message and
            salesperson ID if successful.
        """

        print("\nCreating a salesperson ...")
        print(data)

        salesperson = Salesperson(title = data['title'], 
                    firstname = data['firstname'], 
                    surname = data['surname'],
                    position = data['position'],
                    work_phone= data['work_phone'],
                    email = data['email']
                    )

        session.add(salesperson)
        session.commit()

        result = {}  
        result['message'] = 'Salesperson added successfully!'
        inserted_salesperson_id = salesperson.salesperson_id
        result['salesperson_id'] = inserted_salesperson_id

        return result

    
    def find_by_id(self, session, salesperson_id):
        """
        Find an existing record in the database by its ID.

        Create a query based on salesperson ID and pass this to the
        session.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
            salesperson_id: primary key of the Salesperson schema
 
        Return: dictionary containing salesperson record if successful.
        """

        print("\nFinding a salesperson ...")
        print(salesperson_id)

        sp = session.query(Salesperson).get(salesperson_id) 

        result = {}

        if not sp:
            result['message'] = "Salesperson NOT found"
        else:
            d = {}
            d['salesperson_id'] = sp.salesperson_id
            d['title'] = sp.title
            d['firstname'] = sp.firstname
            d['surname'] = sp.surname
            d['position'] = sp.position
            d['work_phone'] = sp.work_phone
            d['email'] = sp.email

            result['salesperson'] = d

        return result

    
    def find_by_surname(self, session, surname):
        """
        Find salesperson record(s) in the database by surname.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
            surname: surname of salesperson to find
 
        Return: dictionary containing matching salesperson record(s) if found.
        """ 

        print("\nFinding salesperson(s) by surname ...")
        print(surname)

        result = {}

        rows = session.query(Salesperson) \
               .filter(Salesperson.surname.like(surname)) \
               .order_by(Salesperson.salesperson_id).all()   

        if not rows:
            result['message'] = "No salesperson found!"
        else:
            list_sp = []
            for x in rows:
                d = {}
                d['salesperson_id'] = x.salesperson_id
                d['title'] = x.title
                d['firstname'] = x.firstname
                d['surname'] = x.surname
                d['position'] = x.position
                d['work_phone'] = x.work_phone
                d['email'] = x.email
                list_sp.append(d)
                pass     

            result['salespeople'] = list_sp
           
        return result

    
    def find_all(self, session):
        """
        Find all salesperson record(s) in the database.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
 
        Return: dictionary containing all salesperson records if successful.
        """

        print("\nFinding all salespeople ...")

        result = {}

        rows = session.query(Salesperson).all()

        if not rows:
            result['message'] = "No salespeople found!"
        else:
            list_sp = []
            for x in rows:
                d = {}
                d['salesperson_id'] = x.salesperson_id
                d['title'] = x.title
                d['firstname'] = x.firstname
                d['surname'] = x.surname
                d['position'] = x.position
                d['work_phone'] = x.work_phone
                d['email'] = x.email
                list_sp.append(d)
                pass  

            result['salespeople'] = list_sp

        return result

    
    def find_ids(self, session):
        """
        Find IDs of all salesperson(s) in the database.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
 
        Return: dictionary containing list of all existing salesperson IDs.
        """

        print("\nFinding all salesperson ids ...")

        result = {}
 
        rows = session.query(Salesperson).all()

        if not rows:
            result['message'] = "No salespeople found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.salesperson_id)
                pass               

            result['salesperson_ids'] = list_ids
        
        return result


    def update(self, session, salesperson_id, data):
        """
        Update a record in the database.

        Query the database to get the salesperson record by their ID,
        and if found, update according to new values and commit the updated
        record to the database.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
            salesperson_id: primary key of the Salesperson schema
            data: dictionary object containing salesperson data
 
        Return: dictionary containing success message and
            updated salesperson record if successful.
        """

        print("\nUpdating salesperson ...")
        print(salesperson_id)
        print(data)

        result = {}

        sp = session.query(Salesperson).get(salesperson_id)

        if not sp:
            result['message'] = "Salesperson NOT found!"
        else:
            sp.title = data['title']
            sp.firstname = data['firstname']
            sp.surname = data['surname']
            sp.position = data['position']
            sp.work_phone = data['work_phone']
            sp.email = data['email']

            session.commit()

            result['message'] = "Salesperson updated!"     

        return result


    def delete(self, session, salesperson_id):
        """
        Delete a record from the database.
        
        Query the database to get the salesperson record by their ID,
        and if found, delete the record from the database.

        Parameters (apart from self):
            session: session object to connect with db, and store objects
            salesperson_id: primary key of the Salesperson schema
 
        Return: dictionary containing success message if successful.
        """

        print("\nDeleting salesperson ...")
        print(salesperson_id)
 
        result = {}

        sp = session.query(Salesperson).get(salesperson_id)

        if not sp:
            result['message'] = "Salesperson NOT found!"
        else:
            session.delete(sp)         
            session.commit()

            result['message'] = "Salesperson deleted!"   

        return result