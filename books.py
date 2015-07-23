



def load_file(filename, delimiter, fields):
  def do_split(line):
    return [field.strip() for field in line.split(delimiter)]

  # I hope this isn't too code-golf-y
  with open(filename, 'r') as infile:
    return [ dict(zip(fields, do_split(line))) for line in infile]


def print_records(records):
  for record in records:
    print "%(last)s, %(first)s, %(title)s, %(pubdate)s" % record


# using the list sort method, but sorted might be a better choice,
# depending on what you're doing.

def sort_records(records, field, descending=False):
  records.sort(key=lambda x:x['last'], reverse=descending)
 
records  = load_file('slash', '/', ['pubdate','first','last','title'])
records += load_file('csv', ',', ['title','last','first','pubdate'])
records += load_file('pipe', '|', ['first','last','title','pubdate'])


print_records(records)
print "---"
sort_records(records, 'last')
print_records(records)
  
