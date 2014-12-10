import logging
import csv
import argparse
import sys

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    pass

# def write_csv(data, path):
# 	"""
# 	writes data to a CSV file path
# 	"""
# 	with open(path, 'wb') as csv_file:
# 		writer = csv.writer(csv_file, delimiter=',')
# 		for line in data:
# 			writer.writerow(line)

# if __name__=='__main__':
# 	data = []
# 	path = ''
# 	csv_writer(data,path)


def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file")
        writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet

def get(name, filename):
    """Retrieve a snippe with an associated name in the CSV file"""
    logging.debug("Opening file")
    description = "Retrieve snippets of text"
    with open(filename, 'rb') as csvfile:
        snippet_reader = csv.reader(csvfile)
        for row in snippet_reader:
            if name in row:
                yield row


def main(arguments):
    """Main Function"""
    logging.info("Starting snippets")
    #convert parsed arguments from Namespace to dictionary
    command = arguments.pop("command")

    if command == 'put':
        name, snippet = put(**arguments)
        print "Stored {!r} as {!r}".format(snippet, name)

    if command == 'get':
        results = [x for x in get(**arguments)]
        if results:
            print results
        else:
            print "ERROR - Name is nonexistent!!!!!!!!!"

    # else:
    #     print "Snippet is nonexistent"

if __name__== "__main__":
    logging.info("Constructing Parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("filename", default="snippets.csv", nargs="?",
                            help="The snippet filename")

    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of something")
    get_parser.add_argument("filename", default="snippets.csv", nargs='?', help="The snippet filename")
    arguments = parser.parse_args(sys.argv[1:])
    arguments = vars(arguments)
    main(arguments)







