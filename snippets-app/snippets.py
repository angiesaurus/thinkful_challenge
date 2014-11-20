import logging
import csv

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
