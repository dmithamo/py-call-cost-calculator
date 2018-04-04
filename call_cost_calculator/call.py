'''This simple program models using OOP the process of calculating 
the cost of a telephone call. 
'''

# Needed for computation of call duration, and to determine whether call
# is on- or off-peak.
import datetime 

class Call:
    '''Model a call with params as below:

    :param MINIMUM_COST_NEAR : The applicable minimum cost for a short distance call
    :type MINIMUM_COST_NEAR : float, constant
    
    :param MINIMUM_COST_FAR : The applicable minimum cost for a long distance call
    :type MINIMUM_COST_FAR : float, constant

    :param OFF_PEAK_START : Time when off-peak starts
    :type OFF_PEAK_START : datetime.time object

    :param OFF_PEAK_END : Time when off-peak ends
    :type OFF_PEAK_END : datetime.time object

    :param DISTANCE_DELIMITER : The preset for boundary value for short distances
    :type DISTANCE_DELIMITER : int, constant
    
    '''
    MINIMUM_COST_NEAR = 0.20
    MINIMUM_COST_FAR = 0.50
    

    def __init__(self, call_start_time=None, call_end_time=None, if_long_distance=None, if_share_call=None):
        '''Return an instance of a Call object
        :param call_start_time : time when call was initiated. Format HH:MM:SS
        :type call_start_time : datetime.time object

        :param call_end_time : time when call was terminated. Format HH:MM:SS
        :type call_end_time : date.time object

        :param if_long_distance : whether call distance exceeds DISTANCE_DELIMITER
        :type if_long_distance : boolean

        :param if_share_call : whether call was a share-call
        :type if_share_call : boolean

        '''
        self.call_start_time = call_start_time 
        self.call_end_time = call_end_time 
        self.if_long_distance = if_long_distance 
        self.if_share_call = if_share_call

    
    def collect_call_time(self):
        '''Ask for user-input for call_start_time and call_end_time
        '''
        # Determine call_start_time and call_end_time
        call_start_time = input("\nCall started at: Use this format - HH:MM:SS\n>>")
        call_end_time = input("\n\nCall finished at: Use this format - HH:MM:SS\n>>")

        # Convert to objects, and save as instance variables
        self.call_start_time = self.convert_time_to_object(call_start_time)
        self.call_end_time = self.convert_time_to_object(call_end_time)
        print("Started: %s\nFinished: %s" % (call_start_time, call_end_time))


    def convert_time_to_object(self, time_input):
        '''Global method used to convert input time into a time object
        '''
        # Time collected into a list of the hours, mins, and secs
        time_as_list = time_input.split(':')

        # Extract hours (hh), minutes (mm), seconds (ss) from time_as_list and use to make time object
        hh = int(time_as_list[0])
        mm = int(time_as_list[1])
        ss = int(time_as_list[2])

        time_object = datetime.time(hh, mm, ss)
        return time_object
