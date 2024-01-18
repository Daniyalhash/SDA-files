from abc import ABC, abstractmethod

# Strategy Interface
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Concrete Strategies
class BubbleSort(SortingStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort")
        return sorted(data)

class QuickSort(SortingStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort")
        return sorted(data, key=lambda x: x)

# Context
class SortingContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def perform_sort(self, data):
        return self.strategy.sort(data)

# Client Code
if __name__ == "__main__":
    data_to_sort = [5, 2, 8, 1, 7]

    # Using Bubble Sort
    bubble_sort_strategy = BubbleSort()
    context = SortingContext(bubble_sort_strategy)
    result = context.perform_sort(data_to_sort)
    print("Sorted Data:", result)
    print("")

    # Switching to Quick Sort dynamically
    quick_sort_strategy = QuickSort()
    context.set_strategy(quick_sort_strategy)
    result = context.perform_sort(data_to_sort)
    print("Sorted Data:", result)
