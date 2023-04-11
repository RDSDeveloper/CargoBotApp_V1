# Este script inicia la aplicacion

from tkinter import Label, PhotoImage

from action_buttons import *
from cargobot_files import *
from hide_terminal import *
from menu_buttons import *


# Iniciar aplicacion 

# hide_terminal() esta marcado porque sino me cierra VSCODE
create_cargobot_files_folder()
root.mainloop()  