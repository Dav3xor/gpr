import unittest
from StringIO import StringIO

from record_processing import load_file, sort_records

class TestSortRecords(unittest.TestCase):
  def test_normal_use(self):
    records = [ {'a':1, 'b':2, 'c': 3},
                {'a':4, 'b':1, 'c': 4} ]
    sort_records(records, 'b')
    self.assertEqual(records, [ {'a':4, 'b':1, 'c': 4},
                                {'a':1, 'b':2, 'c': 3} ])
  def test_reverse_order(self):
    records = [ {'a':1, 'b':2, 'c': 3},
                {'a':4, 'b':1, 'c': 4} ]
    sort_records(records, 'a', True)
    self.assertEqual(records, [ {'a':4, 'b':1, 'c': 4},
                                {'a':1, 'b':2, 'c': 3} ])
  def test_bad_key(self):
    records = [ {'a':1, 'b':2, 'c': 3},
                {'a':4, 'b':1, 'c': 4} ]
    with self.assertRaises(KeyError):
      sort_records(records, 'd', True)
  
   
class TestLoadFile(unittest.TestCase):
  # tests a normal, successful run.
  def test_normal_use(self):
    records = load_file('csv', ',', ['title','last','first','year'])
    self.assertEqual(records, [{'year': '2008', 
                                'first': 'Robert', 
                                'last': 'Martin', 
                                'title': 'Clean Code'}, 
                               {'year': '2008', 
                                'first': 'James', 
                                'last': 'Shore', 
                                'title': 'The Art of Agile Development'}] )

  def test_no_file(self):
    # test wrong file name
    self.assertRaisesRegexp(IOError, 
                            "No such file or directory: 'csx'", 
                            load_file,
                            'csx', ',', ['title','last','first','year'])

  def test_too_few_columns(self):
    # Too few columns specified for data.
    # currently, it silently loads the columns specified, and
    # ignores the extras.

    # this is likely a bad behavior, just keeping it simple.
    records = load_file('csv', ',', ['title','last','first'])
    self.assertEqual(records, [{'first': 'Robert', 
                                'last': 'Martin', 
                                'title': 'Clean Code'}, 
                               {'first': 'James', 
                                'last': 'Shore', 
                                'title': 'The Art of Agile Development'}] )

  def test_too_many_columns(self):
    # too many columns specified for data
    # same as above, except it ignores the extra specified columns
    records = load_file('csv', ',', ['title','last','first', 'year', 'bogus'])
    self.assertEqual(records, [{'year': '2008', 
                                'first': 'Robert', 
                                'last': 'Martin', 
                                'title': 'Clean Code'}, 
                               {'year': '2008', 
                                'first': 'James', 
                                'last': 'Shore', 
                                'title': 'The Art of Agile Development'}] )
    
  def test_filter(self):
    # a filter that matches one record, but not both
    records = load_file('csv', ',', ['title','last','first','year'], 'James')
    self.assertEqual(records, [ {'year': '2008', 
                                 'first': 'James', 
                                 'last': 'Shore', 
                                 'title': 'The Art of Agile Development'}] )

    # a filter that will match no records
    records = load_file('csv', ',', ['title','last','first','year'], 'Beeblebrox')
    self.assertEqual(records, [] )
   
    # a filter that will match all records 
    records = load_file('csv', ',', ['title','last','first','year'], '2008')
    self.assertEqual(records, [{'year': '2008', 
                                'first': 'Robert', 
                                'last': 'Martin', 
                                'title': 'Clean Code'}, 
                               {'year': '2008', 
                                'first': 'James', 
                                'last': 'Shore', 
                                'title': 'The Art of Agile Development'}] )
    
if __name__ == '__main__':
  unittest.main()

