import socket
from IPy import IP


def get_banner(s):
    '''
    get_banner function grabs the banner by recieving data from the open ports to tell us what service
    is running over the open port. 1024 bytes data is enough for a banner.
    '''
    return s.recv(1024)

def scan_port(ipaddress, port):
    '''
    scan_port function takes 2 parameters:
    ipaddress and port.
    Establishes the connection with our target by sending requests to every port and analyzing the
    responses and then prints the open poet with the banners (if any). We set the timeout of 0.5 to
    speed up the process. 
    Accuracy:
    higher - higher timeout
    low - lower timeout
    At the end of the function we pass to neglect closed and filtered ports
    '''
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open port ' + str(port) + ':' + str(banner.decode().strip('\n').strip('\r')))
        except:
            print('[+] Open port ' + str(port))
    except:
        pass

def check_ip(ip):
    '''
    check_ip function only takes one parameter: ip.
    It checks if the user entered the target in the right ip address format, if yes, returns the 
    ip. If no, we convert the hostname to the right ip address format and return it back.
    '''
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan(target, port_num):
    '''
    scan function takes two parameters:
    target and port_num
    It passes the target to chec_ip function handle edge case where user entered hostname.
    we convert it to the right ip address format. After that we iterate over the user specified
    port numbers and pass the converted_ip and port tot he scan_port function.
    '''
    converted_ip = check_ip(target)
    print('\n'+'[scanning targets ...] ' + str(target))
    for port in range(1, port_num):
        scan_port(converted_ip, port)

if __name__ == "__main__":
    '''
    We ask the user to enter the target or multiple targets and then the port number to be scanned.
    Incase of multiple targets, we split the targets and pass them one by one with the port numbers
    to the scan function.
    '''
    targets = input('[+] Enter target/s to scan (split multiple targets with ,): ')
    port_number = int(input('[+] Enter number of ports you want to scan: '))
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '),port_number)
    else:
        scan(targets, port_number)
