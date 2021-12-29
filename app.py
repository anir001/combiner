import tkinter as tk
import tkinter.font as tkFont
import tkinter.filedialog
import combine

VER = '0.1'


class App:
    def __init__(self, root):
        # setting title
        root.title(f"Combiner {VER}")
        # setting window size
        width=400
        height=150
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        # --------------- #
        self.directory = None

        # --------------- #
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Otwórz folder", command=self.open_directory)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        infomenu = tk.Menu(menubar, tearoff=0)
        infomenu.add_command(label="License", command=self.license_window)
        infomenu.add_command(label="About...", command=self.about_window)
        menubar.add_cascade(label="Info", menu=infomenu)

        root.config(menu=menubar)

        generate = tk.Button(root)
        generate["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        generate["font"] = ft
        generate["fg"] = "#000000"
        generate["justify"] = "center"
        generate["text"] = "Generuj"
        generate.place(x=20, y=20, width=70, height=25)
        generate["command"] = self.generate

    def generate(self):
        if self.directory is not None:
            combiner = combine.Combine()
            combiner.run(self.directory)
            tk.messagebox.showinfo("Ready", "Gotowe, sprawdź folder output")
        else:
            tk.messagebox.showerror("Error", "Wybierz folder")

    def open_directory(self):
        self.directory = tk.filedialog.askdirectory()

    def license_window(self):
        window = tk.Toplevel(root)
        window.title("License")
        l = tk.LabelFrame(window, text="Copyright 2022 ds", padx=20, pady=20)
        l.pack(fill="both", expand="yes")
        window.resizable(width=False, height=False)
        tk.Label(l, text=
                    "Combiner jest wolnym oprogramowaniem: możesz go rozprowadzać dalej\n"
                    "i/lub modyfikować na warunkach Powszechnej Licencji Publicznej GNU,\n"
                    "wydanej przez Fundację Wolnego Oprogramowania - według wersji 3 tej\n"
                    "Licencji lub (według twojego wyboru) którejś z późniejszych wersji.\n\n"
                    
                    "Combiner rozpowszechniany jest z nadzieją, iż będzie on\n"
                    "użyteczny - jednak BEZ JAKIEJKOLWIEK GWARANCJI, nawet domyślnej\n"
                    "gwarancji PRZYDATNOŚCI HANDLOWEJ albo PRZYDATNOŚCI DO OKREŚLONYCH\n"
                    "ZASTOSOWAŃ. W celu uzyskania bliższych informacji sięgnij do\n"
                    "Powszechnej Licencji Publicznej GNU.\n\n"
                    
                    "Z pewnością wraz z Combiner otrzymałeś też egzemplarz\n"
                    "Powszechnej Licencji Publicznej GNU (GNU General Public License).\n"
                    "Jeśli nie - zobacz <http://www.gnu.org/licenses/>.\n").pack()

    def about_window(self):
        window = tk.Toplevel(root)
        window.title("About")
        l = tk.LabelFrame(window, padx=20, pady=20)
        l.pack(fill="both", expand="yes")
        window.resizable(width=False, height=False)
        tk.Label(l, text=f"Combiner {VER}").pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
