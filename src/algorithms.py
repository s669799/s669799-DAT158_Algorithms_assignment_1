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