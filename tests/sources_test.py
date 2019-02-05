import unittest
from app.models import sources

Sources = sources.Sources

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("thisnews","Thisnews","This is the best news","https://google.com","general","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

