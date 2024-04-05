import customtkinter
from tkinter import messagebox 
from PIL import Image, ImageTk



class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get the screen width and height
        width = self.winfo_screenwidth()  # 1536
        height = self.winfo_screenheight()  # 864
        self.geometry("%dx%d" % (width, height))
        self.title("Mirage")
        # self.iconbitmap("AppImages/app.ico")

        # Set the window background image
        bg = customtkinter.CTkImage(light_image=Image.open("AppImages/hacker.jpg"),
                                    size=(1536, 864))
        self.label1 = customtkinter.CTkLabel(self, text="", image=bg)
        self.label1.place(x=0, y=0)

    
        # Add info button
        infg = customtkinter.CTkImage(light_image=Image.open("AppImages/icons8-light-oncool-48.png"),
                                      size=(50, 35))
        self.infgbtn = customtkinter.CTkButton(self, text="",
                                               compound="left", image=infg,
                                               width=10, height=20, corner_radius=0,command=self.info
                                               )
        self.infgbtn.place(x=10, y=10)

        # Add ImgBtn image file
        Img_Btn_img = customtkinter.CTkImage(light_image=Image.open("AppImages/icons8-image-gallery-48.png"),
                                             size=(70, 50))
        self.button_1 = customtkinter.CTkButton(self, text="Image", text_color='black', font=('Helvetica', 15),
                                                fg_color="#EDE4E2", compound="right", image=Img_Btn_img,
                                                width=180, height=50, border_width=5, corner_radius=0,
                                                )
        self.button_1.place(x=1250, y=150)

        # Add AudBtn image file
        Aud_Btn_img = customtkinter.CTkImage(light_image=Image.open("AppImages/icons8-audio-48.png"),
                                             size=(70, 50))
        self.button_2 = customtkinter.CTkButton(self, text="Audio", text_color='black', font=('Helvetica', 15),
                                                fg_color="#EDE4E2", compound="right", image=Aud_Btn_img,
                                                width=180, height=50, border_width=5, corner_radius=0,
                                                )
        self.button_2.place(x=1250, y=250)

        # Add vidBtn image file
        Vid_Btn_img = customtkinter.CTkImage(light_image=Image.open("AppImages/icons-video.png"),
                                             size=(70, 50))
        self.button_3 = customtkinter.CTkButton(self, text="Video", text_color='black', font=('Helvetica', 15),
                                                fg_color="#EDE4E2", compound="right", image=Vid_Btn_img,
                                                width=180, height=50, border_width=5, corner_radius=0,
                                                )
        self.button_3.place(x=1250, y=350)

        # Add FeedBtn image file
        Feed_Btn_img = customtkinter.CTkImage(light_image=Image.open("AppImages/feedback.png"),
                                              size=(70, 50))
        self.button_4 = customtkinter.CTkButton(self, text="Feedback", text_color='black', font=('Helvetica', 15),
                                                fg_color="#EDE4E2", compound="right", image=Feed_Btn_img,
                                                width=180, height=50, border_width=5, corner_radius=0,
                                                )
        self.button_4.place(x=1250, y=450)

        # Add faqBtn image file
        Faq_Btn_img = customtkinter.CTkImage(light_image=Image.open("AppImages/about.png"),
                                             size=(70, 50))
        self.button_5 = customtkinter.CTkButton(self, text="About", text_color='black', font=('Helvetica', 15),
                                                fg_color="#EDE4E2", compound="right", image=Faq_Btn_img,
                                                width=180, height=50, border_width=5, corner_radius=0,
                                                )
        self.button_5.place(x=1250, y=550)


    def info(self):
        lines = ['Image Button - For Image Steganography', 'Audio Button - For Audio Steganography', 'Video Button - For '
                                                                                                 'Video Steganography']
        messagebox.showinfo('How To Use Mirage', "\n".join(lines))



app = App()
app.mainloop()
