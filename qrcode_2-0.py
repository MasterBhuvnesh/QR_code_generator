 # import the qrcode library for generating QR codes
import qrcode 
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk, Image
import os

# create a Tkinter window for user input
root = Tk()
root.title("Input Form")
root.geometry("400x300")

# add an icon to GUI
root.iconbitmap("icon.ico")

# add labels and entry boxes for URL and Name input
label_url = Label(root, text="Enter URL:")
label_url.pack(pady=5)
input_url = Entry(root)
input_url.pack(pady=5)
label_name = Label(root, text="Enter Name:")
label_name.pack(pady=5)
input_name = Entry(root)
input_name.pack(pady=5)

# define a function to get user input
def get_input():
    global user_input_url,user_input_name
    user_input_url = input_url.get()
    user_input_name = input_name.get()

# if URL not given it will show message ("ERROR")    
    if not user_input_url:
        messagebox.showerror("Error", "You have not given URL")
        return

# if name not given it will show message ("ERROR")   
    if not user_input_name:
        messagebox.showerror("Error", "You have not given name")
        return
    

    print("User URL:   ", user_input_url  )
    print("User Name:  ", user_input_name  )
    root.destroy()

# add a button to submit user input
submit_button = Button(root, text="Submit", command=get_input)
submit_button.pack(pady=25)

# run the Tkinter event loop to display the input window
root.mainloop()

# if name or url not given it will exit
if not user_input_url or not user_input_name:
    exit()

# create a QR code using the qrcode library
qr = qrcode.QRCode(version=1, box_size=10, border=5)
data = user_input_url  # use the URL input provided by the user
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# save the QR code as a PNG file named "qr_code.png"
img.save("qr_code.png")

# create a new Tkinter window to display the QR code
root_qr = Tk()
root_qr.title(f'{user_input_name}')
root_qr.config(bg="white")

# add an icon to GUI
root_qr.iconbitmap("icon.ico")

# open the saved image and get its width and height
with Image.open("qr_code.png") as img:
    width, height = img.size
    global Width,Height
    Width=(width)
    Height=(height)

# define a function to delete the saved image when the window is closed
def delete_file_on_close():
    os.remove("qr_code.png")
    root_qr.destroy()

# define a function to prompt the user to select a directory to save the file
def location():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    fi=filedialog.askdirectory(title="Where you want to save ?",initialdir=desktop)
    # using if-else so that if user press cancel in save dialog box it doesn't show error
    if fi:
        img.save(f'{fi}/qr_code.png')
        # rename the saved file to match the user input for the file name
        current_file_name = "qr_code.png"
        file_name=user_input_name+".png"
        new_file_name = file_name
        directory_path = (f'{fi}/')
        file_path = os.path.join(directory_path, current_file_name)
        os.rename(file_path, os.path.join(directory_path, new_file_name))
    else :
        print("user doesn't want to save")
      
# display the image in a Label widget
img = Image.open("qr_code.png")
photo = ImageTk.PhotoImage(img)
label = Label(root_qr, image=photo, width=Width, height=Height,background="white")
label.pack()

# add a button to prompt the user to select a directory to save the file
poke=Button(root_qr,text="save",borderwidth=0,font="20",bg="white",command=location,activebackground="white")
poke.pack(pady=10)

# set a function to be called when the window is closed
root_qr.protocol("WM_DELETE_WINDOW", delete_file_on_close)

# run the Tkinter event loop to display QR code
root_qr.mainloop()
