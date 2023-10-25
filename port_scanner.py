#made by :hatim;saad;youness
#cd /path/port_scanner.py
#python port_scanner.py
import socket

import pyfiglet

def print_banner(text):

    font = pyfiglet.Figlet()

    ascii_art = font.renderText(text)

    print(ascii_art)

print_banner("Samir and Hatim Tool")
print("made by:HATIM,SAAD,YOUNESS")
print("suppervised by : samir.B")
print("_________________________")

def scan_ports(target, ports):

    open_ports = []

    for port in ports:

        try:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.settimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:

                open_ports.append(port)

            sock.close()

        except KeyboardInterrupt:

            print("Scan interrupted by user.")

            return open_ports

        except socket.gaierror:

            print("Hostname could not be resolved.")

            return open_ports

        except socket.error:

            print("Could not connect to server.")

            return open_ports

    return open_ports



def main():

    target = input("Enter the target IP address: ")

    port_range = input("Enter the range of ports to scan (e.g., 1-100): ")

    start, end = map(int, port_range.split('-'))

    ports = list(range(start, end + 1))



    open_ports = scan_ports(target, ports)



    if open_ports:

       print(f"Open ports on {target}: {', '.join(map(str, open_ports))}")

    else:

       print(f"No open ports found on {target}.")





if __name__ == "__main__":

    main()

