# driver.py
# The driver file which contains the statements creating
# the main flow of execution.

import modA
import modB

value1 = int( raw_input( "Enter value.txt one: " ) )
value2 = int( raw_input( "Enter value.txt two: " ) )
resultA = modA.funcA( value1, value2 )
resultB = modB.funcB( resultA )
print "Results = ", resultA, resultB