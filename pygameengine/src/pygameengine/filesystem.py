"""
Contains everything related to using the filesystem in pge
"""
import tkinter.filedialog


def prompt_file(filetypes: list[tuple[str]], savedialog: bool = False) -> None:
    """
    Create a Tk file dialog with whatever filetypes provided. I recommend looking into the actual source code for this function as it is very simple to do yourself.
    :param filetypes: The types of files to allow in the prompt using ("extended name", "extension")
    :param savedialog: The option to use the saving dialog (optional defaults to False)
    :return: None
    """
    top = tkinter.Tk()
    top.withdraw()  # hide window
    if not savedialog:
        file_name = tkinter.filedialog.askopenfilename(parent=top, filetypes=filetypes)
    else:
        file_name = tkinter.filedialog.asksaveasfilename(parent=top, filetypes=filetypes)
    top.destroy()
    return file_name
