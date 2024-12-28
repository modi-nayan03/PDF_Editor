import tkinter
import customtkinter
from pytube import YouTube
import yt_dlp

# def download():
#     try:
#         ytlink = url_var.get()  # Get the YouTube link from the input field
#         ydl_opts = {
#             "format": "bestvideo+bestaudio/best",  # High-quality video and audio
#             "outtmpl": "%(title)s.%(ext)s",        # Save the file with the video title
#         }
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([ytlink])
#         status_label.configure(text="Download Complete!", text_color="green")
#     except Exception as e:
#         status_label.configure(text="Invalid YouTube Link or Download Failed", text_color="red")
#         print(f"Error: {e}")

# # # Logic for downloading YouTube videos
# def download():
#     try:
#         ytlink = url_var.get()
#         ydl_opts = {"format": "best", "outtmpl": "%(title)s.%(ext)s"}
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([ytlink])
#         status_label.configure(text="Download Complete!", text_color="green")
#     except Exception as e:
#         status_label.configure(text="Invalid YouTube Link", text_color="red")
#         print(f"Error: {e}")
def download():
    try:
        ytlink = url_var.get()  # Get the YouTube link from the input field
        ytobject = YouTube(ytlink)
        video = ytobject.streams.get_highest_resolution()  # Get the highest resolution stream
        video.download()
        status_label.configure(text="Download Complete!", text_color="green")
    except Exception as e:
        status_label.configure(text="Invalid YouTube Link", text_color="red")
        print(f"Error: {e}")


# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Add UI to the application
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link", font=("Arial", 20))
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=50, textvariable=url_var, placeholder_text="Enter YouTube link here")
link.pack(pady=10)

# Download button
download_button = customtkinter.CTkButton(app, text="Download", command=download)
download_button.pack(pady=20)

# Status label
status_label = customtkinter.CTkLabel(app, text="")
status_label.pack(pady=10)

# Run the application
app.mainloop()
