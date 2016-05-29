"""Hamming distance measure"""

from py_stringmatching import utils
from py_stringmatching.similarity_measure.sequence_similarity_measure import \
                                                    SequenceSimilarityMeasure


class HammingDistance(SequenceSimilarityMeasure):
    def __init__(self):
        super(HammingDistance, self).__init__()

    def get_raw_score(self, string1, string2):
        """
        Computes the Hamming distance between two strings.

        The Hamming distance between two strings of equal length is the number of positions at which the corresponding
        symbols are different. In another way, it measures the minimum number of substitutions required to change
        one string into the other, or the minimum number of errors that could have transformed one string into the other.

        Args:
            string1,string2 (str): Input strings

        Returns:
            Hamming distance (int)

        Raises:
            TypeError : If the inputs are not strings or if one of the inputs is None.
            ValueError : If the input strings are not of same length

        Examples:
            >>> hd = HammingDistance()
            >>> hd.get_raw_score('', '')
            0
            >>> hd.get_raw_score('alex', 'john')
            4
            >>> hd.get_raw_score(' ', 'a')
            0
            >>> hd.get_raw_score('JOHN', 'john')
            4
        """
        # input validations
        utils.sim_check_for_none(string1, string2)
        utils.tok_check_for_string_input(string1, string2)

        # for Hamming Distance string length should be same
        utils.sim_check_for_same_len(string1, string2)

        # sum all the mismatch characters at the corresponding index of
        # input strings
        return sum(bool(ord(c1) - ord(c2)) for c1, c2 in zip(string1, string2))
