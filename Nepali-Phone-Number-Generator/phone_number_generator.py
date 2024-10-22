import random
import tkinter as tk
from tkinter import messagebox

# Function to generate a Nepali phone number
def generate_nepali_phone_number():
    country_code = "+977"
    
    # NTC and Ncell prefixes
    ntc_prefixes = ['984', '985', '986', '974', '976']
    ncell_prefixes = ['980', '981', '982']
    
    # Randomly choose either NTC or Ncell
    is_ntc = random.choice([True, False])
    
    if is_ntc:
        prefix = random.choice(ntc_prefixes)
    else:
        prefix = random.choice(ncell_prefixes)
    
    # Generate the rest of the 7 digits
    number_body = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    
    return f"{country_code} {prefix}-{number_body}"

# Function to show the generated number in the GUI
def show_phone_number():
    phone_number = generate_nepali_phone_number()
    messagebox.showinfo("Generated Phone Number", phone_number)

# Create a window
root = tk.Tk()
root.title("Nepali Phone Number Generator")

# Set the window size
root.geometry("300x200")

# Add a button to generate a phone number
generate_button = tk.Button(root, text="Generate Phone Number", command=show_phone_number)
generate_button.pack(pady=50)

# Run the application
root.mainloop()