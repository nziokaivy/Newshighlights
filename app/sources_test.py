import unittest
from models import movie
Sources = sources.Sources

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("thisnews","Thisnews","This is the best news",htttps://google.com,"general","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,SOurce))


if __name__ == '__main__':
    unittest.main()