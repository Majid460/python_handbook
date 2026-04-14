# If we are computing repeated work we can store it for future computation this is dynamic programming
# Solve a problem by breaking it into smaller subproblems and storing results to avoid recomputation
# Memoization


class Fib:
    def __init__(self):
        self.dp = {}

    def calculate_fib(self, n):
        if n in self.dp:
            print("here", self.dp[n])
            return self.dp[n]
        if n <= 1:
            return n
        res = self.calculate_fib(n - 1) + self.calculate_fib(n - 2)
        self.dp[n] = res
        return res


if __name__ == "__main__":
    fib = Fib()
    print(fib.calculate_fib(5))
    print(fib.calculate_fib(6))
