import customtkinter
from tkinter import messagebox
from customtkinter import *
from PIL import Image, ImageTk
from custom_exceptions import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class FeedbackToplevelWindow(customtkinter.CTkToplevel,customtkinter.CTkImage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x550")
        self.title("FeedBack")
        self.iconbitmap("AppImages/app.ico")
        
        mail_var = StringVar()
        sub_var = StringVar()
        feed_var = StringVar()
         # Add Mf image file
        ig = customtkinter.CTkImage(light_image=Image.open("AppImages/hbutterfly.png"),
                                  size=(400, 500))
        self.label = customtkinter.CTkLabel(self, text="",image=ig,compound="left")
        self.label.place(x=0, y=0)

        self.mail = customtkinter.CTkLabel(self, text="Enter your email:", font=("Helvetica", 15))
        self.mail.place(x=420, y=50)
        self.mailEntry = customtkinter.CTkEntry(self, textvariable=mail_var, font=("Helvetica", 15), width=300,fg_color="gray20")
        self.mailEntry.place(x=420, y=80)

        self.sub = customtkinter.CTkLabel(self, text="Enter your subject:", font=("Helvetica", 15))
        self.sub.place(x=420, y=110)
        self.subEntry = customtkinter.CTkEntry(self, textvariable=sub_var, font=("Helvetica", 15), width=300,fg_color="gray20")
        self.subEntry.place(x=420, y=140)



        self.text = customtkinter.CTkLabel(self, text="Enter your Feedback:", font=("Helvetica", 15))
        self.text.place(x=420, y=170)
        
        self.tk_textbox = customtkinter.CTkTextbox(self,font=("Helvetica", 15), activate_scrollbars=False)
        self.tk_textbox.grid(sticky="nsew")
        self.tk_textbox.place(x=420, y=200)

        # create CTk scrollbar
        self.ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self,height=60,hover=True, command=self.tk_textbox.yview)
        self.ctk_textbox_scrollbar.grid(sticky="ns")
        self.ctk_textbox_scrollbar.place(x=620, y=230)

        # connect textbox scroll event to CTk scrollbar
        self.tk_textbox.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)
        
        self.sendbtn = customtkinter.CTkButton(self, text="Send",command=self.send_email, font=("Helvetica", 15))
        self.sendbtn.place(x=420, y=470)

    def send_email(self):
        # Get the input fields
        sender_email = self.mailEntry.get()
        subject = self.subEntry.get()
        message = self.tk_textbox.get("1.0", "end")

        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = "example@gmail.com"  # Replace with the recipient email address
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            # Send the email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, "password")  # Replace with the password of the sender email address
            text = msg.as_string()
            server.sendmail(sender_email, msg['To'], text)
            server.quit()
            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {str(e)}")