from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class CustomerInfoWindow:

    def __init__(self, root):
        
        root.title("Asiakastiedot")
        mainframe = ttk.Frame(root, padding=8)
        mainframe.grid(column=0, row=0)
        footerframe = ttk.Frame(root)
        footerframe.grid(column=0, row=8)

        style = ttk.Style()
        style.configure('Custom.TButton', foreground='red',
                        background='yellow')

        header_text = "ASIAKASTIEDOT"
        customer_number_text = "Asiakasnro:"
        company_name_text = "Yrityksen nimi:"
        contact_name_text = "Yhteyshenkilö:"
        post_number_text = "PostiNro:"
        post_address_text = "Postitoimipaikka:"
        phone_number_text = "Puhelin:"
        more_info_text = "Lisätietoja:"
        zoomin_button_text = "Suurenna"
        zoomout_button_text = "Pienennä"
        save_button_text = "TALLENNA"
        delete_button_text = "POISTA"
        default_entry_width = 20
        default_entry_height = 5
        half_entry_width = default_entry_width // 2
        default_entry_padx = "0 5"
        default_entry_pady = "0 5"
        button_default_padding = 5

        self.current_zoom = 1

        second_column_default_padx = "50 20"

        def footer_options(text: str, command) -> dict:
            return {
                    "text": text,
                    "width": 10,
                    "padx": button_default_padding,
                    "pady": button_default_padding,
                    "command": command,
                    "bg": "#1976d2",
                    "font": ('Default', 10, 'bold'),
                    "fg": "white",
                    "activebackground": "#1976d2",
                    "relief": "flat",
                    "borderwidth": 1,
                    }

        self.load_profile_image = Image.open("./media/pic.jpg")
        self.load_profile_image.thumbnail((250, 200))  # dimensions
        self.profile_picture = ImageTk.PhotoImage(self.load_profile_image)

        header = ttk.Label(mainframe, text=header_text,
                           font=("default", 16, "bold"))
        header.grid(column=0, row=0, columnspan=2, sticky=W, pady="0 10")

        customer_number = ttk.Label(mainframe, text=customer_number_text)
        customer_number.grid(column=0, row=1, sticky=W,
                             padx=default_entry_padx, pady=default_entry_pady)
        customer_number_entry = ttk.Entry(mainframe, width=default_entry_width)
        customer_number_entry.grid(column=1, row=1, sticky=W)

        company_name = ttk.Label(mainframe, text=company_name_text)
        company_name.grid(column=0, row=2, sticky=W,
                          padx=default_entry_padx, pady=default_entry_pady)
        company_name_entry = ttk.Entry(mainframe, width=default_entry_width)
        company_name_entry.grid(column=1, row=2, sticky=W)

        contact_name = ttk.Label(mainframe, text=contact_name_text)
        contact_name.grid(column=0, row=3, sticky=W,
                          padx=default_entry_padx, pady=default_entry_pady)
        contact_name_entry = ttk.Entry(mainframe, width=default_entry_width)
        contact_name_entry.grid(column=1, row=3, sticky=W)

        post_number = ttk.Label(mainframe, text=post_number_text)
        post_number.grid(column=0, row=4, sticky=W,
                         padx=default_entry_padx, pady=default_entry_pady)
        post_number_entry = ttk.Entry(mainframe, width=half_entry_width)
        post_number_entry.grid(column=1, row=4, sticky=W)

        post_address = ttk.Label(mainframe, text=post_address_text)
        post_address.grid(column=0, row=5, sticky=W,
                          padx=default_entry_padx, pady=default_entry_pady)
        post_address_entry = ttk.Entry(mainframe, width=default_entry_width)
        post_address_entry.grid(column=1, row=5, sticky=W)

        phone_number = ttk.Label(mainframe, text=phone_number_text)
        phone_number.grid(column=0, row=6, sticky=W,
                          padx=default_entry_padx, pady=default_entry_pady)
        phone_number_entry = ttk.Entry(mainframe, width=default_entry_width)
        phone_number_entry.grid(column=1, row=6, sticky=W)

        more_info = ttk.Label(mainframe, text=more_info_text)
        more_info.grid(column=0, row=7, sticky=NW,
                       padx=default_entry_padx, pady=default_entry_pady)
        more_info_entry = Text(mainframe, width=15, height=default_entry_height)
        more_info_entry.grid(column=1, row=7, sticky=W)

        ### Columns 2-3 ###

        self.picture_field = ttk.Label(mainframe, image=self.profile_picture)
        self.picture_field.image = self.profile_picture
        self.picture_field.grid(column=2, row=1, rowspan=7, columnspan=2,
                           sticky=N, padx=second_column_default_padx)

        zoomin_button = ttk.Button(
            mainframe, text=zoomin_button_text, padding=button_default_padding, command=self.zoomin)
        zoomin_button.grid(column=2, row=7, sticky=W,
                           padx=second_column_default_padx)

        zoomout_button = ttk.Button(
            mainframe, text=zoomout_button_text, padding=button_default_padding, command=self.zoomout)
        zoomout_button.grid(column=3, row=7, sticky=E,
                            padx=second_column_default_padx)

        ## Row 8 (footerframe) ##

        save_button = Button(footerframe, footer_options(save_button_text, self.save))
        save_button.grid(column=0, row=0, pady=20, padx=20)

        delete_button = Button(footerframe, footer_options(delete_button_text, self.delete))
        delete_button.grid(column=1, row=0, pady=20, padx=20)

    def save(self, *args):
        print("Pressed Save")

    def delete(self, *args):
        print("Pressed Delete")

    def zoomin(self, *args):
        print("Pressed Zoomin")
        width, height = self.load_profile_image.size
        if self.current_zoom > 0:
            self.current_zoom += 0.05
        new_width = int(width * self.current_zoom)
        new_height = int(height * self.current_zoom)
        zoomed_image = self.load_profile_image.resize((new_width, new_height))
        self.profile_picture = ImageTk.PhotoImage(zoomed_image)
        self.picture_field.config(image=self.profile_picture)

    def zoomout(self, *args):
        print("Pressed Zoomout")
        width, height = self.load_profile_image.size
        if self.current_zoom > 0.05:
            self.current_zoom -= 0.05
        new_width = int(width * self.current_zoom)
        new_height = int(height * self.current_zoom)
        zoomed_image = self.load_profile_image.resize((new_width, new_height))
        self.profile_picture = ImageTk.PhotoImage(zoomed_image)
        self.picture_field.config(image=self.profile_picture)

root = Tk()
CustomerInfoWindow(root)
root.mainloop()
