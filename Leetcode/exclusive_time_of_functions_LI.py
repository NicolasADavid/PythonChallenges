"""

LinkedIn 2025

Given a list of strings denoting function name, START or END marker, and timestamp. Calls can be nested and one function can call child functions. 
For example:

"abc,START,100"
"def,START,150", 
"def,END,180", 
"abc,END,200"
Inclusive time is defined as all the time spent on a particular function, including time spent on its child calls. 
Exclusive time is defined as the time spent on a particular function only, excluding time spent on its child calls.
In the above example, inclusive time for function "abc" is 200-100=100, while exclusive time for function "abc" is (200-100) - (180-150) = 70

Given such list of strings, figure out the inclusive and exclusive time for any given function call.  

Note that the calls can span multiple levels and nested. 

"abc,START,100",  
"def,START,150", 
"hij,START,170", 
"hij,END,200", 
"def,END,220", 
"job4,START,230", 
"job4,END,250", 
"abc,END,300"

Note that you can assume the inputs are well formed, and there are no out-of-order calls. For example, "abc, START,100" will always appear before "abc,END,300".

For"abc", it should output:
 inclusive time=200
 exclusive time=110
"""

"""

Iterate through function events
When target function start is found, record start of target function, continue
If child function starts, record start
continue until child (first gen) end is found, record end, track count of (end - start)
continue until target function end is found
Return (inclusive time, exclusive time)

"""

from typing import List

def get_execution_time(function_events: List[str], target_function_name: str) -> List[int]:

    inclusive_time = 0
    exclusive_time = 0
    child_execution_time = 0

    end_marker = "END"
    # start_marker = "START"

    inclusive_start = None
    inclusive_end = None

    child_name = None
    child_start = None
    child_end = None

    execution_stack = []
    running_functions = set()

    for function_event in function_events:
        func_name, marker, time = function_event.split(",")

        # Execution order checking
        if marker == end_marker:
            if execution_stack[-1] != func_name:
                #Exception
                pass
            else:
                execution_stack.pop()
                running_functions.remove(func_name)
        else:
            if func_name in running_functions:
                # Exception
                pass

            running_functions.add(func_name)
            execution_stack.append(func_name)
            

        if func_name == target_function_name:
            if not inclusive_start:
                inclusive_start = time
            else:
                inclusive_end = time
                break
        else:
            if inclusive_start:
                if child_name is None:
                    child_name = func_name
                    child_start = int(time)
                else:
                    if func_name == child_name:
                        child_end = int(time)
                        child_execution_time += child_end - child_start
                        child_name = None

    inclusive_time = inclusive_end - inclusive_start
    
    exclusive_time = inclusive_time - child_execution_time

    return [inclusive_time, exclusive_time]
