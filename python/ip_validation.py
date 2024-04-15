#input:"101.102.01.05"
#output:valid or not1


def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    
    return True

# give the input and test the function now
ip = input("Enter an IPv4 address: ")
if is_valid_ipv4(ip):
    print(" valid IPv4 address")
else:
    print("not a valid IPv4 address.")