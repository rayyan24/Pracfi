import tkinter as tk

class MyGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title('My GUI')
        self.geometry('300x200')

        # Create label and pack it to the window
        self.label = tk.Label(self, text='Hello, world!')
        self.label.pack()

        # Create button and pack it to the window
        self.button = tk.Button(self, text='Click me!', command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        # Change the label text when the button is clicked
        self.label.config(text='Button clicked!')

if __name__ == '__main__':
    # Create an instance of MyGUI and start the main event loop
    gui = MyGUI()
    gui.mainloop()
