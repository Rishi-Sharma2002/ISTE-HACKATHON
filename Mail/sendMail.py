from tkinter import *
from Crypto.Cipher import AES
import base64
import os
import smtplib

global email_id

def encryption(info):
    BLOCK_SIZE = 16
    PADDING = '&'
    pad = lambda s : s+ (BLOCK_SIZE-len(s) % BLOCK_SIZE)*PADDING
    EncodeAES = lambda c, s:base64.b64encode(c.encrypt(pad(s)))
    secret = enterKey.get()
    secret = secret.ljust(16,'&')
    print('Encryption key:\n' , secret)
    P = Label(root, text = f'Your Secret key to decrypt the message:{secret}')
    P.place(x=180, y = 550)    
    cipher = AES.new(secret)
    encoded = EncodeAES(cipher, info)
    return encoded

def decrypt(encryptedString):
    PADDING = '&'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))
    key = 'Rishi2002'.ljust(16,'&')
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, encryptedString)
    a = str(decoded).replace('b\'', '')
    print('Decrypted DATA: ',a.replace('&', ''))

def send_mail():
    info = body.get("1.0", "end")

    sender = email_id.get()
    receivers = to_id.get()
    password_sec = pass_id.get()

    message = encryption(info)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, password_sec)
    s.sendmail(sender, receivers, message)
    print('Message SEND !')
    s.quit()


if __name__ == '__main__':
    root = Tk()
    root.geometry('750x750')

    heading = Label(root, text = 'SECURE MAIL SENDER !', font = ('Sans Serif', 20, 'bold'))
    heading.place(x=230, y=10)

    email_id = StringVar()
    enter_email = Label(root, text = 'Email: ', font = ('Sans Serif', 15, 'bold'))
    enter_email.place(x=8, y=80)

    email = Entry(root, textvariable = email_id, width=25)
    email.place(x=70, y=80)

    pass_id = StringVar()
    password = Label(root, text = 'Password: ',font = ('Sans Serif', 15, 'bold'))
    password.place(x=320, y=80)

    pass_place = Entry(root, textvariable = pass_id, width=25, show = '*')
    pass_place.place(x=450, y=80)

    global to_id
    to_id = StringVar()
    to = Label(root, text='To: ',font = ('Sans Serif', 15, 'bold'))
    to.place(x=200, y=150)
    to_content = Entry(root, textvariable=to_id, width = 25)
    to_content.place(x=250, y=150)

    body = Text(root, width = 100, height = 20)
    body.place(x=10, y= 250)

    Content = Label(root, text = 'Message: ',width = 60)
    Content.place(x=100, y= 220)     

    send = Button(root, text='Send Mail', command = send_mail)
    send.place(x=320, y = 700)

    global enterKey 
    enterKey = StringVar()
    EnterKey = Entry(root, width=20, textvariable = enterKey)
    EnterKey.place(x=350, y = 600)

    enter_Key = Label(root, text = 'Enter a Passphrase to encrypt with(Not more than 16): ',font = ('Sans Serif', 8, 'bold'))
    enter_Key.place(x=10, y = 605)

    root.resizable(False, False)
    root.mainloop()
