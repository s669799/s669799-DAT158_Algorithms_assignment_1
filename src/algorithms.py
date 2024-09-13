class Algorithms:

    @staticmethod
    def boyer_moore_algorithm(t:str, p:str):
        n = len(t)
        m = len(p)

        def compute_last(p):
            last = {}
            for k in range(m):
                last[p[k]] = k
            return last

        last = compute_last(p)

        i = j = m - 1
        comparisons:int = 0
        while i < n:
            comparisons += 1
            if t[i] == p[j]:
                if j == 0:
                    return i, comparisons
                else:
                    i -= 1
                    j -= 1
            else:
                i = i + m - min(j, 1 + last.get(t[i], - 1))
                j = m - 1

        return -1, comparisons


    @staticmethod
    def KMP_algorithm(t:str, p:str):

        f = Algorithms.KMP_failure(p)
        i = 0
        j = 0
        n = len(t)
        m = len(p)
        comparisons: int = 0

        while i < n:
            comparisons += 1
            if p[j] == t[i]:
                if j == m - 1:
                    return (i - m + 1), comparisons
                i += 1
                j += 1
            elif j > 0:
                j = f[j - 1]
            else:
                i += 1

        return -1, comparisons

    @staticmethod
    def KMP_failure(p:str):
        i = 1
        j = 0
        m = len(p)
        f = [0] * m
        while i < m:
            if p[j] == p[i]:
                j += 1
                f[i] = j
                i += 1
            elif j > 0:
                j = f[j - 1]
            else:
                f[i] = 0
                i += 1
        return f


    @staticmethod
    def average_comparisons_per_char(comparisons, text_length) -> float:
        return comparisons / text_length if text_length != 0 else 0


    def longest_common_subsequence(X:str, Y:str):
        return Algorithms.lcs_recursive(X, Y, len(X), len(Y))

    def lcs_recursive(X:str, Y:str, n, m):

        if n == 0 or m == 0:
            return 0

        if X[n - 1] == Y[m - 1]:
            return Algorithms.lcs_recursive(X, Y, n - 1, m - 1) + 1
        elif X[n - 1] != Y[m - 1]:
            return max (Algorithms.lcs_recursive(X, Y, n - 1, m),
                        Algorithms.lcs_recursive(X, Y, n, m - 1))

def main():
    test_cases = [
        ("AGGTAB", "GXTXAYB"),
        ("ABC", "AC"),
        ("ABC", "DEF"),
        ("XMJYAUZ", "MZJAWXU"),
        ("AAB", "ABA"),
        ("", ""),
        ("A", ""),
        ("", "B"),
        ("babbaba" , "bbabbaaab"),
        ("abcdefghijklm", "nopqrstuvwxyz")
    ]
    for X, Y in test_cases:
        lcs = Algorithms.longest_common_subsequence(X, Y)
        print(f"LCS of '{X}' and '{Y}' is '{lcs}'")


if __name__ == "__main__":
    main()