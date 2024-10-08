import pytest
from src.algorithms import Algorithms

text = """Dette er en tekst som er beregnet for å søke gjennom med et gitt mønster. Mønsteret kommer under et sted. """
tests = [
    (text, "Dette", 0),
    (text, "bereg", 25),
    (text, "mønst", 65),
    (text, "et st", 97),
    (text, "not_in_text", -1)
]

dynamic_programming_test = [
    ("babbabab", "bbabbaaab", 7),
    ("AGGTAB", "GXTXAYB", 4),
    ("ABC", "AC", 2),
    ("ABC", "DEF", 0),
    ("XMJYAUZ", "MZJAWXU", 4),
    ("AAB", "ABA", 2),
    ("", "", 0),
    ("A", "", 0),
    ("", "B", 0)
]

@pytest.mark.parametrize("text, pattern, expected", tests)
def test_boyer_moore_algorithm(text, pattern, expected):
    index, comparisons = Algorithms.boyer_moore_algorithm(text, pattern)

    avg_comparisons_per_char = Algorithms.average_comparisons_per_char(comparisons, len(text))

    print(f"Test case: text='{text}', pattern='{pattern}' -> ")
    print(f"Expected index: {expected}, Found index: {index}")
    print(f"Total comparisons: {comparisons}")
    print(f"Average comparisons per character: {avg_comparisons_per_char:.2f}\n")

    assert index == expected, f"Test failed: {text} vs {pattern}. Expected: {expected}, got: {index}"

@pytest.mark.parametrize("input, expected", [
    ("aabaaa", [0,1,0,1,2,2])
])
def test_KPM_failure(input, expected):
    failure = Algorithms.KMP_failure(input)
    print(failure)
    assert failure == expected

@pytest.mark.parametrize("text, pattern, expected", tests)
def test_KMP_algorithm(text, pattern, expected):
    index, comparisons = Algorithms.KMP_algorithm(text, pattern)

    avg_comparisons_per_char = Algorithms.average_comparisons_per_char(comparisons, len(text))

    print(f"Test case: text='{text}', pattern='{pattern}' -> ")
    print(f"Expected index: {expected}, Found index: {index}")
    print(f"Total comparisons: {comparisons}")
    print(f"Average comparisons per character: {avg_comparisons_per_char:.2f}\n")

    assert index == expected, f"Test failed: {text} vs {pattern}. Expected: {expected}, got: {index}"

@pytest.mark.parametrize("X, Y, expected", dynamic_programming_test)
def test_longest_common_sequence(X, Y, expected):
    length = Algorithms.longest_common_subsequence(X, Y)
    assert length == expected


@pytest.mark.parametrize("X, Y, expected", dynamic_programming_test)
def test_longest_common_sequence_dynamic(X, Y, expected):
    mem = Algorithms.longest_common_subsequence_dynamic(X, Y)
    assert mem == expected