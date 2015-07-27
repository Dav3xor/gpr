

# using the list sort method, but sorted might be a better choice,
# depending on what you're doing. sorted has more of the FP nature.
def sort_records(records, field, descending=False):
    """ Sort a list of dictionaries.

    Arguments:
      - records -- a list of dictionaries
      - field   -- the dictionary key to sort on
      - descending -- specify ascending or descending order (boolean)
    """
    records.sort(key=lambda x:x[field], reverse=descending)

def load_file(filename, delimiter, fields, filter=None):
    """ Load a list of records.

    Arguments:
      - filename -- the file to be processed
      - delimiter -- the character to split on for fields
      - fields -- a list of names for fields -- ['firstname','lastname','birthday'...]
      - filter -- a text string to filter on.
    """

    def do_split(line):
        # using yield would be more explicit, but a generator
        # expression is cleaner.
        return (field.strip() for field in line.split(delimiter))

    # I hope this isn't too code-golf-y
    with open(filename, 'r') as infile:
        return [ dict(zip(fields, 
                          do_split(line))) 
                 for line in infile
                     if (not filter) or (filter in line)]

