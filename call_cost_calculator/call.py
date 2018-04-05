'''This simple program models using OOP the proces of calculating 
the cost of a telephone call. 
'''

# Needed for computation of call duration, and to determine whether call
# is on- or off-peak.
import datetime


class Call:
    '''Model a call with clas params as below:

    :param MINIMUM_COST_NEAR : The applicable minimum cost for a short distance call
    :type MINIMUM_COST_NEAR : float, constant
    :param MINIMUM_COST_FAR : The applicable minimum cost for a long distance call
    :type MINIMUM_COST_FAR : float, constant

    :param PER_SECOND_COST_NEAR : The applicable cost per second of a short distance call
    :type PER-SECOND_COST_NEAR : float, constant


    :param PER_SECOND_COST_FAR : The applicable cost per second of a long distance call
    :type PER-SECOND_COST_FAR : float, constant


    :param OFF_PEAK_START : Time when off-peak starts
    :type OFF_PEAK_START : datetime.time object

    :param OFF_PEAK_END : Time when off-peak ends
    :type OFF_PEAK_END : datetime.time object

    :param DISTANCE_DELIMITER : The preset for boundary value for short distances
    :type DISTANCE_DELIMITER : int, constant

    :param VAT : The preset for boundary value for short distances
    :type VAT : float, constant

    '''
    # All money is in Ksh.
    MINIMUM_COST_NEAR = 10.00
    MINIMUM_COST_FAR = 20.00

    PER_SECOND_COST_NEAR = 0.50
    PER_SECOND_COST_FAR = 0.75

    OFF_PEAK_START = datetime.time(19, 0, 0)  # 19:00:00
    OFF_PEAK_END = datetime.time(6, 59, 59)  # 06:59:59

    OFF_PEAK_DISCOUNT_NEAR = 0.40
    OFF_PEAK_DISCOUNT_FAR = 0.50

    DISTANCE_DELIMITER = 50  # km

    VAT = 0.14  # Charged on final cost

    def __init__(self, call_start=None, call_end=None, long_distant=None, share_call=None):
        '''Return an instance of a Call object with instance variables as below
        :param call_start : time when call was initiated. Format h:m:s
        :type call_start : datetime.time object

        :param call_end : time when call was terminated. Format h:m:s
        :type call_end : date.time object

        :param long_distant : whether call distance exceeds DISTANCE_DELIMITER
        :type long_distant : boolean

        :param share_call : whether call was a share-call
        :type share_call : boolean

        '''
        self.call_start = call_start
        self.call_end = call_end
        self.long_distant = long_distant
        self.share_call = share_call

    def collect_call_time(self):
        '''Ask for user-input for call_start and call_end
        '''
        # Determine call_start and call_end
        call_start = input(
            "\nCall started at: Use this format - h:m:s\n>>")
        call_end = input(
            "\n\nCall finished at: Use this format - h:m:s\n>>")

        # Convert to objects, and save as instance variables
        self.call_start = self.convert_time_to_object(call_start)
        self.call_end = self.convert_time_to_object(call_end)
        return (self.call_start, self.call_end)

    def convert_time_to_object(self, time_input):
        '''Global method used to convert input time into a time object
        '''
        # Time collected into a list of the hours, mins, and secs
        time_as_list = time_input.split(':')

        # Extract hours (h), minutes (m), seconds (s) from time_as_list and use to make time object
        h = int(time_as_list[0])
        m = int(time_as_list[1])
        s = int(time_as_list[2])

        self.time_object = datetime.time(h, m, s)
        return self.time_object

    def calculate_call_duration(self, call_start, call_end):
        '''Calculate length of call in seconds'''

        starting_time_in_secs = call_start.hour * 3600 + \
            call_start.minute * 60 + call_start.second

        ending_time_in_secs = call_end.hour * 3600 + \
            call_end.minute * 60 + call_end.second

        self.call_duration = ending_time_in_secs - starting_time_in_secs

        return self.call_duration

    def determine_if_off_peak(self, call_start):
        '''Return bool marking call as off-peak or not'''
        if call_start >= Call.OFF_PEAK_START:
            self.is_off_peak = True
        else:
            self.is_off_peak = False
        return self.is_off_peak

    def determine_if_long_distant(self):
        '''Return bool indicating whether call is long distant or not'''
        call_distance = input(
            "\nHow far off is this call made? Enter an estimate in km:\n>>")

        if int(call_distance) >= Call.DISTANCE_DELIMITER:
            self.long_distant = True

        elif int(call_distance) < Call.DISTANCE_DELIMITER:
            self.long_distant = False

        return self.long_distant

    def determine_if_share_call(self):
        '''Return bool marking call as share_call or not'''
        is_share_call = input(
            "\nIs this a share-call? Enter 'y' for yes, 'n' for no\n>>").lower()
        if is_share_call == 'y':
            self.is_share_call = True
        elif is_share_call == 'n':
            self.is_share_call = False
        return self.is_share_call
    
    def calculate_cost(self):
        '''Collect all params, call appropriate method for cost calculation'''
        call_start_time, call_end_time = self.collect_call_time()
        is_off_peak = self.determine_if_off_peak(call_start_time)
        is_long_distant = self.determine_if_long_distant()

        # Call appropriate cost calculation method
        if is_long_distant:
            call_params = self.calculate_basic_cost_long_distant(call_start_time, call_end_time, is_off_peak)
        else:
            call_params = self.calculate_basic_cost_short_distant(call_start_time, call_end_time, is_off_peak)
        
        # Display everything
        self.presentation(call_params)

        return call_params


    
    def calculate_basic_cost_long_distant(self, call_start_time, call_end_time, is_off_peak):
        '''Calculate the basic_call_cost, without VAT or discount'''
        call_duration = self.calculate_call_duration(call_start_time, call_end_time)

        basic_cost = Call.MINIMUM_COST_FAR + (Call.PER_SECOND_COST_FAR * call_duration)

        discount = 0.00 # Default value of discouunt
        if is_off_peak:
            discount = Call.OFF_PEAK_DISCOUNT_FAR * basic_cost

        discounted_cost = basic_cost - discount
        
        return basic_cost, discount, discounted_cost
    
    def calculate_basic_cost_short_distant(self, call_start_time, call_end_time, is_off_peak):
        '''Calculate the basic_call_cost, without VAT'''
        call_duration = self.calculate_call_duration(call_start_time, call_end_time)

        basic_cost = Call.MINIMUM_COST_NEAR + (Call.PER_SECOND_COST_NEAR * call_duration)

        discount = 0.00 # Default value of discouunt
        if is_off_peak:
            discount = Call.OFF_PEAK_DISCOUNT_NEAR * basic_cost

        discounted_cost = basic_cost - discount
        return basic_cost, discount, discounted_cost
    
    def presentation(self, call_params):
        '''Display e'erthing to user'''
        pass

# lo_call = Call()
# lo_call.calculate_cost()