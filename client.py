import tkinter as tk
from tkinter import ttk
import requests,json

functions = {
    "Search Artists by Name": "/artist/param_to_set/name",
    "Albums by Artist ID": "/artist/param_to_set/albums",
    "Tracks by Artist ID": "/artist/param_to_set",
    "Tracks by Album ID": "/albums/param_to_set/tracks",
    "Tracks by Playlist ID": "/playlist/param_to_set",
    "Tracks by Artist ID": "/artist/param_to_set/tracks",
    "Tracks by Genre ID": "/genre/param_to_set/tracks",
    "Tracks by Customer ID": "/customer/param_to_set/tracks"
}

def make_api_request():
    selected_function = function_combobox.get()
    param = parameter_entry.get()
    
    if selected_function in functions:
        api_endpoint = "http://127.0.0.1:8000" +functions[selected_function].replace("param_to_set",param)
        if selected_function in ["Tracks by Album ID", "Tracks by Playlist ID", "Tracks by Artist ID","Tracks by Genre ID","Tracks by Customer ID"] and shuffle_var.get()==1:
            api_endpoint += "/shuffle"
        
        print(api_endpoint)
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            data = response.json()
            display_data(data)
        else:
            display_data({"Error": f"Request failed with status code: {response.status_code}"})

def display_data(data):
    formatted_data = json.dumps(data, indent=2)

    lines = formatted_data.split('\n')

    clean_lines = [line for line in lines if all(char not in line for char in ['{', '}', ']', '    ['])]

    clean_data = '\n'.join(clean_lines).replace(',',"").replace('[',"").replace('"',"").replace("£","£\n")
    clean_data = bytes(clean_data, "utf-8").decode("unicode_escape")
    result_text.configure(state="normal")
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, clean_data)
    result_text.configure(state="disabled")

def on_function_selection(event):
    selected_function = function_combobox.get()
    if selected_function in ["Tracks by Album ID", "Tracks by Playlist ID", "Tracks by Artist ID","Tracks by Genre ID","Tracks by Customer ID"]:
        shuffle_checkbox.grid(row=1, column=2, columnspan=2)
    else:
        shuffle_checkbox.grid_forget()


root = tk.Tk()
root.title("Music Player")
root.iconbitmap("player_icon.ico")

function_combobox = ttk.Combobox(root, values=list(functions.keys()))
function_combobox.grid(row=0, column=1, sticky="ew")
function_combobox.bind("<<ComboboxSelected>>", on_function_selection)

parameter_entry = tk.Entry(root)
parameter_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

parameter_label = tk.Label(root, text="Parameter:")
parameter_label.grid(row=1, column=0)

shuffle_var = tk.IntVar()

shuffle_checkbox = tk.Checkbutton(root, text="Shuffle", variable=shuffle_var)
shuffle_checkbox.grid(row=1, column=2)
shuffle_checkbox.grid_forget()

request_button = tk.Button(root, text="Send the request", command=make_api_request)
request_button.grid(row=2, column=0, columnspan=2)

result_text = tk.Text(root)
result_text.configure(state="disabled")
result_text.grid(row=3, column=0, columnspan=3, sticky="nsew")

scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.grid(row=3, column=3, sticky='ns')

result_text.config(yscrollcommand=scrollbar.set)

root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
