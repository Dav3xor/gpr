#!/usr/bin/env python2.7

import argparse

from record_processing import sort_records, load_file

"""
Hello!

I like to write a little discussion about my solution when
finishing up a coding test like this.  First of all, this was
a lot of fun!  I think you have designed a very good, pragmatic
test.  Honestly, I'd much rather do something like this than
reverse a binary tree on a whiteboard.

When I first looked at the problem, I thought "I could use the
csv module, it allows for custom delimiters, etc...".  Instead,
I rolled my own record loader.  The amount of actual code
is almost the same, and it allows me to show off some nice
functional composition things.

In real life, on a deadline, I would probably just use the csv
module and be done with it.

Simplicity -- take a look at the tests, there are a few compromises
made for simplicity.  If an exception is raised, I don't catch it
and let Python display the stack trace.  I'm assuming a technically
proficient user who can figure out what's going on.  If the data
is mismatched with the column definitions, it silently loads the
records, and either drops a column, or ignores extra ones.

Style -- Mostly pep8, although I like to put spaces after = to
line up related assignments.

Tests -- I think the tests are reasonably complete, given the size
of the dataset.  

Compact code is cool, but it can be difficult to read and 
maintain.  I strive for brevity, but try to keep it readable.
If I do too much on one line, I pull it apart.  I have
a tendency to make variables that may only be used once to
improve readability -- it sometimes makes my code look simple,
but I really do want to help the future maintainer.

Best Regards!
David
"""


def print_records(records):
    """print a list of book records."""
    for record in records:
        print "%(last)s, %(first)s, %(title)s, %(pubdate)s" % record


# keep all the file info in one place, where it's easy to add
# another file if you want.
files = [ ['slash', '/', ['pubdate','first','last','title']],
          ['csv',   ',', ['title','last','first','pubdate']],
          ['pipe',  '|', ['first','last','title','pubdate']] ]




# I couldn't help but notice the expected output of books.py was an exact match
# with what the argparse library would output.  :)
arguments = {'--filter':  { 'help': 'show a subset of books, ' + \
                                    'looks for the argument as a ' + \
                                    'substring of any of the fields', 
                            'type': str },
             '--year':    { 'help': 'sort the books by year, ascending ' + \
                                    'instead of default sort',
                            'action': 'store_true' },
             '--reverse': { 'help': 'reverse sort', 
                            'action': 'store_true' } }

description = "Show a list of books, alphabetical ascending by author's " + \
              "last name"
parser      = argparse.ArgumentParser(description)

for argument, options in arguments.iteritems():
    parser.add_argument(argument, **options)

args = parser.parse_args()

sort_key     = 'pubdate'        if args.year    else 'last'
reverse_sort = True             if args.reverse else False



records = []
for file in files:
    records += load_file(*file, filter=args.filter) 

sort_records(records, sort_key, reverse_sort)
print_records(records)
  
