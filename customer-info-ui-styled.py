from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk


class App(tb.Window):
    def __init__(self, title, size, theme='darkly'):
        '''
        # Main window
        ### Parameters:
        - title: Title of the app
        - size: x and y dimensions of the window. This is also the minimum size
        - theme: your custom theme or one of the above:\n
                  'cosmo', 'flatly', 'litera',\n
                  'minty', 'lumen', 'sandstone', 'yeti',\n
                  'pulse', 'united', 'morph', 'journal',\n
                  'darkly', 'superhero', 'solar',\n
                  'cyborg', 'vapor', 'simplex', 'cerculean'
        '''
        super().__init__(themename=theme)
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        self.main = Main(self)
        self.mainloop()

    def change_theme(self, theme):
        self.style.theme_use(theme)


class Main(tb.Frame):
    def __init__(self, parent):
        '''
        # Main window
        Has profile picture on the left side and\n
        personal information form on the right side
        '''
        self.parent = parent
        default_entry_width = 30
        half_entry_width = default_entry_width // 2

        left_frame = tb.Frame(self.parent, padding=8, width=2)
        left_frame.grid(column=0, row=0, sticky=N)
        right_frame = tb.Frame(self.parent, padding=8)
        right_frame.grid(column=1, row=0, sticky=N)
        ImageWithImport(left_frame,
                        row_and_column=(0, 1),
                        image_path='./media/profile-pic-placeholder.png',
                        image_dimensions=(150, 150),
                        button_text='Lisää kuva',
                        customizations={})

        Label(right_frame, (0, 0), 'Täytä profiilitietosi:',
              customizations={'columnspan': 4})

        themes = self.parent.style.theme_names()
        current_theme = self.parent.style.theme_use()

        Select(right_frame, row_and_column=(0, 5), values=themes,
               placeholder=current_theme, customizations={'width': half_entry_width, 'on_select': self.combobox_selected})

        EntryWithLabel(right_frame, row_and_column=(1, 2), label_text='Nimi',
                       side_by_side=True, customizations={'entry-width': default_entry_width})

        Select(right_frame, row_and_column=(2, 3), values=('Mies', 'Nainen', 'Muu'), placeholder='Valitse sukupuoli',
               customizations={'width': half_entry_width})

        EntryWithLabel(right_frame, row_and_column=(3, 2), label_text='Silmänväri', side_by_side=True,
                       customizations={'entry-width': default_entry_width})

        EntryWithLabel(right_frame, row_and_column=(4, 2), label_text='Korkeus', side_by_side=True,
                       customizations={'entry-width': default_entry_width}, validate='number')
        Label(right_frame, (4, 4), 'cm')

        EntryWithLabel(right_frame, row_and_column=(5, 2), label_text='Paino', side_by_side=True,
                       customizations={'entry-width': default_entry_width}, validate='number')
        Label(right_frame, (5, 4), 'kg')

    def combobox_selected(self, value):
        print("Selected", value)
        self.parent.change_theme(value)


class ImageWithImport(tb.Frame):
    def __init__(self, parent, row_and_column: tuple, image_path: str, image_dimensions=(150, 150), button_text='Lisää kuva', customizations={}):
        '''
        Uses tkinter Label to show the image and\n
        has button on top to load image from disk.
        '''
        super().__init__(parent)
        default_customizations = {}

        if customizations is not None:
            for key, value in customizations.items():
                default_customizations[key] = value

        row, col = row_and_column
        load_image = Image.open(image_path)
        load_image = load_image.resize(image_dimensions)
        image = ImageTk.PhotoImage(load_image)

        import_picture_button = tb.Button(
            parent, text=button_text, command=lambda: self.open_image(image_dimensions))
        import_picture_button.grid(column=col, row=row)
        self.picture_field = tb.Label(parent, image=image)
        self.picture_field.image = image
        self.picture_field.grid(column=col, row=row+1, rowspan=3,
                                sticky=N)

    def open_image(self, image_dimensions: tuple):
        file_path = filedialog.askopenfilename(
            filetypes=[('Image files', '*.png;*.jpg;*.jpeg')])
        if file_path:
            load_image = Image.open(file_path)
            load_image = load_image.resize(image_dimensions)
            image = ImageTk.PhotoImage(load_image)

            self.picture_field.configure(image=image)
            self.picture_field.image = image


class Select(tb.Frame):
    def __init__(self, parent, row_and_column: tuple, values: tuple | list, placeholder: str, customizations=None):
        '''
        Uses tkinter Combobox and has on_select binding available\n
        in customizations that returns the selected value

        ### Parameters:
        - values: list or tuple of options that can be selected
        - placeholder: Text shown when nothing is selected
        - customizations: {'width': 100, 'sticky': W, 'state': 'readonly', 'pady': 5, 'on_select': self.bind_function}
        '''
        super().__init__(parent)
        default_customizations = {'width': 100,
                                  'sticky': W,
                                  'state': 'readonly',
                                  'pady': 5,
                                  'on_select': self.bind_function}

        if customizations is not None:
            for key, value in customizations.items():
                default_customizations[key] = value

        state = default_customizations['state']
        width = default_customizations['width']
        pady = default_customizations['pady']
        sticky = default_customizations['sticky']
        self.binded_command = default_customizations['on_select']
        row, col = row_and_column

        self.select = tb.Combobox(parent,
                                  values=values,
                                  state=state,
                                  width=width)
        
        self.select.set(placeholder)
        self.select.bind('<<ComboboxSelected>>', self.on_select)
        self.select.grid(row=row, column=col, sticky=sticky, pady=pady)

    def on_select(self, e):
        selected_value = self.select.get()
        self.binded_command(selected_value)

    def bind_function(self, e):
        pass


class EntryWithLabel(tb.Frame):
    def __init__(self, parent, row_and_column: tuple, label_text: str, entry_variable=None, side_by_side=False, validate=None, customizations=None):
        '''
        ttkbootsrap Entry and Label combo.\n
        Can be positioned either label ontop or side by side

        ### Parameters:
        - label_text: What is shown in the label
        - entry_variable: Binding variable for Entry
        - side_by_side: If True then Label is shown on left side and on the same row as the Entry
        - validate: 'number'
            - 'number': Only allows numbers to be inserted to the Entry
        - customizations: {'entry-width': 30, 'label-padding': 10}
        '''

        super().__init__(parent)
        default_customizations = {'entry-width': 30,
                                  'label-padding': 10}

        if customizations is not None:
            for key, value in customizations.items():
                default_customizations[key] = value

        row, col = row_and_column
        label_padding = default_customizations['label-padding']
        entry_width = default_customizations['entry-width']

        if side_by_side:
            entry_row = row
            entry_col = col + 1
        else:
            entry_row = row + 1
            entry_col = col

        label = tb.Label(parent, text=label_text, padding=label_padding)
        entry = tb.Entry(parent, textvariable=entry_variable,
                         width=entry_width)
        if validate == 'number':
            validatecommand = (self.register(self.validate_digit), '%P')
            entry.config(validate='key', validatecommand=validatecommand)

        label.grid(row=row, column=col, sticky='E')
        entry.grid(row=entry_row, column=entry_col)

    def validate_digit(self, new_text):
        if new_text.isdigit():
            return True
        elif new_text == '':
            return True
        else:
            return False


class Label(tb.Frame):
    def __init__(self, parent, row_and_column: tuple, text: str, customizations=None):
        '''
        ttkbootstrap Label with customizations
        ### Parameters:
        - row_and_column: tuple with row and column values - (0, 0)
        - text: What is shown in the label
        - customizations: {'sticky': None, 'columnspan': 1, 'justify': 'left'}
        '''
        super().__init__(parent)

        default_customizations = {'sticky': None,
                                  'columnspan': 1,
                                  'justify': 'left'}

        if customizations is not None:
            for key, value in customizations.items():
                default_customizations[key] = value

        sticky = default_customizations['sticky']
        colspan = default_customizations['columnspan']
        justify = default_customizations['justify']

        row, col = row_and_column

        label = tb.Label(parent, text=text, justify=justify)
        label.grid(row=row, column=col, columnspan=colspan, sticky=sticky)


App(title='Profiilin lisäys', size=(600, 300))
