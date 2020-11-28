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
from salesperson_dao import SalespersonDAO
from validation import Validation

class SalespersonGUI():
    """
    GUI class to perform CRUD operations on the Salesperson table in the database.
    """  

    def __init__(self):
        """
        Initialise Salesperson class.
        """
        
        # Data access object
        self.salesperson_dao = SalespersonDAO()

        # Validation object
        self.validator = Validation()

        # Form fields
        self.salesperson_id = tk.StringVar()
        self.title = tk.StringVar()
        self.firstname = tk.StringVar()
        self.surname = tk.StringVar()
        self.position = tk.StringVar()
        self.work_phone = tk.StringVar()
        self.email = tk.StringVar()

        # List of salesperson ids
        self.lb_ids = None

        # Messagebox title
        self.mb_title_bar = "Salesperson CRUD"

        pass

    def create_gui(self, root):
        """
        Create the GUI.

        This is the interface for the user to input data or query the database.
        It is composed of frames containing widgets (e.g. labels, input fields).

        Parameters (apart from self):
            root: main window of application

        Return: 
            salesperson_frame: the frame containing all the widgets for the 
                salesperson CRUD 
        """

        print("Creating Salesperson GUI ...")

        salesperson_frame = tk.Frame(root)
        salesperson_frame.pack()

        # FORM FRAME
        form_frame = tk.Frame(salesperson_frame)
        form_frame.pack()

        # FORM FRAME: ROW 0
        # Heading for Salesperson frame
        tk.Label(form_frame, text="Salesperson",
            font=('arial', 10)).grid(row=0, column=0, columnspan=3)

        # FORM FRAME: ROW 1
        # Label and entry field (disabled) for "Salesperson ID"
        tk.Label(form_frame, text="Salesperson ID", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=1, column=0)

        tk.Entry(form_frame, textvariable=self.salesperson_id, width=30, bd=1,
            state=tk.DISABLED).grid(row=1, column=1)

        # Heading for Listbox to display and select Salesperson IDs
        tk.Label(form_frame, text="Salesperson IDs",
            font=('arial', 10)).grid(row=1, column=2)

        # FORM FRAME: ROW 2
        # Label and combobox field for "Title"
        tk.Label(form_frame, text="Title", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=2, column=0)

        TITLE_VALUES = ("Mr", "Mrs", "Ms", "Miss", "Dr")

        ttk.Combobox(form_frame, state='readonly', textvariable=self.title,
            values=TITLE_VALUES, width=5).grid(row=2, column=1, sticky='w')

        # Listbox to display and select Salesperson IDs
        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=2, column=2, rowspan=6)
        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)

        # FORM FRAME: ROW 3
        # Label and entry field for "First Name"
        tk.Label(form_frame, text="First Name", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=3, column=0)

        tk.Entry(form_frame, textvariable=self.firstname, width=30,
            bd=1).grid(row=3, column=1)

        # FORM FRAME: ROW 4
        # Label and entry field for "Surname"
        tk.Label(form_frame, text="Surname", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=4, column=0)

        tk.Entry(form_frame, textvariable=self.surname, width=30,
            bd=1).grid(row=4, column=1)

        # FORM FRAME: ROW 5
        # Label and entry field for "Position"
        tk.Label(form_frame, text="Position", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=5, column=0)

        POSITION_VALUES = ("Junior", "Associate", "Senior")

        ttk.Combobox(form_frame, state='readonly', textvariable=self.position,
            values=POSITION_VALUES, width=10).grid(row=5, column=1, sticky='w')

        # FORM FRAME: ROW 6
        # Label and entry field for "Work Phone"
        tk.Label(form_frame, text="Work Phone", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=6, column=0)

        tk.Entry(form_frame, textvariable=self.work_phone, width=30,
            bd=1).grid(row=6, column=1)

        # FORM FRAME: ROW 7
        # Label and entry field for "Email"
        tk.Label(form_frame, text="E-mail", font=('arial', 10), width=20,
            anchor='e', bd=1, pady=10, padx=10).grid(row=7, column=0)

        tk.Entry(form_frame, textvariable=self.email, width=30,
            bd=1).grid(row=7, column=1)

        # BUTTON FRAME
        button_frame = tk.Frame(salesperson_frame, pady=10)
        button_frame.pack()

        tk.Button(button_frame, width=10, text="Clear",
            command=self.clear_fields).pack(side=tk.LEFT)

        tk.Button(button_frame, width=10, text="Save",
            command=self.save).pack(side=tk.LEFT)

        tk.Button(button_frame, width=10, text="Delete",
            command=self.delete).pack(side=tk.LEFT)

        tk.Button(button_frame, width=10, text="Load",
            command=self.load).pack(side=tk.LEFT)

        return salesperson_frame

    def clear_fields(self):
        """
        Clear the fields of the form

        Parameters (apart from self): None

        Return: None
        """
        self.salesperson_id.set("")
        self.title.set("")
        self.firstname.set("")
        self.surname.set("")
        self.position.set("")
        self.work_phone.set("")
        self.email.set("")
        pass

    def save(self):
        """
        Save the data displayed on the form to the database.

        Get salesperson data to be saved from the global instance attributes,
        then validate data by calling validate_fields()
        If the data is invalid, a message box is presented to the user.
        If the data is valid, the data is either saved or updated
        If salesperson_id is present, the data is updated
        If not, a new salesperson record is created in the database
 
        Parameters (apart from self): None
 
        Return: None
            
        """
        print("Saving a salesperson ...")

        data = self.get_fields()

        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (len(data['salesperson_id'])==0):
                print("Calling create() as salesperson_id is absent")
                self.create(data)
            else:
                print("Calling update() as salesperson_id is present")
                self.update(data)
                pass
        else:
            message_text = "Invalid fields.\n" + message
            messagebox.showwarning(self.mb_title_bar, message_text, icon='warning')
            pass

    def get_fields(self):
        sp = {}

        sp['salesperson_id'] = self.salesperson_id.get()
        sp['title'] = self.title.get()
        sp['firstname'] = self.firstname.get()
        sp['surname'] = self.surname.get()
        sp['position'] = self.position.get()
        sp['work_phone'] = self.work_phone.get()
        sp['email'] = self.email.get()

        return sp

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
        if len(data['title'])==0:
            valid_data = False
            message_list.append("title is empty")
        if len(data['firstname'])==0:
            valid_data = False
            message_list.append("firstname is empty")
        if len(data['surname'])==0:
            valid_data = False
            message_list.append("surname is empty")
        if len(data['position'])==0:
            valid_data = False
            message_list.append("position year is empty")
        if len(data['work_phone'])==0:
            valid_data = False
            message_list.append("work phone is empty")
        if len(data['email'])==0:
            valid_data = False
            message_list.append("e-mail is empty")

        # Position and title are selected from dropdown menu
        # so no further validation needed

        # Check that firstname and surname are alphabetic
        if not self.validator.is_alphabetic(data['firstname']):
            valid_data = False
            message_list.append("invalid firstname")

        if not self.validator.is_alphabetic(data['surname']):
            valid_data = False
            message_list.append("invalid surname")

        # Other checks
        if not self.validator.is_email(data['email']):
            valid_data = False
            message_list.append("invalid email format")

        if not self.validator.is_phone_number(data['work_phone']):
            valid_data = False
            message_list.append("invalid phone number format")

        message = ', '.join(message_list) 

        return valid_data, message
        pass

    def create(self, data):
        """
        Create a new record in the database.

        A messagebox is used display the outcome (success or failure) 
        of the create operation to the user.

        Parameters (apart from self):
            data: dictionary object containing salesperson data to be saved
 
        Return: None
        """
        print("Creating a salesperson ...")
        print(data)

        session = db.get_db_session()
        result = self.salesperson_dao.create(session, data)
        session.close()

        messagebox.showinfo(self.mb_title_bar, result)
        pass
 
    def update(self, data):
        """
        Update a record in the database.

        A messagebox is used display the outcome (success or failure) 
        of the update operation to the user.

        Parameters (apart from self):
            data: dictionary object containing salesperson data to be saved
 
        Return: None
        """
        print("Updating a salesperson ...")
        print(data)

        session = db.get_db_session()
        result = self.salesperson_dao.update(session, data['salesperson_id'], data)
        session.close()

        messagebox.showinfo(self.mb_title_bar, result)
        pass
  
    def delete(self):
        """
        Delete a record from the database.

        The salesperson_id of the record to be deleted is obtained from a 
        global attribute.

        A messagebox is used display the outcome (success or failure) 
        of the delete operation to the user.

        Parameters (apart from self): None
 
        Return: None

        """
        print("Deleting a salesperson ...")

        sp_id = self.salesperson_id.get()
        print(id)

        session = db.get_db_session()
        result = self.salesperson_dao.delete(session, sp_id)
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
        result = self.salesperson_dao.find_ids(session)
        session.close()
        print("result: ", result)

        if "salesperson_ids" in result:
            list_ids = result["salesperson_ids"]
            self.lb_ids.delete(0, tk.END)

            print("Setting salesperson_id in listbox")

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
        result = self.salesperson_dao.find_by_id(session, value)
        session.close()

        print("result: ", result)

        sp = result['salesperson']
        self.populate_fields(sp)

        pass

    def populate_fields(self, sp):
        """
        Populate the fields of the form with data.

        Parameters (apart from self):
            sp: dictionary object containing all the information
                about a salesperson

        Return: None
        """

        self.salesperson_id.set(sp['salesperson_id'])
        self.title.set(sp['title'])
        self.firstname.set(sp['firstname'])
        self.surname.set(sp['surname'])
        self.position.set(sp['position'])
        self.work_phone.set(sp['work_phone'])
        self.email.set(sp['email'])
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
    gui = SalespersonGUI()

    # Create the gui - pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop - the endless window loop to process user inputs
    root.mainloop()