# Lecture 22 Activity
# Converting inches to centimeters in GUI
# Complete each section as indicated to compute the quantity indicated

import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self):
    
        self.main_window = tk.Tk()
        self.main_window.geometry("400x200")

        #Create 3 frames (2 are done for you)
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window) 
        self.bottom_frame = tk.Frame(self.main_window)


        #Update text of label and add a second label and entry box
        self.prompt_label = tk.Label(self.top_frame,  text= 'Please add a measurement in inches:')
        self.temp_entry = tk.Entry(self.top_frame, width = 10)
        self.prompt_label = tk.Label(self.top_frame, text='Output in centimeters:')
        self.temp_entry = tk.Entry(self.top_frame, width=10)

        
        #Call all pack methods
        self.prompt_label.pack()
        self.temp_entry.pack()


        #Update label appropriately
        self.descrip_label = tk.Label(self.mid_frame, text = 'The measurement in centimeters is: ')
        self.value = tk.StringVar()
        self.value_label = tk.Label(self.mid_frame, textvar = self.value)
        
        self.descrip_label.pack()
        self.value_label.pack()
        
        #Create 2 button widgets for bottom frame, one to perform the calculation, one to quit
        self.calc_button = tk.Button(self.bottom_frame, text = 'Calculate', command = self.compute)
        self.quit_button = tk.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)
        
    
        #Pack the button widgets
        self.calc_button.pack(side = 'bottom')
        self.quit_button.pack(side = 'bottom')


        #Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()


        #Change window Title
        self.main_window.title("Calculator")

        tk.mainloop()

    #Compute the quantity specified in the class instructions
    def compute(self):
        # convert into centimeters
        try:
            inches = float(self.temp_entry.get()) # always a string.
        except ValueError:
            tkinter.messagebox.showinfo('Error', 'Please enter a valid number.')
            #clear the value 
            self.value.set('') 
            # clear the entry box
            self.temp_entry.delete(0, tk.END)
            return

        centimeters = inches * 2.54
        self.value.set(f'{centimeters:.2f} cm')
        tkinter.messagebox.showinfo('Results', f'{inches} inches = {centimeters:.2f} centimeters')
        
if __name__ == "__main__":
    my_gui = MyGUI()



