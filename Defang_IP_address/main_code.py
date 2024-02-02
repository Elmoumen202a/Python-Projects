def ip_address(address):
    return "[.]".join(address.split("."))

# Example usage
ipaddress = ip_address("1.1.2.3")
print(ipaddress)