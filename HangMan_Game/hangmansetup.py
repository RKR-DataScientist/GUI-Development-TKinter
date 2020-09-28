from cx_Freeze import *

includefile = ['hangman.ico']
base = None
if sys.platform == "win32":
    base = 'Win32GUI'

shortcut_table = [
    (
        "DesktopShortcut", # Shortcut
        "DesktopFolder",    # Directory
        "HangMan Game",     # Name
        "TARGETDIR",        # Component
        "[TARGETDIR]\hangman.exe", #Target
        None,   # Arguments
        None,   # Description
        None,   # HotKey
        None,   #Icone
        None,   #IconIndex
        None,   #ShowCMD
        "TARGETDIR", #WKDIR
    )
]

msi_data = {"Shortcut": shortcut_table}

# change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {"data": msi_data}
setup(
    version="1.0",
    description="HangMan Game Developed By Sci-Fic Web",
    author="Sci-Fic Web",
    name=" Hangman Game Player",
    options={'build_exe':{'includer_files': includefile}, "bdist_msi":bdist_msi_options,},
    executables=[
        Executable(
            script="hangman.py",
            base=base,
            icon="hangman.ico",
        )
    ]

)
