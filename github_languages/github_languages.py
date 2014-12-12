import sys
import operator
from collections import defaultdict
from secret import USERNAME, PASSWORD

import requests

def get_repositories(user):
	#Gets a list of the user's get_repositories
	url = "https://api.github.com/users/{user}/repos".format(user=user)
	response = requests.get(url, auth=(USERNAME, PASSWORD))
	return response.json()

def main():
	repositories = get_repositories(sys.argv[1])
	print repositories

if __name__ == '__main__':
	main()