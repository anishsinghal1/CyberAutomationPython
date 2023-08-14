def update_file(import_file, remove_list):
    # Read in the initial contents of the file
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # Convert the contents to a list of IP addresses
    ip_addresses = ip_addresses.split()

    # Remove IP addresses from the remove_list if they exist in ip_addresses
    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)

    # Convert the IP addresses back to a string
    ip_addresses = "\n".join(ip_addresses)

    # Rewrite the file with the updated IP addresses
    with open(import_file, "w") as file:
        file.write(ip_addresses)

# Call the update_file() function with specified file and remove_list
update_file("data/allow_list.txt", ["192.168.25.60", "192.168.90.124", "192.168.60.153"])

# Read and display the updated file
with open("data/allow_list.txt", "r") as file:
    text = file.read()

print(text)

# Can be utilized to rerun the program with the same text file contents
ip_addresses = """ip address
192.168.25.60
192.168.205.12
192.168.97.225
192.168.6.9
192.168.52.90
192.168.158.170
192.168.90.124
192.168.186.176
192.168.133.188
192.168.203.198
192.168.201.40
192.168.218.219
192.168.52.37
192.168.156.224
192.168.60.153
192.168.58.57
192.168.69.116
"""

# Write `ip_addresses` to the "data/allow_list.txt" file
with open("data/allow_list.txt", "w") as file:
    file.write(ip_addresses)
