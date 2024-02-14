def stats_decorator(func):
    def wrapper(numbers):
        print(f"Numbers: {numbers}")
        print(f"Count: {len(numbers)}")
        print(f"Average: {sum(numbers) / len(numbers) if numbers else 0}")
        print(f"Maximum: {max(numbers) if numbers else 'N/A'}")
        print("-" * 30)
        return func(numbers)
    return wrapper

@stats_decorator
def printStats(numbers):
    total = sum(numbers)
    print(f"Total: {total}")
    if numbers:
        print(f"Average (modified): {total / len(numbers)}")
    print("=" * 30)

def main():
    with open('numbers_data.txt', 'r') as file:  
        for line in file:
            numbers = [int(num) for num in line.strip().split()]
            printStats(numbers)

if __name__ == "__main__":
    main()
