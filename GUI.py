import customtkinter
from tkinter import messagebox 
from PIL import Image, ImageTk
import ImageTopLevel
import AudioTopLevel
import VideoTopLevel
import FeedTopLevel
import AbtTopLevel


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get the screen width and height
        width = self.winfo_screenwidth()  # 1536
        height = self.winfo_screenheight()  # 864
        self.geometry("%dx%d" % (width, height))
        self.title("Mirage")
        # self.iconbitmap("AppImages1/app.ico")

        # Set the window background image
        bg = customtkinter.CTkImage(light_image=Image.open("AppImages1/hacker.jpg"),
                                    size=(1536, 864))
        self.label1 = customtkinter.CTkLabel(self, text="", image=bg)
        self.label1.place(x=0, y=0)

    
        # Add info button
        infg = customtkinter.CTkImage(light_image=Image.open("AppImages1/icons8-light-oncool-48.png"),
                                      size=(50, 35))
        self.infgbtn = customtkinter.CTkButton(self, text="",
                                               compound="left", image=infg,
                                               width=10, height=20, corner_radius=0,command=self.info
                                               )
        self.infgbtn.place(x=10, y=10)

        # Add ImgBtn image file
        Img_Btn_img = customtkinter.CTkImage(light_image=Image.open("AppImages1/icons8-image-gallery-48.png"),
                                             size=(70, 50))
        self.button_1 = customtkinter.CTkButton(self, text="Image", text_color='black', font=('Helvetica', 15),
                                                fg_color="#EDE4E2", compound="right", image=Img_Btn_img,
                                                width=180, height=50, border_width=5, corner_radius=0,
                                                command=self.open_toplevel)
        self.button_1.place(x=1250, y=150)

        # Add AudBtn image file
        Aud_Btn_img = customtkinter.CTkImage(light_image=Image.open("AppImages1/icons8-audio-48.png"),
                                             size=(70, 50))
        self.button_2 = customtkinter.CTkButton(self, text="Audio", text_color='black', font=('Helvetica', 15),
                                                fg_color="#EDE4E2", compound="right", image=Aud_Btn_img,
                                                width=180, height=50, border_width=5, corner_radius=0,
                                                command=self.open_toplevel2)
        self.button_2.place(x=1250, y=250)

        # Add vidBtn image file
        Vid_Btn_img = customtkinter.CTkImage(light_image=Image.open("AppImages1/icons-video.png"),
                                             size=(70, 50))
        self.button_3 = customtkinter.CTkButton(self, text="Video", text_color='black', font=('Helvetica', 15),
                                                fg_color="#EDE4E2", compound="right", image=Vid_Btn_img,
                                                width=180, height=50, border_width=5, corner_radius=0,
                                                command=self.open_toplevel3)
        self.button_3.place(x=1250, y=350)

        # Add FeedBtn image file
        Feed_Btn_img = customtkinter.CTkImage(light_image=Image.open("AppImages1/feedback.png"),
                                              size=(70, 50))
        self.button_4 = customtkinter.CTkButton(self, text="Feedback", text_color='black', font=('Helvetica', 15),
                                                fg_color="#EDE4E2", compound="right", image=Feed_Btn_img,
                                                width=180, height=50, border_width=5, corner_radius=0,
                                                command=self.open_toplevel4)
        self.button_4.place(x=1250, y=450)

        # Add faqBtn image file
        Faq_Btn_img = customtkinter.CTkImage(light_image=Image.open("AppImages1/about.png"),
                                             size=(70, 50))
        self.button_5 = customtkinter.CTkButton(self, text="About", text_color='black', font=('Helvetica', 15),
                                                fg_color="#EDE4E2", compound="right", image=Faq_Btn_img,
                                                width=180, height=50, border_width=5, corner_radius=0,
                                                command=self.open_toplevel5)
        self.button_5.place(x=1250, y=550)

        self.toplevel_window = None
        self.toplevel2_window = None
        self.toplevel3_window = None
        self.toplevel4_window = None
        self.toplevel5_window = None

    def info(self):
        lines = ['Image Button - For Image Steganography', 'Audio Button - For Audio Steganography', 'Video Button - For '
                                                                                                 'Video Steganography']
        messagebox.showinfo('How To Use Mirage', "\n".join(lines))

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ImageTopLevel.ImageToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def open_toplevel2(self):
        if self.toplevel2_window is None or not self.toplevel2_window.winfo_exists():
            self.toplevel2_window = AudioTopLevel.AudioToplevelWindow(self)  # create window if its None or destroyed  
        else:
            self.toplevel2_window.focus()  # if window exists focus it

    def open_toplevel3(self):
        if self.toplevel3_window is None or not self.toplevel3_window.winfo_exists():
            self.toplevel3_window = VideoTopLevel.VideoToplevelWindow(self)  # create window if its None or destroyed   
        else:
            self.toplevel3_window.focus()  # if window exists focus it 

    def open_toplevel4(self):
        if self.toplevel4_window is None or not self.toplevel4_window.winfo_exists():
            self.toplevel4_window = FeedTopLevel.FeedbackToplevelWindow(
                self)  # create window if its None or destroyed
        else:
            self.toplevel4_window.focus()

    def open_toplevel5(self):
        if self.toplevel5_window is None or not self.toplevel5_window.winfo_exists():
            self.toplevel5_window = AbtTopLevel.AboutToplevelWindow(self)  # create window if its None or destroyed   
        else:
            self.toplevel5_window.focus()


app = App()
app.mainloop()
