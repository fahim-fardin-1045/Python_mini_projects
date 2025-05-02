import speedtest
from tkinter.ttk import *
from tkinter import *
import threading
import os

# Create main window
root = Tk()
root.title("Internet Speed Test by Fahim")
root.geometry('600x420')  # Bigger window
root.resizable(False, False)
root.configure(bg="#1e1e2f")  # Dark background


# Safely set window icon
icon_path = 'speed.ico'
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# Title Labels
Label(root, text='🚀 INTERNET SPEED TEST', bg='#1e1e2f', fg='#00eaff', font='Arial 22 bold').pack(pady=20)

# Result Labels
down_label = Label(root, text="⏬ Download Speed - ", bg='#1e1e2f', fg='#ffffff', font='Arial 14 bold')
down_label.place(x=100, y=100)
up_label = Label(root, text="⏫ Upload Speed - ", bg='#1e1e2f', fg='#ffffff', font='Arial 14 bold')
up_label.place(x=100, y=150)
ping_label = Label(root, text="📶 Ping - ", bg='#1e1e2f', fg='#ffffff', font='Arial 14 bold')
ping_label.place(x=100, y=200)
server_label = Label(root, text="🌐 Server Location - ", bg='#1e1e2f', fg='#ffffff', font='Arial 14 bold')
server_label.place(x=100, y=250)
Label(root, text='by Fahim', bg='#1e1e2f', fg='#cfcfcf', font='Arial 14 italic').pack(side=BOTTOM, pady=10)

# Initialize result variables
download_speed = 0
upload_speed = 0
ping_speed = 0
server_name = "Unknown"
server_country = "Unknown"

# Function to check speed
def check_speed():
    global download_speed, upload_speed, ping_speed, server_name, server_country
    try:
        speed_test = speedtest.Speedtest()
        speed_test.get_best_server()

        download = speed_test.download()
        upload = speed_test.upload()
        ping = speed_test.results.ping

        server_info = speed_test.results.server
        server_name = server_info.get('sponsor', "Unknown")
        server_country = server_info.get('country', "Unknown")

        download_speed = round(download / (10 ** 6), 2)
        upload_speed = round(upload / (10 ** 6), 2)
        ping_speed = round(ping, 2)
    except Exception as e:
        download_speed = upload_speed = ping_speed = 0
        server_name = "Failed"
        server_country = "Check Network"
        print("Error during speed test:", e)

def update_text():
    thread = threading.Thread(target=check_speed)
    thread.start()
    progress = Progressbar(root, orient=HORIZONTAL, length=300, mode='indeterminate')
    progress.place(x=100, y=300)
    progress.start()
    while thread.is_alive():
        root.update()
        pass
    down_label.config(text="⏬ Download Speed - " + str(download_speed) + " Mbps")
    up_label.config(text="⏫ Upload Speed - " + str(upload_speed) + " Mbps")
    ping_label.config(text="📶 Ping - " + str(ping_speed) + " ms")
    server_label.config(text="🌐 Server Location - " + server_name + ", " + server_country)
    progress.stop()
    progress.destroy()

# Button to start test
button = Button(root, text="▶ Check My Speed", width=30, bd=0, bg='#00eaff', fg='#1e1e2f', pady=10, font='Arial 14 bold', command=update_text)
button.place(x=100, y=340)

root.mainloop()
