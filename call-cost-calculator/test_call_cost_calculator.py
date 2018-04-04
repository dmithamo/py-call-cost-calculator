''''
Unittests for the Call class
'''

import unittest
from call_cost_calculator import Call 

class TestCall(unittest.TestCase):
    '''Define the parent class to contain the test cases'''

    def setUp(self):
        '''Instantiate an instance of the class Call for testing'''
        self.my_call = Call()
    
    def test_call_params(self):
        self.assertTrue(hasattr(self.my_call, "call_start_time"))

if __name__ == '__main__':
    unittest.main()
