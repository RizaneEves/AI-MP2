import Utilities
import time
import numpy as np

file = open("num_attempts.txt",'w')

def recursiveBacktracking(assignment, domain, sources):
    index = Utilities.getUnassignedIndexNearColored(assignment)
    #print(index)
    if(index is None):
        if(Utilities.isAssignmentValid(assignment, sources)):
            file.close()
            return assignment
        return None

    for value in domain:
        if Utilities.isValueConsistent(index, value, assignment, sources):
            file.write('attempt\n')
            #print("Assigning " + value + " to " + "(" + str(index[0]) + ", " + str(index[1]) + ")\n")
            assignment[index[0]][index[1]] = value
            #print(np.array(assignment))
            result = recursiveBacktracking(assignment, domain, sources)
            if result is not None:
                return result
            assignment[index[0]][index[1]] = "_"
    return None

def recursiveBacktracking_mcv(assignment, domain, sources):
    indexes = Utilities.getAllUnassignedIndexNearColored(assignment)
    index = Utilities.getMostConstrainedVariable(indexes,domain,assignment,sources)
    #index = Utilities.getUnassignedIndexNearColored(assignment)
    #print(index)
    if(index is None):
        if(Utilities.isAssignmentValid(assignment, sources)):
            file.close()
            return assignment
        return None

    for value in domain:
        if Utilities.isValueConsistent(index, value, assignment, sources):
            #print("Assigning " + value + " to " + "(" + str(index[0]) + ", " + str(index[1]) + ")\n")
            file.write('attempt\n')
            assignment[index[0]][index[1]] = value
            #print(np.array(assignment))
            result = recursiveBacktracking_mcv(assignment, domain, sources)
            if result is not None:
                return result
            assignment[index[0]][index[1]] = "_"

    return None

startTime = time.time()

array = Utilities.parseArray("input991.txt")
domain = Utilities.getDomain(array)
sources = Utilities.getSources(array)

result = recursiveBacktracking_mcv(array, domain, sources)
print(np.array(result))
Utilities.writeArrayToFile(result, "output991.txt")

endTime = time.time()
print("Search took " + str(endTime - startTime) + " seconds.")
file = open('num_attempts.txt','r')
print("Values attempted: " + str(len(file.readlines())))
file.close()
