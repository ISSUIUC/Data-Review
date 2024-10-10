################################
# This file creates a GUI interface that allows the user to
# select a CSV file, and plot selected columns within the CSV
# in order to analyze trends in the data for data review
################################
import tkinter as tk
from tkinter import filedialog, messagebox, StringVar, Listbox, MULTIPLE
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# Function to load the CSV and create dropdowns and listbox for columns
def load_csv():
    # Asks the user to select a CSV file
    clear_widgets()
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    
    if file_path:
        try:
            # Read the CSV file
            global data
            data = pd.read_csv(file_path)
            
            # Clear previous widgets if any
            clear_widgets()

            # Create dropdown menu for selecting the time column (X-axis)
            column_names = data.columns.tolist()
            selected_time_column.set(column_names[0])  # Set default time column
            
            # Dropdown for time column selection
            time_dropdown_label = tk.Label(root, text="Select Time Column:")
            time_dropdown_label.pack(pady=5)
            time_dropdown_menu = tk.OptionMenu(root, selected_time_column, *column_names)
            time_dropdown_menu.pack(pady=10)

            # Listbox for selecting multiple data columns (Y-axis)
            data_listbox_label = tk.Label(root, text="Select Data Columns (Y-axis):")
            data_listbox_label.pack(pady=5)
            data_listbox.pack(pady=10)
            global displayIndivid
            displayIndivid = tk.IntVar()
            c1 = tk.Checkbutton(root, text='Display Data Invidvidally?',variable=displayIndivid, onvalue=1, offvalue=0)
            c1.pack(pady =20)
            
            # Populate the listbox with column names
            data_listbox.delete(0,tk.END)
            for column in column_names:
                data_listbox.insert(tk.END, column)

            # Add a button to plot the selected columns
            plot_button = tk.Button(root, text="Plot Selected Columns", command=plot_selected_columns)
            plot_button.pack(pady=20)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file\n{e}")

# Function to clear previous widgets
def clear_widgets():
    for widget in root.winfo_children():
        if widget not in (load_button,):
            widget.pack_forget()

# Function to plot the selected columns using Plotly
def plot_selected_columns():
    time_col = selected_time_column.get()
    selected_data_cols = [data_listbox.get(i) for i in data_listbox.curselection()]
    
    if time_col in data.columns and all(col in data.columns for col in selected_data_cols):
        # Create a plotly figure
        if displayIndivid.get() == 0:
            #Displays all graphs together
            fig = go.Figure()

            # Add each selected data column as a trace to the plot
            for col in selected_data_cols:
                fig.add_trace(go.Scatter(x=data[time_col], y=data[col], mode='lines+markers', name=col))

            # Update layout with titles and axis labels
            fig.update_layout(
                title=f"Selected Columns vs Time",
                xaxis_title="Time (ms)",
                yaxis_title="Values",
                showlegend=True
            )
            fig.show()
        elif displayIndivid.get() == 1:
            #Displays graphs separately
            subtitles = [f"{col} vs Time (ms)" for col in selected_data_cols]
            fig = make_subplots(rows=len(selected_data_cols), cols=1, 
                                subplot_titles=subtitles)
            rowCounter = 1
            #Prints subplots and adds titles, xlabels, and ylabels to them
            for col in selected_data_cols:
                fig.add_trace(go.Scatter(x=data[time_col],y = data[col], name = selected_data_cols[rowCounter - 1]),row = rowCounter,col = 1 )
                fig.update_yaxes(title_text= selected_data_cols[rowCounter - 1] , row = rowCounter, col=1)
                fig.update_xaxes(title_text= "Time (ms)" , row = rowCounter, col=1)
                rowCounter += 1
            fig.update_layout(height = rowCounter * 300, width = 800, title_text=f"Selected Columns vs Time", showlegend=True)

            # Show the plot in the default browser
            fig.show()
    else:
        messagebox.showerror("Error", "Invalid column selection.")

# Initialize the main window
root = tk.Tk()
root.title("CSV Viewer with Interactive Plotting")
root.geometry("600x500")

# Initialize variables
selected_time_column = StringVar(root)
data_listbox = Listbox(root, selectmode=MULTIPLE, height=10, width=50)

# Create a button to load CSV file
load_button = tk.Button(root, text="Load CSV File", command=load_csv)
load_button.pack(pady=10)

# Run the application
root.mainloop()
