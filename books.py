import argparse
from record_processing import sort_records, load_file


def print_records(records):
  """print a list of book records."""
  for record in records:
    print "%(last)s, %(first)s, %(title)s, %(pubdate)s" % record

# keep all the file info in one place, where it's easy to add
# another file if you want.
files = [ ['slash', '/', ['pubdate','first','last','title']],
          ['csv',   ',', ['title','last','first','pubdate']],
          ['pipe',  '|', ['first','last','title','pubdate']] ]




arguments = {'--filter':  { 'help': 'show a subset of books, looks for the argument as a substring of any of the fields', 
                            'type': str },
             '--year':    { 'help': 'sort the books by year, ascending instead of default sort',
                            'action': 'store_true' },
             '--reverse': { 'help': 'reverse sort', 
                            'action': 'store_true' } }
              

parser = argparse.ArgumentParser(description="Show a list of books, alphabetical ascending by author's last name")
for argument, options in arguments.iteritems():
  parser.add_argument(argument, **options)
args = parser.parse_args()

sort_key     = 'pubdate'        if args.year    else 'last'
reverse_sort = True             if args.reverse else False



records = []
for file in files:
  records += load_file(*file, filter=args.filter) 

print_records(records)
print "---"
sort_records(records, sort_key, reverse_sort)
print_records(records)
  
