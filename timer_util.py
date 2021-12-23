"""! @brief A context manager that times our functions for us."""
##
# @section description_timer_util Description
# Use this as a context manager to time your functions.
# Not as functional as the timeit module but very practical
#
##
# @file timer_util.py
#
# @section libraries_timer_util Libraries/Modules
# - contextlib
# - time
#
# @section author_timer_util Author(s)
# - Created by Stephen Tellis.

# Import python libs
from time import perf_counter
from contextlib import contextmanager

# Generate a context manager for benchmarking
@contextmanager
def timer():
    start = perf_counter()
    yield
    end = perf_counter()
    rospy.logerr(f"Elapsed Time: {(end - start)}s")
