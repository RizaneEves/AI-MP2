import Utilities
import numpy as np

def recursiveBacktracking(assignment, domain, sources):
    index = Utilities.getUnassignedIndexNearColored(assignment)
    #print(index)
    if(index is None):
        if(Utilities.isAssignmentValid(assignment, sources)):
            return assignment
        return None

    for value in domain:
        if Utilities.isValueConsistent(index, value, assignment, sources):
            #print("Assigning " + value + " to " + "(" + str(index[0]) + ", " + str(index[1]) + ")\n")
            assignment[index[0]][index[1]] = value
            print(np.array(assignment))
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
            return assignment
        return None

    for value in domain:
        if Utilities.isValueConsistent(index, value, assignment, sources):
            #print("Assigning " + value + " to " + "(" + str(index[0]) + ", " + str(index[1]) + ")\n")
            assignment[index[0]][index[1]] = value
            print(np.array(assignment))
            result = recursiveBacktracking_mcv(assignment, domain, sources)
            if result is not None:
                return result
            assignment[index[0]][index[1]] = "_"

    return None

array = Utilities.parseArray("input10.txt")
domain = Utilities.getDomain(array)
sources = Utilities.getSources(array)

result = recursiveBacktracking_mcv(array, domain, sources)
print(np.array(result))
Utilities.writeArrayToFile(result, "output10.txt")
