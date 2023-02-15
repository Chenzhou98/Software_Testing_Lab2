import random
from Question3_programs import Membership_unsorted
import Mutation_1
import Mutation_2
import Mutation_3
import Mutation_4
import Mutation_5
import Mutation_6

def RandomArrayGenerator(length=6, low=0, high=100):
    array = []
    #random.seed(10)
    for i in range(length):
        element = random.randint(low, high)
        array.append(element)
    return array


def Test_Random():
    counter = 1
    errorfound = 0
    while errorfound != 1:
        input_array = RandomArrayGenerator()
        key = input_array[random.randint(0, len(input_array))]

        correct_result = Membership_unsorted(input_array, key)
        mutated_result = Mutation_2.Membership_unsorted(input_array, key)  # to be modified
        print (input_array,key, correct_result, mutated_result)
        if correct_result == mutated_result:
            counter = counter + 1
        else:
            print("Testing method: Random Testing",)
            print("Correct result is ", correct_result, "whereas mutated result is ", mutated_result)
            print("Mutaion error is found in loop ", counter)
            errorfound = 1
    return

def Test_Pairwise():
    counter = 1
    errorfound = 0
    input = pairwise() # generate pairwise array
    print(input)
    while errorfound != 1:
        for elements in input: # choose one combination from pairwise array
            key = elements[random.randint(0, len(elements)-1)]
            #print(key, elements)
            correct_result = Membership_unsorted(elements, key)
            mutated_result = Mutation_2.Membership_unsorted(elements, key)  # to be modified
            #print (input, key, correct_result, mutated_result)
            if correct_result == mutated_result:
                counter = counter + 1
            else:
                print("Testing method: Pairwise Testing",)
                print("Correct result is ", correct_result, "whereas mutated result is ", mutated_result)
                print("Mutaion error is found in loop ", counter)
                errorfound = 1
                break
    return

def pairwise(length=6, low= 1, high=100):
    defaults = []
    typicals = []
    testCases = []
    """
    # generate M=length: M dimension. n=2: pairwise test case
    # For example: a length=3 dimension pairwise testing
    # Typical1 = { Sat, Sun }
    # Typical2 = { A, B }
    # Typical3 = { 1, 2 }
    # have 
    # defaults = ["Sat","A","1"]
    # typicals = ["Sun","B","2"]
    # which have testcase
    # (def1, def2, def3), [0-wise]
    # (Sun, def2, def3), (def1, B, def3), (def1, def2, 2), [1-wise]
    # (Sun, B, def3), (Sun, def2, 2), (def1, B, 2) [2-wise]
    """
    # Separate typical and default into 2 arrays
    while len(defaults) < length:
        defaults.append(random.randint(low, high))
        typicals.append(random.randint(low, high))
    #print(defaults, typicals)
    #defaults = ["Sat","A","1"]
    #typicals = ["Sun","B","2"]

    #0-wise
    testCases.append(defaults)
    #1-wise
    for element in range(length):
        newTestCase = defaults[0:element] + typicals[element:element + 1] + defaults[element + 1:]
        testCases.append(newTestCase)
    #2-wise
    for element1 in range(length):
        for element2 in range(element1 + 1, length):
            newTestCase = defaults[0:element1] + typicals[element1:element1 + 1] + \
                          defaults[element1 + 1:element2] + typicals[element2:element2 + 1] \
                          + defaults[element2 + 1:]
            testCases.append(newTestCase)
    return testCases # testcase include 0, 1, 2 wise

if __name__ == "__main__":

    Test_Pairwise()
