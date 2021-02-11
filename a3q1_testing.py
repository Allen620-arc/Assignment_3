"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""

import a3q1_provided

test_suite = [

    { "inputs"  : [1, 2, 3, 4],
      "outputs" : [1, 2, 3, 4],
      "reason"  : "Returns a copy of the given list of data" },
]

for test in test_suite:
    inputs = test["inputs"]
    result = a3q1_provided.copy2(inputs)
    if result != test["outputs"]:
        print("Testing fault: selection_sort() returned", result, "on inputs", inputs, "(",test["reason"],")")