from sys import argv

def dummy_worker(loop_length):
    t = 1
    for i in range(loop_length):
        for j in range(loop_length):
            t = i * j
            print(t)
    return t


if __name__ == "__main__":
    dummy_worker(int(argv[1]))