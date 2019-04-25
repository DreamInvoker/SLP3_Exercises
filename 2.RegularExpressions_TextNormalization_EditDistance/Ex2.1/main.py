import re

str1 = 'a word is the sequence of characters.'

str2 = 'Bob is finding a big b2 B ib job'

str3 = 'b babc bba bab abab baba babab'

# 1.the set of all alphabetic strings;
pattern1 = re.compile(r'[a-zA-Z]+')
# expect to output: ['a', 'word', 'is', 'the', 'sequence', 'of', 'characters']
print(pattern1.findall(str1))

# 2.the set of all lower case alphabetic strings ending in a b;
pattern2 = re.compile(r'[a-z]*b\b')
# expect to output: ['ob', 'ib', 'job']
print(pattern2.findall(str2))

# 3.the set of all strings from the alphabetic a,b such that
# each a is immediately preceded by and immediately followed by a b
pattern3 = re.compile(r'\bb+(b|ab)*\b')
print(pattern3.findall(str3))



