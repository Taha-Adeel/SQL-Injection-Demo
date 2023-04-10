import nmap # To scan for open ports for a given ip address
import requests # To send HTTP requests
import re # To search for the flag in the html source code
import subprocess # To run bash commands

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

def get_flag_from_HTML(html: str):
	# Search for the flag in the html sorce code. The flag is of the form flagN{...}, where N is a number
	print('Searching for flag in HTML source code ...')
	flag = re.findall('flag\d{1}\{[^\}]+\}', html)
	if flag:
		return flag[0]
	else:
		print('Flag not found in HTML source code')
		return None


def get_flag_1():
	url = 'http://' + ip + ':' + ports[1]
	print(f'Getting flag from {url} ...')

	response = requests.get(url)

	if response.status_code == 200:  # If the request is successful
		html_source_code = response.text  # Retrieve the HTML source code
		print(html_source_code)  # Print the HTML source code
		flag = get_flag_from_HTML(html_source_code)  # Search for the flag in the HTML source code
		if flag:
			print(f'Flag found: {flag}')
	else:
		print(f"Error: {response.status_code} {response.reason}")  # Print the error message


	return

def get_flag_2():
	return 'flag2{Cybersecurity_is_not_just_about_technology,_it\'s_also_about_people}'

def get_flag_3():
	return 'flag3{I\'ve_got_my_tin_foil_hat_on}'

def get_flag_4():
	return 'flag4{I\'m_not_sure_if_this_is_a_good_idea}'



ip = '10.200.15.248'
# ip = input('Enter IP address: ')

ports = ['22', '4451', '4461']
# ports = get_open_ports(ip)

get_flag_1()