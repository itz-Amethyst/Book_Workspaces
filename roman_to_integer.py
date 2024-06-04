class Solution(object):

    roman_integers = {"I": 1 , "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        answer = 0

        for i in s:
            answer = self.roman_integers.get(i,0) + answer


        return answer



input = list(map(str, input("Enter the number: ").strip().upper()))
a = Solution()

print(a.romanToInt(input))