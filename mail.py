import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Application")

        self.sender_email = "kp979183@gmail.com"
        self.sender_password = "kaviya@2005"

        self.create_widgets()

    def create_widgets(self):
        self.to_label = tk.Label(self.root, text="To:")
        self.to_label.pack()
        self.to_entry = tk.Entry(self.root)
        self.to_entry.pack()

        self.subject_label = tk.Label(self.root, text="Subject:")
        self.subject_label.pack()
        self.subject_entry = tk.Entry(self.root)
        self.subject_entry.pack()

        self.message_label = tk.Label(self.root, text="Message:")
        self.message_label.pack()
        self.message_text = tk.Text(self.root, height=10, width=40)
        self.message_text.pack()

        self.send_button = tk.Button(self.root, text="Send", command=self.send_email)
        self.send_button.pack()

    def send_email(self):
        receiver_email = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", "end")

        if not receiver_email or not subject or not message:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = receiver_email
            msg["Subject"] = subject

            msg.attach(MIMEText(message, "plain"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, receiver_email, msg.as_string())

            messagebox.showinfo("Success", "Email sent successfully!")

        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error", "Authentication failed. Check your email and password.")
        except smtplib.SMTPException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailApp(root)
    root.mainloop()
