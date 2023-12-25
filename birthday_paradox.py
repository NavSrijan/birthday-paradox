import random
import multiprocessing as mp
import matplotlib.pyplot as plt

def get_sample(n):
    return [random.randint(1, 366) for _ in range(n)]

def check_pair(sample):
    sample_set = set(sample)
    x = len(sample)
    y = len(sample_set)
    if x==y:
        return False #Pair doesn't exist
    else:
        return True  #Pair does exist

def run_test(n, result_list, test_cases = 1000):
    count = 0
    for i in range(1, test_cases+1):
        sample = get_sample(n)
        bul = check_pair(sample)
        if bul is True:
            count+=1
    percent = (count*100)/test_cases
    result_list.append(percent)

def run_multiple_test(n, test_cases = 100000):
    manager = mp.Manager()
    result_list = manager.list()
    if test_cases<=100000:
        chunk_size = 1000
    else:
        chunk_size = test_cases/100

    processes = []
    instances = int(test_cases/chunk_size)
    for i in range(instances):
        p = mp.Process(target=run_test, args=(n,result_list))
        processes.append(p)
        p.start()

    for i in processes:
        i.join()
    final_result = sum(result_list)/len(result_list)
    print(f"Final percentage for {n}: {final_result}")
    return final_result

def get_graph(max_limit):
    results = {}
    for n in range(1, max_limit+1):
        res = run_multiple_test(n, 100000)
        results[n]=res

    plt.plot(results.keys(), results.values(), marker='o')
    plt.title('Percentage vs. n')
    plt.xlabel('n')
    plt.ylabel('Percentage')
    plt.grid(True)
    plt.show()



#run_multiple_test(3, 1000000)
get_graph(100)




