# ########
# Packages
# ########
import tkinter as tk
from PIL import ImageTk, Image

# ##############
# Import classes
# ##############

from salesperson_gui import SalespersonGUI
from car_gui import CarGUI

# ######################
# CarDealershipGUI Class
# ######################

class CarDealershipGUI():
    """
    GUI class for the main interface of the Car Dealership transaction processing system.
    """  

    def __init__(self):
        """
        Initialise CarDealershipGUI class.
        """

        print("Creating Car Dealership GUI ...")

        self.current_gui = None

        self.root = tk.Tk()
        self.root.title("Car Dealership System")

        # SET WINDOW DIMENSIONS
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        
        print("Main window coordinates (width, height, x, y) :", width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        # MENU BAR
        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open",command='')
        file_menu.add_command(label="Save",command='')
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Salesperson menu
        salesperson_menu = tk.Menu(menubar, tearoff=0)
        salesperson_menu.add_command(label="Salesperson", command=self.create_salesperson_gui)
        menubar.add_cascade(label="Salesperson", menu=salesperson_menu)

        # Car menu
        car_menu = tk.Menu(menubar, tearoff=0)
        car_menu.add_command(label="Car",command=self.create_car_gui)
        menubar.add_cascade(label="Car", menu=car_menu)

        self.root.config(menu=menubar)

        # CANVAS FOR IMAGE
        self.image = Image.open('car.jpg')
        self.image = self.image.resize((900, 600))
        self.image = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(self.root, height=900, width=600, bg="darkgrey")
        self.canvas.create_image(450, 300, image=self.image) 

        # Place the canvas in the middle of the frame
        self.canvas.pack(fill="none", expand=True)

        pass

    def create_salesperson_gui(self):
        """
        Create Salesperson GUI child frame when "Salesperson" selected from menu.
        """
        if self.canvas:
            self.canvas.destroy()

        if self.current_gui:
            self.current_gui.destroy()

        salesperson_gui = SalespersonGUI()
        self.current_gui = salesperson_gui.create_gui(self.root)
        pass

    def create_car_gui(self):
        """
        Create Car GUI child frame when "Car" selected from menu.
        """
        if self.canvas:
            self.canvas.destroy()

        if self.current_gui:
            self.current_gui.destroy()

        car_gui = CarGUI()
        self.current_gui = car_gui.create_gui(self.root)
        pass

# ###########
# Main method
# ###########

if __name__ == '__main__':

    # Instantiate the main application gui
    # it will create all the necessary GUIs
    gui = CarDealershipGUI()

    # Run the mainloop 
    # the endless window loop to process user inputs
    gui.root.mainloop()
    pass