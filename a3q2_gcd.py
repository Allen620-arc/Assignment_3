"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""

import a3q2_provided

test_suite = [

    {   "inputs"  : 0.5,
        "outputs" : 0.7071078,
        "reason"  : "The square root of 0.5 is 0.7071078." },

    {   "inputs"  : 9,
        "outputs" : 3,
        "reason"  : "The square root of 16 is 4." },

    {   "inputs"  : 0,
        "outputs" : 0,
        "reason"  : "The square root of 0 is 0." },

    {   "inputs"  : 1,
        "outputs" : 1,
        "reason"  : "The square root of 1 is 1." }
]

for test in test_suite:
    inputs = test["inputs"]
    result = a3q2_provided.newtonraphson(inputs)
    if result != test["outputs"]:
        print("Testing fault: selection_sort() returned", result, "on inputs", inputs, "(",test["reason"],")")