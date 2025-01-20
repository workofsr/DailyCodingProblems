# Given a list of numbers and a number k, return whether any two numbers
# from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def sol(original_list: list, value: int):
    """
    Finding the equivalent of k.
    :param value: equivalence
    :type original_list: list of data
    """
    print(True in [True if i + j == value else False for i in original_list for j in original_list if not i == j])


if __name__ == '__main__':
    data = [10, 15, 3, 7]
    k = 17
    sol(data, k)
