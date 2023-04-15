import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MyGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("My GUI")
        self.master.config(bg= "#fff0f5")

        # Create the header frame and set the background color to TCU's purple
        self.header_frame = tk.Frame(self.master, bg="#4d1979")
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Load the logo image and resize it
        logo_image = Image.open("client_logo.jpg")
        logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)

        # Convert the logo image to a PhotoImage and add it to the logo canvas
        self.logo_image = ImageTk.PhotoImage(logo_image)
        self.logo_canvas = tk.Canvas(self.header_frame, width=self.logo_image.width(), height=self.logo_image.height(), bg="#4d1979", highlightthickness=0)
        self.logo_canvas.pack(side="left", padx=10, pady=10)
        self.logo_canvas.create_image(0, 0, anchor="nw", image=self.logo_image)

        # Load the first map image and resize it
        map1_image = Image.open("map1.jpg")
        map1_image = map1_image.resize((300, 300), Image.ANTIALIAS)

        # Convert the first map image to a PhotoImage and add it to the first canvas
        self.map1_image = ImageTk.PhotoImage(map1_image)
        self.map1_canvas = tk.Canvas(self.master, width=self.map1_image.width(), height=self.map1_image.height())
        self.map1_canvas.grid(row=1, column=0, padx=10, pady=10)
        self.map1_canvas.create_image(0, 0, anchor="nw", image=self.map1_image)

        # Load the second map image and resize it
        map2_image = Image.open("map2.jpg")
        map2_image = map2_image.resize((300, 300), Image.ANTIALIAS)

        # Convert the second map image to a PhotoImage and add it to the second canvas
        self.map2_image = ImageTk.PhotoImage(map2_image)
        self.map2_canvas = tk.Canvas(self.master, width=self.map2_image.width(), height=self.map2_image.height())
        self.map2_canvas.grid(row=1, column=1, padx=10, pady=10)
        self.map2_canvas.create_image(0, 0, anchor="nw", image=self.map2_image)

        # Add other widgets to the GUI
        self.label = tk.Label(self.master, text="Welcome to TCU's Campus Store!")
        self.label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.button = tk.Button(self.master, text="Find my way!", command=self.on_button_click)
        self.button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

    def on_button_click(self):
        # Show the maps
        self.map1_canvas.grid(row=1, column=0, padx=10, pady=10)
        self.map2_canvas.grid(row=1, column=1, padx=10, pady=10)

        # Hide the initial label and button
        self.label.grid_forget()
        self.button.grid_forget()

        # Add the section selection label and radio buttons
        self.section_label = tk.Label(self.master, text="Please select your current section:")
        self.section_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.selected_section = tk.StringVar(value="None")
        self.selected_section_list = []

        self.cashier_radio = tk.Radiobutton(self.master, text="Cashier", variable=self.selected_section, value="Cashier")
        self.cashier_radio.grid(row=3, column=0, padx=5, pady=5)

        self.starbucks_radio = tk.Radiobutton(self.master, text="Starbucks", variable=self.selected_section, value="Starbucks")
        self.starbucks_radio.grid(row=4, column=0, padx=5, pady=5)

        self.hats_radio = tk.Radiobutton(self.master, text="Hats", variable=self.selected_section, value="Hats")
        self.hats_radio.grid(row=5, column=0, padx=5, pady=5)

        self.mens_radio = tk.Radiobutton(self.master, text="Men's Clothing", variable=self.selected_section, value="Men's Clothing")
        self.mens_radio.grid(row=6, column=0, padx=5, pady=5)

        self.womens_radio = tk.Radiobutton(self.master, text="Women's Clothing", variable=self.selected_section, value="Women's Clothing")
        self.womens_radio.grid(row=3, column=1, padx=5, pady=5)

        self.fan_gear_radio = tk.Radiobutton(self.master, text="Fan Gear", variable=self.selected_section, value="Fan Gear")
        self.fan_gear_radio.grid(row=4, column=1, padx=5, pady=5)

        self.electronics_radio = tk.Radiobutton(self.master, text="Electronics", variable=self.selected_section, value="Electronics")
        self.electronics_radio.grid(row=5, column=1, padx=5, pady=5)

        self.supplies_radio = tk.Radiobutton(self.master, text="Supplies", variable=self.selected_section, value="Supplies")
        self.supplies_radio.grid(row=6, column=1, padx=5, pady=5)

        self.books_radio = tk.Radiobutton(self.master, text="Books", variable=self.selected_section, value="Books")
        self.books_radio.grid(row=3, column=2, padx=5, pady=5)

        self.clerk_radio = tk.Radiobutton(self.master, text="Clerk", variable=self.selected_section, value="Clerk")
        self.clerk_radio.grid(row=4, column=2, padx=5, pady=5)

        self.textbooks_radio = tk.Radiobutton(self.master, text="Textbooks", variable=self.selected_section, value="Textbooks")
        self.textbooks_radio.grid(row=5, column=2, padx=5, pady=5)

        # Add the section selection submit button
        self.section_submit_button = tk.Button(self.master, text="Submit", command=self.on_section_submit)
        self.section_submit_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

    def on_section_submit(self):
        # Get the selected section
        selected_section = self.selected_section.get()

        # If no section is selected, show an error message
        if selected_section == "None":
            error_message = tk.Label(self.master, text="Please select a section.", fg="red")
            error_message.grid(row=8, column=0, padx=10, pady=10, columnspan=2)
            error_message.after(1000, error_message.destroy)  # hide the error message after 3 seconds
            return

        # Destroy the section selection label and radio buttons
        self.section_label.destroy()
        self.mens_radio.destroy()
        self.womens_radio.destroy()
        self.hats_radio.destroy()
        self.fan_gear_radio.destroy()
        self.textbooks_radio.destroy()
        self.electronics_radio.destroy()
        self.supplies_radio.destroy()
        self.books_radio.destroy()
        self.cashier_radio.destroy()
        self.starbucks_radio.destroy()
        self.clerk_radio.destroy()
        self.section_submit_button.destroy()

        # Add the item selection label and check boxes
        self.item_label = tk.Label(self.master, text="Please select what you want to buy. Select at least one.")
        self.item_label.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

        self.selected_items = {}
        self.item_values = {
            "Men's Clothing": tk.StringVar(value=""),
            "Women's Clothing": tk.StringVar(value=""),
            "Hats": tk.StringVar(value=""),
            "Fan Gear": tk.StringVar(value=""),
            "Textbooks": tk.StringVar(value=""),
            "Electronics": tk.StringVar(value=""),
            "Supplies": tk.StringVar(value="")
        }

        self.mens_clothing_check = tk.Checkbutton(self.master, text="Men's Clothing", variable=self.item_values["Men's Clothing"],  onvalue="Men's Clothing", offvalue="")
        self.mens_clothing_check.grid(row=3, column=0, padx=5, pady=5)
        self.selected_items["Men's Clothing"] = self.item_values["Men's Clothing"]

        self.womens_clothing_check = tk.Checkbutton(self.master, text="Women's Clothing", variable=self.item_values["Women's Clothing"], onvalue="Women's Clothing", offvalue="")
        self.womens_clothing_check.grid(row=3, column=1, padx=5, pady=5)
        self.selected_items["Women's Clothing"] = self.item_values["Women's Clothing"]

        self.hats_check = tk.Checkbutton(self.master, text="Hats", variable=self.item_values["Hats"], onvalue="Hats", offvalue="")
        self.hats_check.grid(row=4, column=0, padx=5, pady=5)
        self.selected_items["Hats"] = self.item_values["Hats"]

        self.fan_gear_check = tk.Checkbutton(self.master, text="Fan Gear", variable=self.item_values["Fan Gear"], onvalue="Fan Gear", offvalue="")
        self.fan_gear_check.grid(row=4, column=1, padx=5, pady=5)
        self.selected_items["Fan Gear"] = self.item_values["Fan Gear"]

        self.textbooks_check = tk.Checkbutton(self.master, text="Textbooks", variable=self.item_values["Textbooks"], onvalue="Textbooks", offvalue="")
        self.textbooks_check.grid(row=5, column=0, padx=5, pady=5)
        self.selected_items["Textbooks"] = self.item_values["Textbooks"]

        self.electronics_check = tk.Checkbutton(self.master, text="Electronics", variable=self.item_values["Electronics"], onvalue="Electronics", offvalue="")
        self.electronics_check.grid(row=5, column=1, padx=5, pady=5)
        self.selected_items["Electronics"] = self.item_values["Electronics"]

        self.supplies_check = tk.Checkbutton(self.master, text="Supplies", variable=self.item_values["Supplies"], onvalue="Supplies", offvalue="")
        self.supplies_check.grid(row=6, column=0, padx=5, pady=5)
        self.selected_items["Supplies"] = self.item_values["Supplies"]


        self.item_submit_button = tk.Button(self.master, text="Next", command=self.on_submit)
        self.item_submit_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

    def on_submit(self):
        selected = [item for item in self.selected_items.keys() if self.selected_items[item].get()]
        if len(selected) == 0:
            messagebox.showerror("Error", "Please select at least one item.")
        else:
            messagebox.showinfo("Success", f"Selected items: {', '.join(selected)}")

        # Get the selected section
        selected_section = self.selected_section.get()

        # Display the selected section and items
        message = f"You selected {', '.join(selected)} from the {selected_section} section. "
        message += "To find these items, please follow the signs to the appropriate aisle."
        message_label = tk.Label(self.master, text=message)
        message_label.grid(row=8, column=0, padx=10, pady=10, columnspan=2)

        

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = MyGUI(root)
    root.mainloop()
