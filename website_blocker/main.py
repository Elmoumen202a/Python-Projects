import time
from datetime import datetime as dt

# Path to the system's hosts file (may vary depending on your OS)
# For Windows: r"C:\Windows\System32\drivers\etc\hosts"
# For Linux/Mac: "/etc/hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# IP address to redirect blocked websites to
# This points to the local machine (localhost), effectively blocking the website
redirect_ip = "127.0.0.1"

# File that contains the list of websites to block
# Each website should be listed on a new line
websites_path = "websites.txt"

# Time settings: hours during which websites will be blocked
# For example, block websites from 9 AM to 5 PM
start_hour = 9  # Block websites starting from 9 AM
end_hour = 17   # Unblock websites after 5 PM

def read_websites(file_path):
    """
    Read the list of websites to block from the specified file.
    This function reads the websites.txt file and returns a list of websites.
    """
    with open(file_path, 'r') as file:
        # Read the websites, strip any extra spaces or newlines
        return [line.strip() for line in file if line.strip()]

def block_websites():
    """
    Block the websites by adding entries to the hosts file.
    This will redirect the websites to localhost, effectively blocking them.
    """
    websites = read_websites(websites_path)  # Get list of websites from file

    with open(hosts_path, 'r+') as file:
        # Read the current content of the hosts file
        content = file.read()

        # Loop through the websites and add them to the hosts file if not already blocked
        for website in websites:
            if website not in content:
                # Write a new line in the hosts file that maps the website to localhost
                file.write(f"{redirect_ip} {website}\n")

def unblock_websites():
    """
    Unblock websites by removing the entries from the hosts file.
    This will allow access to the websites again.
    """
    websites = read_websites(websites_path)  # Get list of websites from file

    with open(hosts_path, 'r+') as file:
        # Read all lines from the hosts file
        lines = file.readlines()

        # Go back to the beginning of the file to overwrite it
        file.seek(0)

        # Write back only the lines that do not contain the blocked websites
        for line in lines:
            # If the line does not contain any of the websites, write it back
            if not any(website in line for website in websites):
                file.write(line)

        # Truncate the file to remove any remaining blocked websites
        file.truncate()

def main():
    """
    Main function to run the website blocker.
    It checks every 5 minutes whether the current time is within the blocking hours.
    If it is, it blocks the websites; otherwise, it unblocks them.
    """
    while True:
        # Get the current hour
        current_hour = dt.now().hour

        # If the current time is within the blocking period
        if start_hour <= current_hour < end_hour:
            print("Working hours... Blocking websites.")
            block_websites()  # Block websites during work hours
        else:
            print("Free time... Unblocking websites.")
            unblock_websites()  # Unblock websites outside of work hours

        # Sleep for 5 minutes (300 seconds) before checking again
        time.sleep(300)

if __name__ == "__main__":
    main()  # Run the main function