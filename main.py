import tkinter as tk
import pyshorteners

def shorten_url_Generator():
    longurl = entry.get()
    if longurl:
        shortener = pyshorteners.Shortener()
        shorturl = shortener.tinyurl.short(longurl)
        result_label.config(text=f"Short URL: {shorturl}")
    else:
        result_label.config(text="Enter a URL")
# Create the main window
window = tk.Tk()
window.title("Short_URLs_Generator")
window.geometry("600x300")
# Input field for the long URL
entry_label = tk.Label(window, text="Enter the long URL")
entry_label.pack()
entry = tk.Entry(window, width=50)
entry.pack()
# Button to generate the short URL
shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url_Generator)
shorten_button.pack()
# Label to display the short URL
result_label = tk.Label(window, text="")
result_label.pack()
# Run the application
window.mainloop()
