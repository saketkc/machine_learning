import orngIO
import sys
print sys.argv[1]
data = orngIO.loadARFF(sys.argv[1])
data.save(sys.argv[1].split('.')[0]+".tab")

