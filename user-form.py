from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

# TODO:
# - Final stylings


class CustomerInfoWindow:

    def __init__(self, root):
        
        validateInteger  = root.register(self.validate_int)
        root.title("Profiilin syötteet käyttäen gridiä")
        root.geometry("450x250")
        mainframe = ttk.Frame(root, padding=8)
        mainframe.grid(column=0, row=0)

        header_text = "Täytä tietosi:"
        name_text = "Nimi"
        eye_color_text = "Silmän väri"
        height_text = "Pituus"
        height_unit_text = "cm"
        weight_text = "Paino"
        weight_unit_text = "kg"
        default_entry_width = 30
        #default_entry_height = 5
        half_entry_width = default_entry_width // 2
        #default_entry_padx = "0 5"
        default_entry_pady = "0 5"
        #button_default_padding = 5
        gender_text = 'Valitse sukupuoli'
        gender_values = ('Mies', 'Nainen', 'Muu')

        self.height_var = StringVar()
        
        self.load_pic_placeholder = Image.open("./media/profile-pic-placeholder.png")
        self.load_pic_placeholder.thumbnail((150, 100))  # dimensions
        self.profile_picture = ImageTk.PhotoImage(self.load_pic_placeholder)

        import_picture_button = ttk.Button(mainframe, text="Lisää kuva", command=self.open_image)
        import_picture_button.grid(column=0, row=1)
        self.picture_field = ttk.Label(mainframe, width=150, image=self.profile_picture)
        self.picture_field.image = self.profile_picture
        self.picture_field.grid(column=0, row=2, rowspan=3,
                           sticky=N)

        header_info = ttk.Label(mainframe, text=header_text)
        header_info.grid(column=1, row=0, columnspan=2)

        name_entry_text = ttk.Label(mainframe, text=name_text)
        name_entry_text.grid(column=1, row=1, sticky=E)
        name_entry = ttk.Entry(mainframe, width=default_entry_width)
        name_entry.grid(column=2, row=1, sticky=W, pady=default_entry_pady)

        gender_dropdown = ttk.Combobox(mainframe, values=gender_values, state="readonly", width=half_entry_width)
        gender_dropdown.set(gender_text)
        gender_dropdown.grid(column=2, row=2, sticky=W, ipady=2, pady=default_entry_pady)

        eye_color_entry_text = ttk.Label(mainframe, text=eye_color_text)
        eye_color_entry_text.grid(column=1, row=3, sticky=E, pady=default_entry_pady)
        eye_color_entry = ttk.Entry(mainframe, width=default_entry_width)
        eye_color_entry.grid(column=2, row=3, sticky=W, pady=default_entry_pady)

        height_entry_text = ttk.Label(mainframe, text=height_text)
        height_entry_text.grid(column=1, row=4, sticky=E, pady=default_entry_pady)
        height_entry = ttk.Entry(mainframe, textvariable=self.height_var, width=default_entry_width, validate='all', validatecommand=(validateInteger, '%S'))
        height_entry.grid(column=2, row=4, sticky=W, pady=default_entry_pady)
        height_entry_unit_text = ttk.Label(mainframe, text=height_unit_text)
        height_entry_unit_text.grid(column=3, row=4, sticky=W, pady=default_entry_pady)

        weight_entry_text = ttk.Label(mainframe, text=weight_text)
        weight_entry_text.grid(column=1, row=5, sticky=E, pady=default_entry_pady)
        weight_entry = ttk.Entry(mainframe, width=default_entry_width, validate='all', validatecommand=(validateInteger, '%S'))
        weight_entry.grid(column=2, row=5, sticky=W, pady=default_entry_pady)
        weight_entry_unit_text = ttk.Label(mainframe, text=weight_unit_text)
        weight_entry_unit_text.grid(column=3, row=5, sticky=W, pady=default_entry_pady)

    def validate_int(self, height: int):
        try:
            int(height)
            return True
        except ValueError:
            return False
        
    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            load_image = Image.open(file_path)
            load_image.thumbnail((150, 100))
            image = ImageTk.PhotoImage(load_image)

            self.picture_field.configure(image=image)
            self.picture_field.image = image


root = Tk()
CustomerInfoWindow(root)
root.mainloop()
