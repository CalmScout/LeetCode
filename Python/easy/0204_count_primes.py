"""
Count the number of prime numbers less than a non-negative number, n.
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        sieve = [False] * 2 + [True] * (n-2)
        idx = 2
        while idx * idx < n:
            if sieve[idx]:
                sieve[idx*idx:n:idx] = [False] * len(sieve[idx*idx:n:idx])
            idx += 1
        return sum(sieve)


if __name__ == "__main__":
    n = 10
    out = 4
    actual = Solution().countPrimes(n)
    assert actual == out, (actual, out)

    n = 4
    out = 2
    actual = Solution().countPrimes(n)
    assert actual == out, (actual, out)
