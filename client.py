import tkinter as tk
from tkinter import ttk
import requests
import json

# Dictionary of API functions
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

# Function to make API requests
def make_api_request():
    """
    Make a request to the API based on the selected function and parameter.
    
    Parameters:
    None
    
    Returns:
    None
    """
    # Get the selected function and parameter
    selected_function = function_combobox.get()
    param = parameter_entry.get()

    # Construct the API endpoint based on the selected function and parameter
    if selected_function in functions:
        api_endpoint = "http://127.0.0.1:8000" + functions[selected_function].replace("param_to_set", param)
        if selected_function in ["Tracks by Album ID", "Tracks by Playlist ID", "Tracks by Artist ID", "Tracks by Genre ID", "Tracks by Customer ID"] and shuffle_var.get() == 1:
            api_endpoint += "/shuffle"

        # Make a GET request to the API endpoint
        response = requests.get(api_endpoint)

        # If the request is successful, display the data, otherwise display an error message
        if response.status_code == 200:
            data = response.json()
            display_data(data)
        else:
            display_data({"Error": f"Request failed with status code: {response.status_code}"})

# Function to display API response data
def display_data(data):
    """
    Format and display the API response data.
    
    Parameters:
    data (dict): The data retrieved from the API.
    
    Returns:
    None
    """
    # Format the data to display it in the text field
    formatted_data = json.dumps(data, indent=2)
    lines = formatted_data.split('\n')
    clean_lines = [line for line in lines if all(char not in line for char in ['{', '}', ']', '    ['])]
    clean_data = '\n'.join(clean_lines).replace(',', "").replace('[', "").replace('"', "").replace("£", "£\n")
    clean_data = bytes(clean_data, "utf-8").decode("unicode_escape")

    # Update the text field with the formatted data
    result_text.configure(state="normal")
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, clean_data)
    result_text.configure(state="disabled")

# Function triggered when a function is selected
def on_function_selection(event):
    """
    Show or hide the shuffle checkbox based on the selected function.
    
    Parameters:
    event (Event): The event triggered by function selection.
    
    Returns:
    None
    """
    # Show the shuffle checkbox if the selected function requires it, otherwise hide it
    selected_function = function_combobox.get()
    if selected_function in ["Tracks by Album ID", "Tracks by Playlist ID", "Tracks by Artist ID", "Tracks by Genre ID", "Tracks by Customer ID"]:
        shuffle_checkbox.grid(row=1, column=2, columnspan=2)
    else:
        shuffle_checkbox.grid_forget()

# Create the main window
root = tk.Tk()
root.title("Music Player")
root.iconbitmap("player_icon.ico")

# Create the function selection combobox
function_combobox = ttk.Combobox(root, values=list(functions.keys()))
function_combobox.grid(row=0, column=1, sticky="ew")
function_combobox.bind("<<ComboboxSelected>>", on_function_selection)

# Create the parameter entry field
parameter_entry = tk.Entry(root)
parameter_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

# Create the parameter label
parameter_label = tk.Label(root, text="Parameter:")
parameter_label.grid(row=1, column=0)

# Create the shuffle variable
shuffle_var = tk.IntVar()

# Create the shuffle checkbox
shuffle_checkbox = tk.Checkbutton(root, text="Shuffle", variable=shuffle_var)
shuffle_checkbox.grid(row=1, column=2)
shuffle_checkbox.grid_forget()

# Create the request button
request_button = tk.Button(root, text="Send the request", command=make_api_request)
request_button.grid(row=2, column=0, columnspan=2)

# Create the result text field
result_text = tk.Text(root)
result_text.configure(state="disabled")
result_text.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Create the scrollbar for the result text field
scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.grid(row=3, column=3, sticky='ns')

result_text.config(yscrollcommand=scrollbar.set)

root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

# Run the main event loop
root.mainloop()
