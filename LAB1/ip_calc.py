"""
MODULE DOCSTRING
"""
import sys


def main():
    """
    MAIN FUNCTION
    """
    address = "192.168.10.10/16"
    print(checker(address))
    print(get_ip_from_raw_address(address))
    print(get_network_address_from_raw_address(address))
    print(get_broadcast_address_from_raw_address(address))
    print(get_binary_mask_from_raw_address(address))
    print(get_first_usable_ip_address_from_raw_address(address))
    print(get_penultimate_usable_ip_address_from_raw_address(address))
    print(get_number_of_usable_hosts_from_raw_address(address))
    print(get_ip_class_from_raw_address(address))
    print(check_private_ip_address_from_raw_address(address))

def checker(raw_address):
    """
    Checker of the ip
    >>> checker("91.124.230.205/30")
    True
    """
    try:
        ip_address, mask = raw_address.split("/")
    except ValueError:
        print("Missing prefix")
        sys.exit()
    try:
        if 0 <= int(mask) <= 32:
            pass
        else:
            return None
    except:
        print("Error")
        sys.exit()
    try:
        if ip_address.count(".") == 3:
            pass
        else:
            print("Error")
            sys.exit()
        ips = ip_address.split(".")
        for elem in ips:
            if 0 <= int(elem) <= 255:
                pass
            else:
                return None
    except:
        print("Error")
        sys.exit()
    return True

def bin_to_int(binary):
    """
    Makes binary into integer
    >>> bin_to_int("111")
    7
    """
    return int("0b" + str(binary), 2)

def int_to_bin(integer):
    """
    Makes integer into binary
    >>> int_to_bin(7)
    '111'
    """
    return bin(integer)[2:]

def get_ip_from_raw_address(raw_address: str) -> str:
    """
    Gets ip from raw address
    >>> get_ip_from_raw_address("91.124.230.205/30")
    '91.124.230.205'
    """
    if checker(raw_address) is None:
        return None
    ip_address, _ = raw_address.split("/")
    return ip_address

def get_network_address_from_raw_address(raw_address: str) -> str:
    """
    Gets network address from raw address
    >>> get_network_address_from_raw_address("91.124.230.205/30")
    '91.124.230.204'
    """
    if checker(raw_address) is None:
        return None
    ip_address, mask = raw_address.split("/")
    ips = ip_address.split(".")
    mask = int(mask)
    masks = []
    for _ in range(4):
        number = ""
        for _ in range(8):
            if mask > 0:
                mask -= 1
                number += "1"
            else:
                number += "0"
        masks.append(bin_to_int(number))
    address = []
    for index in range(4):
        address.append(str(int(ips[index]) & int(masks[index])))
    address_str = ".".join(address)
    return address_str

def get_binary_mask_from_raw_address(raw_address: str) -> str:
    """
    Gets binary mask from raw address
    >>> get_binary_mask_from_raw_address("91.124.230.205/30")
    '11111111.11111111.11111111.11111100'
    """
    if checker(raw_address) is None:
        return None
    _, mask = raw_address.split("/")
    mask = int(mask)
    masks = []
    for _ in range(4):
        number = ""
        for _ in range(8):
            if mask > 0:
                mask -= 1
                number += "1"
            else:
                number += "0"
        masks.append(number)
    return ".".join(masks)

def get_broadcast_address_from_raw_address(raw_address: str) -> str:
    """
    Gets broadcast address from raw address
    >>> get_broadcast_address_from_raw_address("91.124.230.205/30")
    '91.124.230.207'
    """
    if checker(raw_address) is None:
        return None
    ip_address, _ = raw_address.split("/")
    ips = ip_address.split(".")
    binary_mask = get_binary_mask_from_raw_address(raw_address).split(".")
    for elem_index in range(len(binary_mask)):
        elem = list(binary_mask[elem_index])
        for letter_index in range(len(binary_mask[elem_index])):
            if elem[letter_index] == "1":
                elem[letter_index] = "0"
            else:
                elem[letter_index] = "1"
        binary_mask[elem_index] = bin_to_int("".join(elem))
    address = []
    for index in range(4):
        address.append(str(int(ips[index]) | int(binary_mask[index])))
    return ".".join(address)

def get_first_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    Gets first usable ip address from raw address
    >>> get_first_usable_ip_address_from_raw_address("91.124.230.205/30")
    '91.124.230.205'
    """
    if checker(raw_address) is None:
        return None
    ips = list(get_network_address_from_raw_address(raw_address).split("."))
    for elem_index in range(len(ips)):
        if int(ips[-(elem_index + 1)]) != 255:
            ips[-(elem_index + 1)] = str(int(ips[-(elem_index + 1)]) + 1)
            break
        else:
            pass
    return ".".join(ips)

def get_penultimate_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    Gets penultimate usable ip address from raw address
    >>> get_penultimate_usable_ip_address_from_raw_address("91.124.230.205/30")
    '91.124.230.205'
    """
    if checker(raw_address) is None:
        return None
    ip_address, _ = raw_address.split("/")
    _ = list(ip_address.split("."))
    broadcast = list(get_broadcast_address_from_raw_address(raw_address).split("."))
    for elem_index in range(len(broadcast)):
        if int(broadcast[-(elem_index + 1)]) > 1:
            broadcast[-(elem_index + 1)] = str(int(broadcast[-(elem_index + 1)]) - 2)
            break
        else:
            pass
    return ".".join(broadcast)

def get_number_of_usable_hosts_from_raw_address(raw_address: str) -> int:
    """
    Gets number of usable hosts from raw address
    >>> get_number_of_usable_hosts_from_raw_address("91.124.230.205/30")
    2
    """
    if checker(raw_address) is None:
        return None
    _, mask = raw_address.split("/")
    return 2 ** (32 - int(mask)) - 2

def get_ip_class_from_raw_address(raw_address: str) -> str:
    """
    Gets ip class from raw address
    >>> get_ip_class_from_raw_address("91.124.230.205/30")
    'A'
    """
    if checker(raw_address) is None:
        return None
    ip_address, _ = raw_address.split("/")
    ips = ip_address.split(".")
    ranges = [128,192,224,240,255]
    classer = ["A", "B", "C", "D", "E"]
    for ranger in range(len(ranges)):
        if int(ips[0]) < ranges[ranger]:
            return classer[ranger]

def check_private_ip_address_from_raw_address(raw_address: str) -> bool:
    """
    Checks private ip address from raw address
    >>> check_private_ip_address_from_raw_address("91.124.230.205/30")
    False
    """
    if checker(raw_address) is None:
        return None
    ip_address, _ = raw_address.split("/")
    ips = ip_address.split(".")
    if int(ips[0]) == 10:
        return True
    elif int(ips[0]) == 172:
        if 16 <= int(ips[1]) <= 31:
            return True
        else:
            return False
    elif int(ips[0]) == 192:
        if int(ips[1]) == 168:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
