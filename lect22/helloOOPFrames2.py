import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.geometry("400x200")

        #Create 2 frames
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        #Create a Label widget for top frame
        self.prompt_label = tk.Label(self.top_frame,  text= 'Enter temperature in degrees F: ')
        self.temp_entry = tk.Entry(self.top_frame, width = 10)
        
        # Call pack methods
        self.prompt_label.pack()
        self.temp_entry.pack()

        #Create mid frame
        self.descrip_label = tk.Label(self.mid_frame, text = 'Converted to degrees C: ')
        self.value = tk.StringVar()
        self.deg_label = tk.Label(self.mid_frame, textvar = self.value)
        
        self.descrip_label.pack()
        self.deg_label.pack()
        
        #Create a Label widget for bottom frame
        self.calc_button = tk.Button(self.bottom_frame,  text= 'Convert', command= self.convert)
        self.quit_button = tk.Button(self.bottom_frame, text = 'Quit', command=self.main_window.destroy)
    
        # Call pack methods
        self.quit_button.pack(side = 'bottom')
        self.calc_button.pack(side = 'bottom')

        #Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        self.main_window.title("Temperature Converter")
        # Start the Tkinter event loop
        tk.mainloop()

    def convert(self):
        fahr = float(self.temp_entry.get())
        cel = (fahr - 32) * 5/9
        cel = round(cel, 2)
        self.value.set(cel)
        #tkinter.messagebox.showinfo('Results', str(fahr) + ' degrees fahrenheit = ' + str(cel) + 'degrees celsius')
        #tkinter.messagebox.showinfo('Results', f'{fahr} degrees F = {cel:.2f} degrees C')
        
if __name__ == "__main__":
    my_gui = MyGUI()



