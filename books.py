import argparse

arguments = {'--filter':  { 'help': 'string to find', 
                            'type': str },
             '--year':    { 'help': 'sort by year, ascending' },
             '--reverse': { 'help': 'reverse sort order' } }
              



files = [ ['slash', '/', ['pubdate','first','last','title']],
          ['csv',   ',', ['title','last','first','pubdate']],
          ['pipe',  '|', ['first','last','title','pubdate']] ]


def load_file(filename, delimiter, fields):
  def do_split(line):
    return (field.strip() for field in line.split(delimiter))

  # I hope this isn't too code-golf-y
  with open(filename, 'r') as infile:
    return [ dict(zip(fields, do_split(line))) for line in infile]


def print_records(records):
  for record in records:
    print "%(last)s, %(first)s, %(title)s, %(pubdate)s" % record


# using the list sort method, but sorted might be a better choice,
# depending on what you're doing. sorted has more of the FP nature.
def sort_records(records, field, descending=False):
  records.sort(key=lambda x:x['last'], reverse=descending)



records = []
for file in files:
  records += load_file(*file) 

print_records(records)
print "---"
sort_records(records, 'last')
print_records(records)
  
