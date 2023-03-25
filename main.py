# python3
# Nikita Ščipanovs 221RDB061

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    data = sorted([(j, t) for j, t in enumerate(data)], key=lambda x: x[1])

    thread_times = [0] * n

    for j, t in data:
        thread = min(range(n), key=lambda i: thread_times[i])

        start_time = thread_times[thread]
        output.append((thread, start_time))

        thread_times[thread] = start_time + t

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line

    for thread, start_time in result:
        print(f"{thread} {start_time}")



if __name__ == "__main__":
    main()
