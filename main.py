
from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search


def print_result(method_name: str, target: int, index: int) -> None:
    if index != -1:
        print(f"{method_name}: {target} found at index {index}")
    else:
        print(f"{method_name}: {target} not found")


def part1_small_tests() -> None:
    # Small test list
    arr = [3, 5, 8, 12, 14, 18, 21]
    arr.sort()  # required for binary search 

    target_present = 12
    target_absent = 9

    for target in (target_present, target_absent):
        print(f"\n--- Part 1 tests for target = {target} ---")

        r = recursive_binary_search(arr, target, 0, len(arr) - 1)
        print_result("Recursive Binary Search", target, r)

        i = iterative_binary_search(arr, target)
        print_result("Iterative Binary Search", target, i)

        s = sequential_search(arr, target)
        print_result("Sequential Search", target, s)


if __name__ == "__main__":
    part1_small_tests()

    """Part 2"""
    import random


def part2_random_tests() -> None:
    print("\n================ Part 2: Randomized Testing ================\n")

    # Random list example from instructions
    arr = [random.randint(1, 100) for _ in range(20)]

    # 50% chance to choose a target that will fail
    target = random.choice(arr) if random.random() < 0.5 else 999

    print("Original array (unsorted):", arr)
    print("Target:", target)

    # Sort for binary search (required) 
    arr_sorted = sorted(arr)
    print("Sorted array:", arr_sorted)

    # Run all searches
    r = recursive_binary_search(arr_sorted, target, 0, len(arr_sorted) - 1)
    i = iterative_binary_search(arr_sorted, target)
    s = sequential_search(arr_sorted, target)  

    print_result("Recursive Binary Search", target, r)
    print_result("Iterative Binary Search", target, i)
    print_result("Sequential Search", target, s)

    # Interpretation: successful vs unsuccessful
    print("\nInterpretation:")
    print("- If the result is -1, the target was not found (unsuccessful search).")
    print("- Otherwise, the returned value is the index where the target was found (successful search).")


    import time


def time_call_microseconds(fn, *args) -> float:
    """Return execution time for fn(*args) in microseconds."""
    start = time.perf_counter()
    fn(*args)
    end = time.perf_counter()
    return (end - start) * 1_000_000  # seconds -> microseconds 

"""Part 3"""
def part3_runtime_measurement() -> None:
    print("\n================ Part 3: Runtime Measurement ================\n")

    data_sizes = [5000, 50000, 100000, 150000, 1000000]  # required 
    trials = 10  # required averaging approach 

    results = []  # list of (N, avg_rbs, avg_ibs, avg_seq)

    for N in data_sizes:
        sum_rbs = 0.0
        sum_ibs = 0.0
        sum_seq = 0.0

        for _ in range(trials):  # underscore = unused loop variable
            # Required setup: sorted array of N random ints, random target 
            arr = sorted([random.randint(1, 1_000_000) for _ in range(N)])
            target = random.randint(1, 1_000_000)

            sum_rbs += time_call_microseconds(recursive_binary_search, arr, target, 0, len(arr) - 1)
            sum_ibs += time_call_microseconds(iterative_binary_search, arr, target)
            sum_seq += time_call_microseconds(sequential_search, arr, target)

        avg_rbs = sum_rbs / trials
        avg_ibs = sum_ibs / trials
        avg_seq = sum_seq / trials

        results.append((N, avg_rbs, avg_ibs, avg_seq))

        print(f"N = {N}")
        print(f"Average Recursive Binary Search time: {avg_rbs:10.2f} 탎")
        print(f"Average Iterative Binary Search time: {avg_ibs:10.2f} 탎")
        print(f"Average Sequential Search time:       {avg_seq:10.2f} 탎\n")

    # Final results table printout
    print("Final Results Table (copy into report):")
    print(f"{'Size of Data (N)':>15} | {'Recursive BS (탎)':>18} | {'Iterative BS (탎)':>18} | {'Sequential (탎)':>16}")
    print("-" * 76)
    for N, rbs, ibs, seq in results:
        print(f"{N:15d} | {rbs:18.2f} | {ibs:18.2f} | {seq:16.2f}")


