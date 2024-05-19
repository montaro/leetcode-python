class Solution:
    def isHappy(self, n: int) -> bool:
        new_n = n
        squares_set = set()
        while True:
            n_str = str(new_n)
            n_squares = [int(x) ** 2 for x in n_str]
            print(f"Squares of {n_str} is {n_squares}")
            new_n = sum(n_squares)
            print(f"Sum of squares: {new_n}")
            if new_n == 1:
                print(f"Happy Number!! {n}")
                print("-------------------------------------------------------")
                return True
            else:
                if new_n in squares_set:
                    print(f"Got into an endless loop, {n} is not a Happy Number!")
                    print("-------------------------------------------------------")
                    return False
                else:
                    squares_set.add(new_n)


if __name__ == "__main__":
    sol = Solution()
    sol.isHappy(n=19)
    sol.isHappy(n=2)
    print(sol.isHappy(n=3))
    print(sol.isHappy(n=4))
    print(sol.isHappy(n=5))
    print(sol.isHappy(n=6))
    print(sol.isHappy(n=7))
    print(sol.isHappy(n=8))
    print(sol.isHappy(n=9))
