# This script creates a class to analyze the runtime metrics of the module when it's executed

class RuntimeMetric:
    def __init__(self, size: int, time_ns: float):
        """
        Holds data to determine Big-O runtime metrics
        size: size of the problem
        time_ns: duration of the solution
        """
        self.size = size
        self.time = time_ns

    def get_runtime(self) -> float:
        """
        Retrieves the time it took to solve the problem
        return: the time measured in nanoseconds
        """
        return self.time

    def get_size(self) -> int:
        """
        Retrieves the size of the problem
        return: a size that is determined by the way the problem is stated
        """
        return self.size
