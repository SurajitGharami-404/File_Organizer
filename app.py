import tkinter 
import Start_page


class App:
    def __init__(self,root,title,geometry) -> None:
        self.root=root
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.pageshow=Start_page.Start_page(self,self.root)


def main():
    root=tkinter.Tk()
    App(root,'File Organizer','600x500')
    root.mainloop()
if __name__=='__main__':
    main()