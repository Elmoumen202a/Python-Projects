import speedtest

def main():
    """
    Main function to demonstrate getting Wifi speed and printing the results.
    """
    download_speed, upload_speed = get_wifi_speed()
    print("Wifi Download Speed is ", download_speed)
    print("Wifi Upload Speed is ", upload_speed)
def get_wifi_speed():
    """
    Get Wifi download and upload speed using the speedtest library.
    Returns:
        tuple: Tuple containing download speed and upload speed.
    """
    wifi = speedtest.Speedtest()
    download_speed = wifi.download()
    upload_speed = wifi.upload()
    return download_speed, upload_speed



if __name__ == "__main__":
    main()