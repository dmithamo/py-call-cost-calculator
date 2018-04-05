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
        # Collect a call_start_time and call_end_time and calculate call_duration
        call_start_time, call_end_time = self.my_call.collect_call_time()
        call_duration = self.my_call.calculate_call_duration(
            call_start_time, call_end_time)
        self.assertEqual(call_duration, 7200)

    def test_off_peak_determination(self):
        '''Test the function that determines whether call time is off peak or not'''
        # Collect call start time and end time
        call_start_time = self.my_call.collect_call_time()[0]
        self.assertEqual(self.my_call.determine_if_off_peak(
            call_start_time), True)

    def test_long_distance_calculation(self):
        '''Test the function that marks a call as long distant or not'''
        self.assertEqual(self.my_call.determine_if_long_distant(), False)
        self.assertEqual(self.my_call.determine_if_long_distant(), True)

    def test_share_call_function(self):
        '''Test the function that marks a call as share-call or not'''
        self.assertEqual(self.my_call.determine_if_share_call(), True)
        self.assertEqual(self.my_call.determine_if_share_call(), False)
    
    def test_basic_cost_calculation(self):
        '''Test calculation of basic call cost - 5second, long distant, off-peak call'''
        self.assertEqual(self.my_call.calculate_cost(), (23.75, 11.875, 11.875))

    def test_basic_cost_calculation_2(self):
        '''Test calculation of basic call cost - 5second, long distant, not off-peak call'''
        self.assertEqual(self.my_call.calculate_cost(), (23.75, 0.00, 23.75))
    
    def test_basic_cost_calculation_3(self):
        '''Test calculation of basic call cost - 5second, short distant, off-peak call'''
        self.assertEqual(self.my_call.calculate_cost(), (12.50, 5.0, 7.50))

    def test_basic_cost_calculation_4(self):
        '''Test calculation of basic call cost - 5second, short distant, not off-peak call'''
        self.assertEqual(self.my_call.calculate_cost(), (12.50, 0.00, 12.50))

if __name__ == '__main__':
    unittest.main()
