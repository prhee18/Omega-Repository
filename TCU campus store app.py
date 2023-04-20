import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class MyGUI:

    def __init__(self, master):
        self.master = master
        self.container = tk.Frame(self.master)
        self.master.title("TCU Campus Store App")
        self.master.config(bg= "#B2A4D4")
        

        # Create the header frame and set the background color to TCU's purple
        self.header_frame = tk.Frame(self.master, bg="#4d1979")
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Load the logo image and resize it
        logo_image = Image.open("client_logo.jpg")
        logo_image = logo_image.resize((80, 80), Image.ANTIALIAS)

        # Convert the logo image to a PhotoImage and add it to the logo canvas
        self.logo_image = ImageTk.PhotoImage(logo_image)
        self.logo_canvas = tk.Canvas(self.header_frame, width=self.logo_image.width(), height=self.logo_image.height(), bg="#4d1979", highlightthickness=0)
        self.logo_canvas.pack(side="left", padx=10, pady=10)
        self.logo_canvas.create_image(0, 0, anchor="nw", image=self.logo_image)

        # Load the first map image and resize it
        map1_image = Image.open("campus store map.png")
        map1_image = map1_image.resize((700, 250), Image.ANTIALIAS)

        # Convert the first map image to a PhotoImage and add it to the first canvas
        self.map1_image = ImageTk.PhotoImage(map1_image)
        self.map1_canvas = tk.Canvas(self.master, width=self.map1_image.width(), height=self.map1_image.height())
        self.map1_canvas.grid(row=1, column=0, padx=10, pady=10)
        self.map1_canvas.create_image(0, 0, anchor="nw", image=self.map1_image)

        # Add other widgets to the GUI
        self.label = tk.Label(self.master, text="Welcome to TCU's Campus Store!", bg = "#fff0f5", font=("Arial", 12, "bold"))
        self.label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.button = tk.Button(self.master, text="Find my way!", bg="#d0f0c0", fg="black", font=("Arial", 10, "bold"), bd=3, relief="raised", width=10, height=2, command=self.on_button_click)
        self.button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)


    def on_button_click(self):  
        

        # Show the map in the container frame
        self.map1_canvas = tk.Canvas(self.container, width=500, height=300)
        self.map1_canvas.grid(row=0, column=0, padx=0, pady=0)

        # Hide the initial label and button
        self.label.grid_forget()
        self.button.grid_forget()

        # Create a new frame for radio buttons
        self.radio_frame = tk.Frame(self.master,bg = "#fff0f5")
        self.radio_frame.grid(row=3, column=0, padx=10, pady=10)

        # Add the section selection label and radio buttons

        self.section_label = tk.Label(self.master, text="Please select your current section:", bg = "#fff0f5", font=("Arial", 12, "bold"))
        self.section_label.grid(row=2, column=0, padx=5, pady=5, columnspan=1)
        self.section_label.columnconfigure(0, minsize = 0)

        self.selected_section = tk.StringVar(value="None")
        self.selected_section_list = []

        self.cashier_radio = tk.Radiobutton(self.radio_frame, text="Cashier", variable=self.selected_section, value="Cashier", bg="#fff0f5")
        self.cashier_radio.grid(row=3, column=0, padx=(0,0), pady=0, sticky="w")

        self.starbucks_radio = tk.Radiobutton(self.radio_frame, text="Starbucks", variable=self.selected_section, value="Starbucks", bg="#fff0f5")
        self.starbucks_radio.grid(row=4, column=0, padx=0, pady=0, sticky="w")

        self.hats_radio = tk.Radiobutton(self.radio_frame, text="Hats", variable=self.selected_section, value="Hats", bg="#fff0f5")
        self.hats_radio.grid(row=5, column=0, padx=0, pady=0, sticky="w")

        self.mens_radio = tk.Radiobutton(self.radio_frame, text="Men's Clothing", variable=self.selected_section, value="Men's Clothing", bg="#fff0f5")
        self.mens_radio.grid(row=6, column=0, padx=0, pady=0, sticky="w")

        self.womens_radio = tk.Radiobutton(self.radio_frame, text="Women's Clothing", variable=self.selected_section, value="Women's Clothing", bg="#fff0f5")
        self.womens_radio.grid(row=7, column=0, padx=0, pady=0, sticky="w")

        self.fan_gear_radio = tk.Radiobutton(self.radio_frame, text="Fan Gear", variable=self.selected_section, value="Fan Gear", bg="#fff0f5")
        self.fan_gear_radio.grid(row=3, column=1, padx=0, pady=0, sticky="w")

        self.electronics_radio = tk.Radiobutton(self.radio_frame, text="Electronics", variable=self.selected_section, value="Electronics", bg="#fff0f5")
        self.electronics_radio.grid(row=4, column=1, padx=0, pady=0, sticky="w")

        self.supplies_radio = tk.Radiobutton(self.radio_frame, text="Supplies", variable=self.selected_section, value="Supplies", bg="#fff0f5")
        self.supplies_radio.grid(row=5, column=1, padx=0, pady=0, sticky="w")

        self.books_radio = tk.Radiobutton(self.radio_frame, text="Books", variable=self.selected_section, value="Books", bg="#fff0f5")
        self.books_radio.grid(row=6, column=1, padx=0, pady=0, sticky="w")

        self.clerk_radio = tk.Radiobutton(self.radio_frame, text="Clerk", variable=self.selected_section, value="Clerk", bg="#fff0f5")
        self.clerk_radio.grid(row=7, column=1, padx=0, pady=0, sticky="w")

        self.textbooks_radio = tk.Radiobutton(self.radio_frame, text="Textbooks", variable=self.selected_section, value="Textbooks", bg="#fff0f5")
        self.textbooks_radio.grid(row=8, column=1, padx=0, pady=0, sticky="w")

        # Add the section selection submit button
        self.section_submit_button = tk.Button(self.master, bg="#d0f0c0", fg="black", font=("Arial", 10, "bold"), bd=3, relief="raised", width=5, height=1, text="Next", command=self.on_section_submit, anchor="center")
        self.section_submit_button.grid(row=9, column=0, padx=10, pady=10, columnspan=2)

    def on_section_submit(self):
        # Get the selected section
        selected_section = self.selected_section.get()

        # If no section is selected, show an error message
        if selected_section == "None":
            error_message = tk.Label(self.master, text="Please select a section.", fg="red", bg = "#fff0f5", font=("Arial", 12, "bold"))
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

        # Create a new frame for radio buttons
        self.checkbox_frame = tk.Frame(self.master, bg = "#fff0f5")
        self.checkbox_frame.grid(row=3, column=0, padx=10, pady=10)

        # Add the item selection label and check boxes
        self.item_label = tk.Label(self.master, text="Please select what you want to buy. Select at least one.", bg = "#fff0f5", font=("Arial", 12, "bold"))
        self.item_label.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

        self.selected_items = {}
        self.item_values = {
            "Men's Clothing": tk.StringVar(value=""),
            "Women's Clothing": tk.StringVar(value=""),
            "Hats": tk.StringVar(value=""),
            "Fan Gear": tk.StringVar(value=""),
            "Textbooks": tk.StringVar(value=""),
            "Electronics": tk.StringVar(value=""),
            "Supplies": tk.StringVar(value=""),
            "Books": tk.StringVar(value=""),
        }

        self.mens_clothing_check = tk.Checkbutton(self.checkbox_frame, text="Men's Clothing", variable=self.item_values["Men's Clothing"],  onvalue="Men's Clothing", offvalue="", bg="#fff0f5")
        self.mens_clothing_check.grid(row=3, column=0, padx=0, pady=5, sticky="w")
        self.selected_items["Men's Clothing"] = self.item_values["Men's Clothing"]

        self.womens_clothing_check = tk.Checkbutton(self.checkbox_frame, text="Women's Clothing", variable=self.item_values["Women's Clothing"], onvalue="Women's Clothing", offvalue="", bg="#fff0f5")
        self.womens_clothing_check.grid(row=4, column=0, padx=0, pady=5, sticky="w")
        self.selected_items["Women's Clothing"] = self.item_values["Women's Clothing"]

        self.hats_check = tk.Checkbutton(self.checkbox_frame, text="Hats", variable=self.item_values["Hats"], onvalue="Hats", offvalue="", bg="#fff0f5")
        self.hats_check.grid(row=5, column=0, padx=0, pady=0, sticky="w")
        self.selected_items["Hats"] = self.item_values["Hats"]

        self.fan_gear_check = tk.Checkbutton(self.checkbox_frame, text="Fan Gear", variable=self.item_values["Fan Gear"], onvalue="Fan Gear", offvalue="",  bg="#fff0f5")
        self.fan_gear_check.grid(row=6, column=0, padx=0, pady=0, sticky= "w")
        self.selected_items["Fan Gear"] = self.item_values["Fan Gear"]

        self.textbooks_check = tk.Checkbutton(self.checkbox_frame, text="Textbooks", variable=self.item_values["Textbooks"], onvalue="Textbooks", offvalue="",  bg="#fff0f5")
        self.textbooks_check.grid(row=3, column=1, padx=0, pady=0, sticky="w")
        self.selected_items["Textbooks"] = self.item_values["Textbooks"]

        self.electronics_check = tk.Checkbutton(self.checkbox_frame, text="Electronics", variable=self.item_values["Electronics"], onvalue="Electronics", offvalue="", bg="#fff0f5")
        self.electronics_check.grid(row=4, column=1, padx=0, pady=0, sticky= "w")
        self.selected_items["Electronics"] = self.item_values["Electronics"]

        self.supplies_check = tk.Checkbutton(self.checkbox_frame, text="Supplies", variable=self.item_values["Supplies"], onvalue="Supplies", offvalue="", bg="#fff0f5")
        self.supplies_check.grid(row=5, column=1, padx=0, pady=0, sticky="w")
        self.selected_items["Supplies"] = self.item_values["Supplies"]

        self.supplies_check = tk.Checkbutton(self.checkbox_frame, text="Books", variable=self.item_values["Books"], onvalue="Books", offvalue="", bg="#fff0f5")
        self.supplies_check.grid(row=6, column=1, padx=0, pady=0, sticky="w")
        self.selected_items["Books"] = self.item_values["Books"]

        self.item_submit_button = tk.Button(self.master, text="Find your way!", command=self.on_submit, bg = "#d0f0c0", font=("Arial", 10, "bold"))
        self.item_submit_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

    def on_submit(self):
        selected = [item for item in self.selected_items.keys() if self.selected_items[item].get()]
        if len(selected) == 0:
            messagebox.showerror("Error", "Please select at least one item.")
        else:
            messagebox.showinfo("Success", f"Selected items: {', '.join(selected)}")
            # Get the selected section
            selected_section = self.selected_section.get()

            #Write the logic for the shortest path through TCU campus store
            distance_dict = {"Cashier": 1, "Starbucks": 2, "Hats": 3, "Men's Clothing": 4, "Women's Clothing": 5, "Fan Gear": 6, "Supplies": 7, "Electronics": 8, "Textbooks": 9, "Books": 10, "Clerk": 11}

            '''The logic for finding the shortest path is as follows: if the selected item list match the item in distance dict, 
            then the user will just go to the location with the highest number, the second highest, etc. and down to the last definitive location, which is the cashier'''

            #Match number in distance_dict with item in selected list
            number_list = []
            for item in selected:
                number_list.append(distance_dict[item])
            #Sort the number list from largest to smallest
            number_list.sort(reverse=True)
            print(number_list)
            #Match the number in number list with the items in distance dict
            sorted_items = []
            for number in number_list:
                for item in distance_dict:
                    if number == distance_dict[item]:
                        sorted_items.append(item)
            
            #Destroy Next button
            self.item_submit_button.destroy()

            # Display the selected section and items
            message = f"You selected {', '.join(selected)}, and you're going from the {selected_section} section. "
            for i in range(len(number_list)): 
                if i == 0:
                    message += f"\n To find these items, please follow the following instructions:\n"
                    if sorted_items[0] == selected_section:
                        message += f"You're already at the {selected_section} section, so go to second step;"
                    else: 
                        if sorted_items[0] == "Cashier" or sorted_items[0] == "Starbucks" or sorted_items[0] == "Fan Gear" or sorted_items[0] == "Women's Clothing" or sorted_items[0] == "Men's Clothing" or sorted_items[0] == "Hats":
                            message += f"First, go to the first floor"
                        if sorted_items[0] ==  "Supplies" or sorted_items[0] == "Electronics" or sorted_items[0] == "Textbooks" or sorted_items[0] == "Books" or sorted_items[0] == "Clerk":
                            message += f"First, go to the second floor"
                        message += f" and go to {sorted_items[0]};"
                elif i == 1:
                    message += f"\n Second,"
                    if "go to the first floor" in message:
                        if sorted_items[1] ==  "Supplies" or sorted_items[1] == "Electronics" or sorted_items[1] == "Textbooks" or sorted_items[1] == "Books" or sorted_items[1] == "Clerk":
                            message += f" go to the second floor and"
                    elif "go to the second floor" in message:
                        if sorted_items[1] == "Cashier" or sorted_items[1] == "Starbucks" or sorted_items[1] == "Fan Gear" or sorted_items[1] == "Women's Clothing" or sorted_items[1] == "Men's Clothing" or sorted_items[1] == "Hats":
                            message += f" go to the first floor and"
                    message += f" go to {sorted_items[1]};"
                elif i == 2:
                    message += f"\n Third,"
                    if "go to the first floor" in message:
                        if sorted_items[2] ==  "Supplies" or sorted_items[2] == "Electronics" or sorted_items[2] == "Textbooks" or sorted_items[2] == "Books" or sorted_items[2] == "Clerk":
                            message += f" go to the second floor and"
                    elif "go to the second floor" in message:
                        if sorted_items[2] == "Cashier" or sorted_items[2] == "Starbucks" or sorted_items[2] == "Fan Gear" or sorted_items[2] == "Women's Clothing" or sorted_items[2] == "Men's Clothing" or sorted_items[2] == "Hats":
                            message += f" go to the first floor and"
                    message += f" go to {sorted_items[2]};"
                elif i == 3:
                    message += f"\n Fourth,"
                    if "go to the first floor" in message:
                        if sorted_items[3] ==  "Supplies" or sorted_items[3] == "Electronics" or sorted_items[3] == "Textbooks" or sorted_items[3] == "Books" or sorted_items[3] == "Clerk":
                            message += f" go to the second floor and"
                    elif "go to the second floor" in message:
                        if sorted_items[3] == "Cashier" or sorted_items[3] == "Starbucks" or sorted_items[3] == "Fan Gear" or sorted_items[3] == "Women's Clothing" or sorted_items[3] == "Men's Clothing" or sorted_items[3] == "Hats":
                            message += f" go to the first floor and"
                    message += f" go to {sorted_items[3]};"       
                elif i == 4:
                    message += f"\n Fifth,"
                    if "go to the first floor" in message:
                        if sorted_items[4] ==  "Supplies" or sorted_items[4] == "Electronics" or sorted_items[4] == "Textbooks" or sorted_items[4] == "Books" or sorted_items[4] == "Clerk":
                            message += f" go to the second floor and"
                    elif "go to the second floor" in message:
                        if sorted_items[4] == "Cashier" or sorted_items[4] == "Starbucks" or sorted_items[4] == "Fan Gear" or sorted_items[4] == "Women's Clothing" or sorted_items[4] == "Men's Clothing" or sorted_items[4] == "Hats":
                            message += f" go to the first floor and"
                    message += f" go to {sorted_items[4]};"  
                elif i == 5:
                    message += f"\n Sixth,"
                    if "go to the first floor" in message:
                        if sorted_items[5] ==  "Supplies" or sorted_items[5] == "Electronics" or sorted_items[5] == "Textbooks" or sorted_items[5] == "Books" or sorted_items[5] == "Clerk":
                            message += f" go to the second floor and"
                    elif "go to the second floor" in message:
                        if sorted_items[5] == "Cashier" or sorted_items[5] == "Starbucks" or sorted_items[5] == "Fan Gear" or sorted_items[5] == "Women's Clothing" or sorted_items[5] == "Men's Clothing" or sorted_items[5] == "Hats":
                            message += f" go to the first floor and"
                    message += f" go to {sorted_items[5]};"  
                elif i == 6:
                    message += f"\n Seventh,"
                    if "go to the first floor" in message:
                        if sorted_items[6] ==  "Supplies" or sorted_items[6] == "Electronics" or sorted_items[6] == "Textbooks" or sorted_items[6] == "Books" or sorted_items[6] == "Clerk":
                            message += f" go to the second floor and"
                    elif "go to the second floor" in message:
                        if sorted_items[6] == "Cashier" or sorted_items[6] == "Starbucks" or sorted_items[6] == "Fan Gear" or sorted_items[6] == "Women's Clothing" or sorted_items[6] == "Men's Clothing" or sorted_items[6] == "Hats":
                            message += f" go to the first floor and"
                    message += f" go to {sorted_items[6]};"  
                elif i == 7:
                    message += f"\n Eighth,"
                    if "go to the first floor" in message:
                        if sorted_items[7] ==  "Supplies" or sorted_items[7] == "Electronics" or sorted_items[7] == "Textbooks" or sorted_items[7] == "Books" or sorted_items[7] == "Clerk":
                            message += f" go to the second floor and"
                    elif "go to the second floor" in message:
                        if sorted_items[7] == "Cashier" or sorted_items[7] == "Starbucks" or sorted_items[7] == "Fan Gear" or sorted_items[7] == "Women's Clothing" or sorted_items[7] == "Men's Clothing" or sorted_items[7] == "Hats":
                            message += f" go to the first floor and"
                    message += f" go to {sorted_items[7]};"
                elif i == 8:
                    message += f"\n Ninth,"
                    if "go to the first floor" in message:
                        if sorted_items[8] ==  "Supplies" or sorted_items[8] == "Electronics" or sorted_items[8] == "Textbooks" or sorted_items[8] == "Books" or sorted_items[8] == "Clerk":
                            message += f" go to the second floor and"
                    elif "go to the second floor" in message:
                        if sorted_items[8] == "Cashier" or sorted_items[8] == "Starbucks" or sorted_items[8] == "Fan Gear" or sorted_items[8] == "Women's Clothing" or sorted_items[8] == "Men's Clothing" or sorted_items[8] == "Hats":
                            message += f" go to the first floor and"
                    message += f" go to {sorted_items[8]};"

            message += f"\n Finally, go to the cashier on the first floor and pay for your items."
            
            message_label = tk.Label(self.master, text=message, bg="#fff0f5")
            message_label.grid(row=8, column=0, padx=10, pady=10, columnspan=2)
            
if __name__ == "__main__":
    root = tk.Tk()
    
    # Set a fixed size for column 1
    root.columnconfigure(1, minsize=10)
    my_gui = MyGUI(root)
    root.mainloop()
