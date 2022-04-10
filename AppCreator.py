import sys, os
from colorama import Fore

def banner():
    print(f"""{Fore.RESET}
                               {Fore.RED}Dev By Tahg{Fore.RESET}
░█████╗░██████╗░██████╗░░░░░░░░█████╗░██████╗░███████╗░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
███████║██████╔╝██████╔╝█████╗██║░░╚═╝██████╔╝█████╗░░███████║░░░██║░░░██║░░██║██████╔╝
██╔══██║██╔═══╝░██╔═══╝░╚════╝██║░░██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
██║░░██║██║░░░░░██║░░░░░░░░░░░╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
            {Fore.RED}GitHub: {Fore.BLUE}https://github.com/T4hg/ {Fore.RESET}
    """)

def creator():
    prefix = f"{Fore.RED}APP {Fore.BLUE}Creator {Fore.GREEN}· {Fore.WHITE}"
    system_prefix = f"{Fore.RED}$ {Fore.GREEN}"
    file_name = input(prefix + "File Name (EXAMPLE: tool): ")
    file = open(f"{file_name}.pyw",'w+')
    file.write(f'''# This app is created by App Creator - GitHub: https://github.com/T4hg/
import sys
import datetime
from tkinter import CENTER
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from requests import get
    ''')
    print(system_prefix + "Imports Created...\n")
    opt1 = input(prefix + "Web Url (EXAMPLE: https://www.example.es/): ")
    if opt1 == "":
        print(system_prefix + f"{Fore.RED}ERROR {Fore.GREEN}You need to put a web page\n")
        sys.exit()
    print(system_prefix + "Web OK...\n")
    opt2 = input(prefix + "Icon Url (EXAMPLE: https://www.example.es/example.png/): ")
    if opt2 == "":
        print(system_prefix + f"{Fore.RED}ERROR {Fore.GREEN}You need to put a icon url\n")
        sys.exit()
    file.write(f'''# 
app = QtWidgets.QApplication(sys.argv)
windows = QtWidgets.QWidget()
    ''')
    print(system_prefix + "Icon Created...\n")
    opt3 = input(prefix + "Window Name (EXAMPLE: AppCreator): ")
    if opt3 == "":
        print(system_prefix + f"{Fore.RED}ERROR {Fore.GREEN}You need to put a name\n")
        sys.exit()
    print(system_prefix + "Placing All...\n")
    file.write('''#
x = datetime.datetime.now()
name = f"ICON-{x.year}-{x.minute}.png"
icon = open(name,'wb')
    ''')
    file.write(f'''
icon_res = get("{opt2}")
icon.write(icon_res.content)
icon.close()
windows.setWindowIcon(QtGui.QIcon(name))
windows.setWindowTitle("{opt3} | By AppCreator - GitHub: https://github.com/T4hg/")
windows.resize(500,500)
windows.move(100,100)
html = get("{opt1}").text
web_view = QWebEngineView()
web_view.setHtml(html)
web = QVBoxLayout()
web.addWidget(web_view)
windows.setLayout(web)
windows.show()
sys.exit(app.exec_())
    ''')
    print(f"""{Fore.GREEN}App created perfectly
{Fore.WHITE}Remember to {Fore.YELLOW}star {Fore.WHITE}me on my GitHub ({Fore.BLUE}https://github.com/T4hg/{Fore.WHITE})

{Fore.RED}NOTE: You will have to install all the dependencies to run the program, it will be better not to touch the source code of the program to avoid errors.
""")
    input(system_prefix + "ENTER TO EXIT...")
    file.close()
if __name__ == '__main__':
    os.system("cls")
    banner()
    creator()