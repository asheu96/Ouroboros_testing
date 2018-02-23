try:
    import numpy as np
except ImportError:
    print('Could not import numpy')

try:
    import logging
except ImportError:
    print('Could not import logging')

class List:

    def __init__(self, my_list, sum = None, minMax = None, maxDiff = None):

        logging.basicConfig(filename='listLog.txt', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S')
        with open('listLog.txt', 'w'):
            pass
        
        self.list = my_list
        logging.info('Set object list to given argument')

        self.get_sum()
        self.min_max()
        self.max_diff()

        logging.info('Finished assigning attributes')
        
    def get_sum(self):

        """
        :param my_list: list containing real numbers to be summed
        :raises: TypeError if list cannot be summed
        :raises: ValueError if no elements in given list
        :returns: sum of all elements in the list
        """

        try:
            np.sum(self.list)
        except TypeError:
            print('Input list should be numbers')
            logging.debug('Given list does not contain summable elements')
            return None

        if len(self.list) == 0:
            logging.warning('List contains no elements')
            return None
            
        sum = 0
        for elem in self.list:
            sum += elem
        self.sum = sum
        logging.info('Elements have been successfully summed')
        return self.sum

    def min_max(self):

        """ Function returns the max and min value of the input list
        :param my_list: a list of numbers
        :returns max_min: a tuple of the min and max values of given list
        :raises TypeError: can only input a list of numbers
        :raises ValueError: can not input a list with complex numbers
        """
        if np.iscomplexobj(self.list):
            #raise ValueError('Given list contains imaginary numbers')
            logging.warning('Given list contains imaginary numbers')
            return None
        
        try:
            np.max(self.list)
        except ValueError:
            logging.debug('List contains values of incorrect value')
        except TypeError:
            logging.debug('List contains values of incorrect type')
            return None
        
        if len(self.list) <= 1:
            #raise ValueError('Too little elements to find min and max')
            logging.debug('Too little elements to find min and max')
            return None

        self.minMax = ((np.max(self.list), np.min(self.list)))
        logging.info('Element min and max have been successfully found')
        return self.minMax

    def max_diff(self):

        """Function will return maximum difference between adjacent numbers.
        Function takes in the inputted list of values, splits it into two arrays to calculate the difference between
        adjacent values, takes the absolute values of the differences to disregard positioning, and then outputs the
        maximum value.

        :param input_list: List of numbers
        :return: Maximum difference
        :raises ImportError: Check if numpy is installed or virtual env is established
        :raises TypeError: Input not given as a list of values
        :raises ValueError: Can occur when only 1 number is given in the list
        """

        # Function
        if any(self.list) < 0:
            logging.warning('Negative values present in list')
        
        if (len(self.list) <= 1):
            logging.warning('Not enough elements in list')
            return None

        try:
            np.diff(self.list)
        except ValueError:
            logging.error('ValueError, add more numbers to list')
            print('Add more numbers to list')
            return None
                    
        except TypeError:
            print('Input list should be numbers')
            logging.debug('Given list does not contain numbers')
            return None
       
        input_list = np.array(self.list)
        diffs = abs(np.diff(input_list))
        self.maxDiff = max(diffs)
        logging.info('Max difference successfully found')
        return self.maxDiff
        

