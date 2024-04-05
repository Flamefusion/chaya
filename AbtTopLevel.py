import customtkinter
from customtkinter import *
from PIL import Image, ImageTk
from custom_exceptions import *

class AboutToplevelWindow(customtkinter.CTkToplevel,customtkinter.CTkImage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x550")
        self.title("About Us")
        self.iconbitmap("AppImages1/app.ico")
        self.resizable(False, False)

        
         # Add Mf image file
        ig = customtkinter.CTkImage(light_image=Image.open("AppImages1/hdiscuss.png"),
                                  size=(400, 500))
        self.label = customtkinter.CTkLabel(self, text="",image=ig,compound="left")
        self.label.place(x=0, y=0)

        self.Aboutus = customtkinter.CTkLabel(self, text="Who we are ?", font=("Helvetica", 15))
        self.Aboutus.place(x=420, y=50)
        self.AboutusTxtBox = customtkinter.CTkTextbox(self, font=("Helvetica", 15), width=350, height=420,)
        self.AboutusTxtBox.place(x=420, y=80)
        self.AboutusTxtBox.insert("0.0", "We are a team of 3 members.\n\nShekhar Behera\nBranch- CSE\nGithub - https://github.com/Flamefusion\nTechnical Lead\n\nHemant Kumar Sahu\nBranch- CSE\nMail - hemantkumarsahu785@gmail.com\nResource Manager & Feedbaack Lead\n\nSweta Rani Sahu\nBranch- CSE\nMail - swetsahu986@gmail.com\nCreative Design Lead\n\nReference:")  # insert at line 0 character 0
        self.AboutusTxtBox.configure(state="disabled")
       