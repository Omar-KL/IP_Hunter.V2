import ipinfo
import threading
import socket
from colored import fg, bg
from time import sleep

color1 = bg(16)
color2 = fg(1)
color8 = fg(21)
color4 = fg(165)
color5 = fg(11)
color6 = fg(93)
color7 = fg(15)
color8 = fg(14)

print(color1 + "")
print(color6 + """
  _____   _____                     
 |_   _| |  __ \                    
   | |   | |__) |                   
   | |   |  ___/                    
  _| |_  | |                        
 |_____| |_|                                              
        _____            __         
       |_   _|          / _|        
         | |    _ __   | |_    ___  
         | |   | '_ \  |  _|  / _ \ 
        _| |_  | | | | | |   | (_) |
       |_____| |_| |_| |_|    \___/ 

""""")
print("=" * 50)
print("Made it By Omar-KL")
print("Instagram: @1_k1e")
print("Youtube: https://www.youtube.com/@magician-teq")
print("Don't use it for Illegal Purposes.. ")
print("=" * 50)

while True:
    print(color8+"[1] "+color7+"IP Information.")
    print(color8+"[2] "+color7+"Open Ports Scanning.")
    print(color5+"="*50)

    choice = input(color8+"[+] "+color7+"Enter your choice: ")

    if choice == "1":
        try:
            print(color2+" NOTE: "+color7+"To get a Token you have to create an Account at ipinfo.io")
            access_token = input(color2 + 'Enter Your Token: ')
            ip = input(color2 + "Enter Target IP Address: ")
            handler = ipinfo.getHandler(access_token)
            details = handler.getDetails(ip)

            print(color5 + "=" * 50)
            print(color8 + "Decimal: ", color4 + details.ip, end="\n")
            print(color8 + "Hostname: ", color4 + details.hostname, end="\n")
            print(color8 + "City: ", color4 + details.city, end="\n")
            print(color8 + "State/Region: ", color4 + details.region, end="\n")
            print(color8 + "Country: ", color4 + details.country_name, end="\n")
            print(color8 + "Postal: ", color4 + details.postal, end="\n")
            print(color8 + "timezone: ", color4 + details.timezone, end="\n")
            print(color8 + "Assignment: ", color4 + details.org, end="\n")
            print(color5 + "=" * 50)
            sleep(10)


        except:
            print(color5+"="*50)
            print(color4+"IP or Token is invalid, try again..")
            print(color5+"="*50)

    elif choice == "2":
        try:
            ip = input(color8+"[+] "+color7+"Enter the Target IP address: ")
            range_ports = input(color8+"[+] "+color7+"Enter the range of ports that you want to scan EX:(1, 100): ")
            print(color8+"[*] "+color7+"the scan may take some minutes.. ")
            start, end = map(int, range_ports.split(','))

            def port_scan(ip):
                open_ports = []

                for port in range(start, end+1):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(1)

                    status = s.connect_ex((ip, port))

                    if status == 0:
                        try:
                            service = socket.getservbyport(port)
                        except OSError:
                            service = "Unknown"
                        open_ports.append((port, service))
                        s.close()

                if len(open_ports)>0:
                    print(color4+"*** Open Ports Found ***")
                    for port, service in open_ports:
                        print(color2+ f"{port} ({service})")
                        exit()
                else:
                    print(color4+"No Open Ports Found")
                    exit()

            port_scan(ip)
        except Exception as e:
            print("Error: ", e)
            exit()

    # Set the number of threads you want to use
            num_threads = 100
            # Divide the range of ports into chunks for each thread
            chunk_size = (end - start) // num_threads
            threads = []

            for i in range(num_threads):
                start_port = start + i * chunk_size
                end_port = start + (i + 1) * chunk_size - 1
                t = threading.Thread(target=port_scan, args=(ip, start_port, end_port))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

        except Exception as e:
            print("[+] Error: ", e)
            exit()
    else:
        print(color2+"*"*50)
        print(color7+"Invalid Value.. please try again..")
        print(color2+"*"*50)