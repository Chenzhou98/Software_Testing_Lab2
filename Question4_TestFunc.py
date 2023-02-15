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


import copy
import itertools
from sys import stdout
from loguru import logger
def parewise(option):
    cp = []  #original combination
    s = []  #seperate
    for x in eval('itertools.product' + str(tuple(option))):
        cp.append(x)
        print(cp)
        s.append([i for i in itertools.combinations(x, 2)])
    logger.info('original combination' % len(cp))
    del_row = []
    s2 = copy.deepcopy(s)
    for i in range(len(s)):
        t = 0
        for j in range(len(s[i])):
            flag = False
            for i2 in [x for x in range(len(s2)) if s2[x] != s[i]]:
                if s[i][j] == s2[i2][j]:
                    t = t + 1
                    flag = True
                    break
            if not flag:
                break
        if t == len(s[i]):
            del_row.append(i)
            s2.remove(s[i])
    res = [cp[i] for i in range(len(cp)) if i not in del_row]
    logger.info('pairwise combination:%s' % len(res))
    return res



def Test():
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
            print("Testing method:",)
            print("Correct result is ", correct_result, "whereas mutated result is ", mutated_result)
            print("Mutaion error is found in loop ", counter)
            errorfound = 1
    return

if __name__ == "__main__":

    Test()

    """
    pl = [['M', 'O', 'P'], ['W', 'L', 'I'], ['C', 'E',"O"]]
    a = parewise(pl)
    print()
    for i in a:
        print(i)
    """
