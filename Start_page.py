
import tkinter
from tkinter import filedialog,messagebox
from functools import partial
from os import path,remove,mkdir,scandir
from shutil import copy
from utility import types
from pathlib import Path


class Start_page:
    def __init__(self,parent,window):
        self.parent=parent
        self.canvas=tkinter.Canvas(window,height=50)
        self.canvas.pack()
        
        self.app_name= tkinter.Label(window,text='File Organizer 🤖',font=('Raleway',20),fg='#FC4F4F',underline=5)
        self.app_name.pack()

        self.instruction_text=tkinter.Label(window,text='Select the folder you want to organize',font=('Raleway',12),fg='#21325E', pady=15)
        self.instruction_text.pack()

        self.canvas=tkinter.Canvas(height=20)
        self.canvas.pack()

        self.select_btn=tkinter.Button(window,text='Select',command=partial(self.handle_click,window),width=10,height=2,font=('Raleway',10),fg='#fff',relief='flat',bg="#4D77FF",activebackground='#bbb',activeforeground='#fff')
        self.select_btn.pack()

        self.canvas=tkinter.Canvas(height=20)
        self.canvas.pack()

    def handle_click(self,window):
        path =  filedialog.askdirectory(title="Select Folder")
        if not path:
            self.instruction_text.config(text=f'No path selected')
        elif path:
            self.instruction_text.config(text=f'Selected folder: {path}')
            start_btn=tkinter.Button(window,text='Organize',command=partial(self.organize,window,path),relief='flat',width=10,height=2,font=('Raleway',10),bg='#219F94', fg='#fff')
            start_btn.pack()
            canvas=tkinter.Canvas(height=20)
            canvas.pack()

## METHODS TO MAKE SUB-FOLDERS AND ORGANIZE MAIN FOLDER

    def make_dir(self,window,folder_path,main_path):
        msg_box=tkinter.Text(window,padx=15,pady=15)
        msg_box.pack()
        for type in types:
            new_folder_path=path.join(folder_path,type)
            if not path.exists(new_folder_path):
                mkdir(new_folder_path)
            for file in scandir(main_path):
                if path.isfile(file):
                    for ext in types[type]:
                        if ext==Path(file).suffix:
                            msg=f'Copying {path.join(main_path,path.basename(file))} to --> {path.join(new_folder_path,path.basename(file))}\n\n'
                            msg_box.insert(1.0,msg)
                            copy(file,new_folder_path)
                            remove(file)
                            msg_box.update()
                    
        messagebox.showinfo('Organize successful',f'Organizing successful.\n Found new folder {folder_path}')                    
        return

    def Organizer(self,window,main_path):
        if(path.exists(main_path)):
            organized_folder_path=path.join(main_path,"Organized_folder")
            if not path.exists(organized_folder_path):
                mkdir(organized_folder_path)    
            self.make_dir(window,organized_folder_path,main_path)
            return

## ORGANIZE BUTTON COMMAND FUNCTION
    def organize(self,window,path):
        self.Organizer(window,path)
        return
