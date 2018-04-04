''''
Unittests for the Call class
'''

import unittest
from call_cost_calculator.call import Call 

class TestCall(unittest.TestCase):
    '''Define the parent class to contain the test cases'''

    def setUp(self):
        '''Instantiate an instance of the class Call for testing'''
        self.my_call = Call()

    def test_has_all_parameters(self):
        pass
        
    
if __name__ == '__main__':
    unittest.main()
