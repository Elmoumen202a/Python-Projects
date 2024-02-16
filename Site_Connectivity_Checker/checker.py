import urllib.request
import tkinter as tk

def check_url(url, result_label):
    try:
        # Attempt to open the URL and get the status code
        status_code = urllib.request.urlopen(url).getcode()
        website_is_up = status_code == 200

        # Check if result_label is provided and update it accordingly
        if result_label is not None:
            if website_is_up:
                result_label.config(text='Website Available', fg='green')
            else:
                result_label.config(text='Website Not Available', fg='red')

        # Return a tuple with the result and no error
        return website_is_up, None  

    except Exception as e:
        # Handle exceptions and update result_label if provided
        if result_label is not None:
            result_label.config(text=f'Error: {e}', fg='red')
        return False, str(e)

def test_connectivity():
    window = tk.Tk()
    window.geometry('600x400')
    head = tk.Label(window, text='Website Connectivity Checker', font=('Calibri 15'))
    head.pack(pady=20)

    # Variable to store the entered URL
    url = tk.StringVar()
    # Entry widget to input the website URL
    entry = tk.Entry(window, textvariable=url)
    entry.place(x=200, y=80, height=30, width=280)

    # Label to display the result
    result_label = tk.Label(window, text='', font=('Calibri 15'))
    result_label.place(x=220, y=200)

    # Button to trigger the URL check
    tk.Button(window, text='Check', command=lambda: check_url(url.get(), result_label)).place(x=285, y=150)
    
    # Run the Tkinter main loop
    window.mainloop()

# Check if the script is being run directly
if __name__ == '__main__':
    # Call the function to test website connectivity
    test_connectivity()
