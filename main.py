from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=90, pady=100)


def calculate_clicked():
    km_calculated_label.config(text=int(int(miles_entry.get()) * 1.609))


# entry
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)


# button
calculate_button = Button(text="Calculate", command=calculate_clicked, font=("Arial", 24, "bold"))
calculate_button.grid(column=1, row=2)


# labels
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
iet_label = Label(text="is equal to", font=("Arial", 24, "bold"))
km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_calculated_label = Label(text="0", font=("Arial", 24, "bold"))

# place labels
miles_label.grid(column=2, row=0)
iet_label.grid(column=0, row=1)
km_label.grid(column=2, row=1)
km_calculated_label.grid(column=1, row=1)


window.mainloop()
