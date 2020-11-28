# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

# ##############
# Import classes
# ##############
import database as db 
from car_dao import CarDAO
from validation import Validation

class CarGUI():
    """
    GUI class to perform CRUD operations on the Car table in the database.
    """  

    def __init__(self):
        """
        Initialise CarGUI class.
        """

        # Data access object
        self.car_dao = CarDAO()

        # Validation object
        self.validator = Validation()

        # Form fields
        self.car_id = tk.StringVar()
        self.make = tk.StringVar()
        self.model = tk.StringVar()
        self.registration = tk.StringVar()
        self.manufacture_year = tk.StringVar()
        self.colour = tk.StringVar()

        # List of car ids
        self.lb_ids = None

        # Messagebox title
        self.mb_title_bar = "Car CRUD"

        pass

    def create_gui(self, root):
        """
        Create the GUI.

        This is the interface for the user to input data or query the database.
        It is composed of frames containing widgets (e.g. labels, input fields).

        Parameters (apart from self):
            root: main window of application

        Return: 
            car_frame: the frame containing all the widgets for the car CRUD 
        """

        print("Creating Car GUI ...")

        car_frame = tk.Frame(root)
        car_frame.pack()

        # FORM FRAME
        form_frame = tk.Frame(car_frame)
        form_frame.pack()

        # FORM FRAME: ROW 0
        # Heading for Car frame
        tk.Label(form_frame, text="Car",
            font=('arial', 10)).grid(row=0, column=0, columnspan=3)

        # FORM FRAME: ROW 1
        # Label and entry field (disabled) for "Car ID"
        tk.Label(form_frame, text="Car ID", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=1, column=0)

        tk.Entry(form_frame, textvariable=self.car_id, width=30, bd=1,
            state=tk.DISABLED).grid(row=1, column=1)

        # Heading for Listbox to display and select Car IDs
        tk.Label(form_frame, text="Car IDs",
            font=('arial', 10)).grid(row=1, column=2)

        # FORM FRAME: ROW 2
        # Label and entry field for "Make"
        tk.Label(form_frame, text="Make", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=2, column=0)

        tk.Entry(form_frame, textvariable=self.make, width=30, bd=1).grid(row=2, column=1)

        # Listbox to display and select Car IDs
        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=2, column=2, rowspan=5)
        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)

        # FORM FRAME: ROW 3
        # Label and entry field for "Model"
        tk.Label(form_frame, text="Model", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=3, column=0)

        tk.Entry(form_frame, textvariable=self.model, width=30, bd=1).grid(row=3, column=1)

        # FORM FRAME: ROW 4
        # Label and entry field for "Registration"
        tk.Label(form_frame, text="Registration", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=4, column=0)

        tk.Entry(form_frame, textvariable=self.registration, width=30,
            bd=1).grid(row=4, column=1)

        # FORM FRAME: ROW 5
        # Label and entry field for "Manufacture Year"
        tk.Label(form_frame, text="Manufacture Year", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=5, column=0)

        tk.Entry(form_frame, textvariable=self.manufacture_year, width=30,
            bd=1).grid(row=5, column=1)

        # FORM FRAME: ROW 6
        # Label and entry field for "Colour"
        tk.Label(form_frame, text="Colour", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=6, column=0)

        tk.Entry(form_frame, textvariable=self.colour, width=30,
            bd=1).grid(row=6, column=1)

        # BUTTON FRAME
        button_frame = tk.Frame(car_frame, pady=10)
        button_frame.pack()

        tk.Button(button_frame, width=10, text="Clear",
            command=self.clear_fields).pack(side=tk.LEFT)

        tk.Button(button_frame, width=10, text="Save",
            command=self.save).pack(side=tk.LEFT)

        tk.Button(button_frame, width=10, text="Delete",
            command=self.delete).pack(side=tk.LEFT)

        tk.Button(button_frame, width=10, text="Load",
            command=self.load).pack(side=tk.LEFT)

        return car_frame

    def clear_fields(self):
        """
        Clear the fields of the form

        Parameters (apart from self): None

        Return: None
        """
        self.car_id.set("")
        self.make.set("")
        self.model.set("")
        self.registration.set("")
        self.manufacture_year.set("")
        self.colour.set("")
        pass

    def save(self):
        """
        Save the data displayed on the form to the database.

        Get car data to be saved from the global instance attributes,
        then validate data by calling validate_fields()
        If the data is invalid, a message box is presented to the user.
        If the data is valid, the data is either saved or updated
        If car_id is present, the data is updated
        If not, a new car record is created in the database
 
        Parameters (apart from self): None
 
        Return: None
            
        """
        print("Saving a car ...")

        data = self.get_fields()

        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (len(data['car_id'])==0):
                print("Calling create() as car_id is absent")
                self.create(data)
            else:
                print("Calling update() as car_id is present")
                self.update(data)
                pass
        else:
            message_text = "Invalid fields.\n" + message
            messagebox.showwarning(self.mb_title_bar, message_text, icon='warning')
            pass

    def get_fields(self):
        """
        Get the data entered in the fields of the form

        Parameters (apart from self): None

        Return:
            car_record: dictionary object containing all the information 
                about a car
        """
        car_record = {}

        car_record['car_id'] = self.car_id.get()
        car_record['make'] = self.make.get()
        car_record['model'] = self.model.get()
        car_record['registration'] = self.registration.get()
        car_record['manufacture_year'] = self.manufacture_year.get()
        car_record['colour'] = self.colour.get()

        return car_record

    def validate_fields(self, data):
        """
        Validate the data entered in the fields of the form

        Parameters (apart from self):
            data: dictionary object containing all the information entered on the form

        Return:
            valid_data: a boolean indication whether the data is valid (True) or 
                not valid (False)
            message: a string containing details about the fields that are not valid
            
            Returned as a tuple (valid_data, message)
        """
        valid_data = True
        message_list = []

        # Check field is not empty
        if len(data['make'])==0:
            valid_data = False
            message_list.append("make is empty")
        if len(data['model'])==0:
            valid_data = False
            message_list.append("model is empty")
        if len(data['registration'])==0:
            valid_data = False
            message_list.append("registration is empty")
        if len(data['manufacture_year'])==0:
            valid_data = False
            message_list.append("manufacture year is empty")
        if len(data['colour'])==0:
            valid_data = False
            message_list.append("colour is empty")

        # Check that colour and make are alphabetic
        if not self.validator.is_alphabetic(data['colour']):
            valid_data = False
            message_list.append("invalid colour")

        if not self.validator.is_alphabetic(data['make']):
            valid_data = False
            message_list.append("invalid make")

        # Model can contain numbers e.g. Mazda2
        if not self.validator.is_alphanumeric(data['model']):
            valid_data = False
            message_list.append("invalid model")

        # Other checks
        if not self.validator.is_manufacture_year(data['manufacture_year']):
            valid_data = False
            message_list.append("invalid manufacture year")

        if not self.validator.is_registration(data['registration']):
            valid_data = False
            message_list.append("invalid registration")

        message = ', '.join(message_list) 

        return valid_data, message

        pass

    def create(self, data):
        """
        Create a new record in the database.

        A messagebox is used display the outcome (success or failure) 
        of the create operation to the user.

        Parameters (apart from self):
            data: dictionary object containing car data to be saved
 
        Return: None
        """
        print("Creating a car ...")
        print(data)

        session = db.get_db_session()
        result = self.car_dao.create(session, data)
        session.close()

        messagebox.showinfo(self.mb_title_bar, result)
        pass
 
    def update(self, data):
        """
        Update a record in the database.

        A messagebox is used display the outcome (success or failure) 
        of the update operation to the user.

        Parameters (apart from self):
            data: dictionary object containing car data to be saved
 
        Return: None
        """
        print("Updating a car ...")
        print(data)

        session = db.get_db_session()
        result = self.car_dao.update(session, data['car_id'], data)
        session.close()

        messagebox.showinfo(self.mb_title_bar, result)
        pass
  
    def delete(self):
        """
        Delete a record from the database.

        The car_id of the record to be deleted is obtained from a 
        global attribute.

        A messagebox is used display the outcome (success or failure) 
        of the delete operation to the user.

        Parameters (apart from self): None
 
        Return: None

        """
        print("Deleting a car ...")

        car_record_id = self.car_id.get()
        print(id)

        session = db.get_db_session()
        result = self.car_dao.delete(session, car_record_id)
        session.close()

        messagebox.showinfo(self.mb_title_bar, result)
        pass
        
    def load(self):
        """
        Retrieve a list of IDs from the database and load them into a listbox.
 
        Parameters (apart from self):
  
        Return: None
        """

        session = db.get_db_session()
        result = self.car_dao.find_ids(session)
        session.close()
        print("result: ", result)

        if "car_ids" in result:
            list_ids = result["car_ids"]
            self.lb_ids.delete(0, tk.END)

            print("Setting car_id in listbox")

            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
            pass

    def on_list_select(self, evt):
        """
        Actions to be triggered when a user clicks an item in the listbox.

        Defined above in create_gui(), where on_list_select is bound to the
        listbox selection.

        Parameters (apart from self):
            evt: object containing information about the mouse click

        Return: None
        """

        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)

        print(index)
        print(value)

        session = db.get_db_session()
        result = self.car_dao.find_by_id(session, value)
        session.close()

        print("result: ", result)

        car_record = result['car']
        self.populate_fields(car_record)

        pass

    def populate_fields(self, car_record):
        """
        Populate the fields of the form with data.

        Parameters (apart from self):
            car_record: dictionary object containing all the information
                about a car

        Return: None
        """

        self.car_id.set(car_record['car_id'])
        self.make.set(car_record['make'])
        self.model.set(car_record['model'])
        self.registration.set(car_record['registration'])
        self.manufacture_year.set(car_record['manufacture_year'])
        self.colour.set(car_record['colour'])
        pass


# ###########
# Main method
# ###########

if __name__ == '__main__':
     
    # Setup a root window (in the middle of the screen)
    root = tk.Tk()
    root.title("Car Dealership System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = CarGUI()

    # Create the gui - pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop - the endless window loop to process user inputs
    root.mainloop()