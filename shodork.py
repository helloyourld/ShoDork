import shodan
import os
import sys

SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"

api = shodan.Shodan(SHODAN_API_KEY)

print('''
 ______     __  __     ______     _____     ______     ______     __  __    
/\  ___\   /\ \_\ \   /\  __ \   /\  __-.  /\  __ \   /\  == \   /\ \/ /    
\ \___  \  \ \  __ \  \ \ \/\ \  \ \ \/\ \ \ \ \/\ \  \ \  __<   \ \  _"-.  
 \/\_____\  \ \_\ \_\  \ \_____\  \ \____-  \ \_____\  \ \_\ \_\  \ \_\ \_\ 
  \/_____/   \/_/\/_/   \/_____/   \/____/   \/_____/   \/_/ /_/   \/_/\/_/ 
                                                                            
''')

if len(sys.argv) != 3:
    print(
        f"Usage : python3 {sys.argv[0]} [-q <single-dork>] / [-f <filename>]")
    sys.exit(1)

option = sys.argv[1]
input_file = sys.argv[2]

if option == "-q":
    dorks = [input_file.strip()]
elif option == "-f":
    with open(input_file, 'r') as f:
        dorks = f.readlines()
        dorks = [d.strip() for d in dorks]
else:
    print("Invalid option. Use -q for single dork or -f for input file.")
    sys.exit(1)

ip_file = open("ips.txt", "w")

for dork in dorks:
    try:
        results = api.search(dork)
        print(f"Found {results['total']} results for dork: {dork}")

        for result in results['matches']:
            ip_file.write(result['ip_str'] + "\n")
    except shodan.APIError as e:
        print('Error: %s' % e)

print("Done! All IPs saved to ips.txt")
ip_file.close()
