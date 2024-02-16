import urllib.request
import tkinter as tk

# Function to test website connectivity
def test_connectivity():
    # Create the main Tkinter window
    window = tk.Tk()
    window.geometry('600x400')  # Set window size
    head = tk.Label(window, text='Website Connectivity Checker', font=('Calibri 15'))
    head.pack(pady=20)

    # Function to check URL connectivity
    def check_url():
        web = (url.get())
        # Use urllib to open the URL and get the status code
        status_code = urllib.request.urlopen(web).getcode()
        # Check if the status code is 200 (OK)
        website_is_up = status_code == 200

        # Display the result in the Tkinter window
        if website_is_up:
            tk.Label(window, text='Website Available', font=('Calibri 15')).place(x=260, y=200)
        else:
            tk.Label(window, text='Website Not Available', font=('Calibri 15')).place(x=260, y=200)

    # Variable to store the entered URL
    url = tk.StringVar()
    # Entry widget to input the website URL
    tk.Entry(window, textvariable=url).place(x=200, y=80, height=30, width=280)
    # Button to trigger the URL check
    tk.Button(window, text='Check', command=check_url).place(x=285, y=150)
    
    # Run the Tkinter main loop
    window.mainloop()

# Check if the script is being run directly
if __name__ == '__main__':
    # Call the function to test website connectivity
    test_connectivity()
