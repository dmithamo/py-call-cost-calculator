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

    def test_call_duration_calculation(self):
        '''Test the function that calculates call duration in seconds'''
        self.assertEqual(self.my_call.calculate_call_duration(
            datetime.time(10, 30, 30), datetime.time(12, 30, 30)), 7200)
        
    def test_if_time_is_of_peak(self):
        start_time = datetime.time(19, 20, 30)
        end_time = datetime.time(5, 20, 30)
        self.assertEqual(self.my_call.determine_if_off_peak(start_time, end_time), True)

        start_time2 = datetime.time(11, 10, 10)
        end_time2 = datetime.time(15, 10, 10)
        self.assertEqual(self.my_call.determine_if_off_peak(start_time2, end_time2), False)
        
    def test_if_call_long_distance_calculation(self):
        '''Test the function that marks a call as long distant or not'''
        self.assertEqual(self.my_call.determine_if_long_distant(), False)
        self.assertEqual(self.my_call.determine_if_long_distant(), True)
        
    def test_if_call_is_share_call_function(self):
        '''Test the function that marks a call as share-call or not'''
        self.assertEqual(self.my_call.determine_if_share_call(), True)
        self.assertEqual(self.my_call.determine_if_share_call(), False)
        
if __name__ == '__main__':
    unittest.main()
