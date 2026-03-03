# Importing required modules
from tkinter import *
import calendar
from tkinter import messagebox


# Function to show calendar
def showCalendar():
    try:
        year = int(year_field.get())

        # Create new window using Toplevel (Professional way)
        gui = Toplevel(root)
        gui.config(background='grey')
        gui.title(f"Calendar - {year}")
        gui.geometry("550x600")

        # Get calendar text
        gui_content = calendar.calendar(year)

        # Display calendar
        calYear = Label(gui, text=gui_content,
                        font="Consolas 10 bold",
                        justify=LEFT,
                        bg="grey")
        calYear.pack(pady=20)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid year!")


# Main window
if __name__ == "__main__":

    root = Tk()
    root.config(background='light grey')
    root.title("Calendar Application")
    root.geometry("300x200")

    # Heading
    heading = Label(root, text="Calendar",
                    bg='light grey',
                    font=("Times", 24, "bold"))
    heading.pack(pady=10)

    # Year Label
    year_label = Label(root, text="Enter Year",
                       bg='light grey',
                       font=("Arial", 12))
    year_label.pack()

    # Year Entry
    year_field = Entry(root, width=20)
    year_field.pack(pady=5)

    # Show Button
    show_button = Button(root, text="Show Calendar",
                         fg='white', bg='blue',
                         command=showCalendar)
    show_button.pack(pady=5)

    # Exit Button
    exit_button = Button(root, text="Exit",
                         fg='white', bg='red',
                         command=root.destroy)
    exit_button.pack(pady=5)

    root.mainloop()