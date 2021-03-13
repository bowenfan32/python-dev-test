"""
Write a short docstring for the function below,
so that other people reading this code can quickly understand what this function does.

You may also rename the functions if you can think of clearer names.
"""


def check_time(start_time, end_time, value):
    """
    Set to a specific value if it falls between start and end time, otherwise return 0.0

    @param start_time: start time string
    @param end_time: end time string
    @param value: value to set to
    @return: returns a inner function
    """

    def compare_time(time):
        if start_time <= time <= end_time:
            y = value
        else:
            y = 0.0
        return y

    return compare_time
