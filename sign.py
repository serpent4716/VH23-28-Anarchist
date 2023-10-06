from tkinter import *
from PIL import ImageTk , Image

class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)




        self.bg_frame = Image.open('.idea\\prupleblue1.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill= 'both', expand='yes')

        self.lgn_frame = Frame(self.window, bg='black', width='950', height=600)
        self.lgn_frame.place(x=200, y=70)

        self.txt = 'Welcome'
        self.heading = Label(self.lgn_frame, text=self.txt, font= ('yu gothic ui', 25, 'bold'), bg= 'black', fg='white')
        self.heading.place(x=80, y= 30, width= 300, height = 30)

        self.side_image = Image.open('.idea\\programerleft.jpg')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo,bg='black')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        self.sign_in_image = Image.open('.idea\\heyy1.jpg')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo,bg='black')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)


def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()


if __name__ == '__main__':
    page()
