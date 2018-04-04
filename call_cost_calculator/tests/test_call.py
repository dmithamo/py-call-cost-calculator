''''
Unittests for the Call class
'''

import unittest
import datetime
from call_cost_calculator.call import Call 

class TestCall(unittest.TestCase):
    '''Define the parent class to contain the test cases'''

    def setUp(self):
        '''Instantiate an instance of the class Call for testing'''
        self.my_call = Call()

    def test_call_duration(self):
        self.assertEqual(self.my_call.calculate_call_duration(
            datetime.time(10, 30, 30), datetime.time(12, 30, 30)), 7200)
    
if __name__ == '__main__':
    unittest.main()
