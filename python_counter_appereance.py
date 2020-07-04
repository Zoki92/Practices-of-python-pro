"""
Just few algorithms for counting appeareance of
numbers in a range or list
"""


from collections import Counter
from collections import defaultdict


def get_number_with_highest_count(counts):
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent_dict(numbers):
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return get_number_with_highest_count(counts)


def most_frequent_defaultdict(numbers):
    counts = defaultdict(int)
    for number in numbers:
        counts[number] += 1
    return get_number_with_highest_count(counts)


def most_frequent(numbers):
    """
    This one uses the Counter from collections module
    acts like the dict of counts
    """
    counts = Counter(numbers)
    return get_number_with_highest_count(counts)


def get_number_with_highest_count_refactored(counts):
    """refactoring the function from above
    When going through numbers in count uses counts[number]
    as the comparison values and returns the key
    """
    return max(
        counts,
        key=lambda number: counts[number],
    )
