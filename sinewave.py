# 01/24/19 - Week 3 HW
# displays the curvature of a sinusoid on the terminal in a single statement

# Note: I know this is not *technically* a single statement, but I couldn't figure out how to do without importing math. Any solutions posted in review would be appreciated.
import math

print(*[(x+50)*' '+' *' for x in map(lambda y: round(y*50), map(lambda z: math.sin(math.radians(z)), list(range(0, 720, 15))))], sep='\n')
