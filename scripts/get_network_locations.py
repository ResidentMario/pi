"""
Running this scripts returns the IP addresses on the current network that correspond with Raspberry
Pi machines and prints them out.
"""
import socket

n = 0
out = ''
while True:
    proposed_hostname = f'raspberrypi{n}'
    try:
        host_ip = socket.gethostbyname(proposed_hostname)
        out += f'The {proposed_hostname} hostname maps to the {host_ip} IP address.\n'
        n += 1
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        if n == 0:
            print("No Raspberry Pi devices were found.")
        else:
            print(out)
        break
