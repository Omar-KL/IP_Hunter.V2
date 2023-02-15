import subprocess
import socket
import os
import sys
from colored import fg,bg
import time
import ipinfo

white = fg(15)
aqua = fg(14)
green = fg(10)
pink = fg(201)
yellow = fg(11)
black_bg = bg(16)
light_purp = fg(54)
red = fg(1)
light_purp = fg(93)
black = fg(16)

msg = (light_purp+"""
  _____   _____                                      
 |_   _| |  __ \                                     
   | |   | |__) |                                    
   | |   |  ___/                                     
  _| |_  | |                                         
 |_____| |_|                                         
          _    _                   _                 
         | |  | |                 | |                
         | |__| |  _   _   _ __   | |_    ___   _ __ 
         |  __  | | | | | | '_ \  | __|  / _ \ | '__|
         | |  | | | |_| | | | | | | |_  |  __/ | |   
         |_|  |_|  \__,_| |_| |_|  \__|  \___| |_|                                                            
""")
def typewriter(msg):
    for chart in msg:
        sys.stdout.write(chart)
        sys.stdout.flush()
        if chart != "\n":
            time.sleep(0)
        else:
            time.sleep(0.30)
typewriter(msg)

print(yellow+"=" * 50)
print(light_purp + "Made it By Omar-KL")
print(light_purp + "Instagram: @1_k1e")
print(light_purp + "Youtube: https://www.youtube.com/@magician-teq")
print(light_purp + "Don't use it for Illegal Purposes.. ")
print(yellow+"=" * 50)


print(aqua + "[1] " + white + "IP Information.")
print(aqua+"[2] " + white + "IP Scan For Vulnerabilities.")
print(yellow+"="*50)
choice = input(aqua + "[+] " + white + "Enter your choice: ")
filename = "output.txt"

if choice == "1":
    try:
        print(red + " NOTE: " + white + "To get a Token you have to create an Account at ipinfo.io")
        access_token = input(aqua+"[*] " +white + 'Enter Your Token: ')
        ip = input(aqua+ "[*] " +white + "Enter Target IP Address: ")
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip)

        print(yellow + "=" * 50)
        print(aqua + "Decimal: ", pink + details.ip, end="\n")
        print(aqua + "Hostname: ", pink + details.hostname, end="\n")
        print(aqua + "City: ", pink + details.city, end="\n")
        print(aqua + "State/Region: ", pink + details.region, end="\n")
        print(aqua + "Country: ", pink + details.country_name, end="\n")
        print(aqua + "Postal: ", pink + details.postal, end="\n")
        print(aqua + "timezone: ", pink + details.timezone, end="\n")
        print(aqua + "Assignment: ", pink + details.org, end="\n")
        print(yellow + "=" * 50)
        print("")
        with open("output.txt", "a") as file:
            file.write("Decimal: " + details.ip + "\n")
            file.write("Hostname: " + details.hostname + "\n")
            file.write("City: " + details.city + "\n")
            file.write("State/Region: " + details.region + "\n")
            file.write("Country: " + details.country_name + "\n")
            file.write("Postal: " + details.postal + "\n")
            file.write("timezone: " + details.timezone + "\n")
            file.write("Assignment: " + details.org + "\n")
            file.write("=" * 50 + "\n")

    except Exception as e:
        print(yellow + "=" * 50)
        print(pink + "Error: ", e)
        print(yellow + "=" * 50)

elif choice == "2":
    try:
        def scan_ip(ip, ports_list):
            try:
                socket.inet_aton(ip)
                # First command: "nmap [ip] -O"
                nmap_os_command = f"nmap {ip} -p {ports} -O"
                os_info = subprocess.run(nmap_os_command, shell=True, stdout=subprocess.PIPE)
                os_info = os_info.stdout.decode('utf-8')

                # Second command: "sudo nmap -sV --script=nmap-vulners"
                nmap_exploits_command = f"nmap -sV -p {ports}  --script=vulners {ip}"
                exploits = subprocess.run(nmap_exploits_command, shell=True, stdout=subprocess.PIPE)
                exploits = exploits.stdout.decode('utf-8').split('\n')
                limited_exploits = exploits[:30]
                # Print the output of both commands
                print(pink + "=" * 100)
                print(white+"OS Information:")
                print(pink + "=" * 100)
                print(aqua+os_info)

                if not os.path.exists(filename):
                    with open(filename, "w") as file:
                        file.write(light_purp + "This is a new file:" + "\n")
                        with open(filename, "a") as f:
                            f.write(os_info + "\n")
                            f.write(" ")
                        for exploit in limited_exploits:
                            print(aqua+exploit)
                            with open(filename, "a") as f:
                                f.write(exploit + "\n")
                else:
                    with open(filename, "a") as f:
                        f.write(os_info + "\n")
                        f.write(" ")
                        print(pink + "=" * 100)
                        print(white+"Vulnerabilities:")
                        print(pink + "=" * 100)
                    for exploit in limited_exploits:
                        print(aqua+exploit)
                        with open(filename, "a") as f:
                            f.write(exploit + "\n")
                    with open(filename, "a") as f:
                        f.write("="*100 + "\n")

            except socket.error:
                print(red+"Invalid IP Address..")
                exit()

        # Ask the user whether they want to scan one IP or multiple IPs
        choice = input(aqua+"[+] " +white+ "Do you want to scan one IP or multiple IPs? (1/m): ")

        if choice == '1':
            def get_ports_list(ports_input):
                try:
                    if '-' in ports_input:
                        start, end = map(int, ports_input.split('-'))
                        return list(range(start, end + 1))
                    else:
                        return [int(ports_input)]
                except ValueError:
                    return []
            ports = input(aqua+"[+] " +white+ "Enter the Ports to scan (e.g. 80 or 1-100): ")
            ports_list = get_ports_list(ports)
            if not ports_list:
                print(red+"Invalid ports format, try again..")
                exit()
            ip = input(aqua+"[+] " +white+ "Enter the IP address to scan: ")
            msg1=(red+"[*] Working On It...")
            def typewriter(msg1):
                for chart in msg1:
                    sys.stdout.write(chart)
                    sys.stdout.flush()
                    if chart != "\n":
                        time.sleep(0.050)
                    else:
                        time.sleep(0.5)
            typewriter(msg1)
            print(" ")
            scan_ip(ip, ports_list)



        elif choice == 'm':
            def get_ports_list(ports_input):
                try:
                    if '-' in ports_input:
                        start, end = map(int, ports_input.split('-'))
                        return list(range(start, end + 1))
                    else:
                        return [int(ports_input)]
                except ValueError:
                    return []
            ports = input(aqua+"[+] " +white+ "Enter the Ports to scan (e.g. 80 or 1-100): ")
            ports_list = get_ports_list(ports)
            if not ports_list:
                print(red+"Invalid ports format, try again..")

            file_path = input(aqua+"[+] " +white+ "Enter the path of the file containing the IP addresses: ")
            try:
                with open(file_path, 'r') as f:
                    ips = f.readlines()
                for ip in ips:
                    scan_ip(ip.strip(), ports_list)
            except FileNotFoundError:
                print(red+"File Not Found, Please Try Again...")
        else:
            print(red+"Invalid choice, try again.")
    except Exception as e:
        print("Error: ", e)
else:
    print(red + "Invalid choice, try again.")
