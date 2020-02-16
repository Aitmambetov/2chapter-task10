"""
You are given a string.
In the first line, print the third character of this string.
In the second line, print the second to last character of this string.
In the third line, print the first five characters of this string.
In the fourth line, print all but the last two characters of this string.
In the fifth line, print all the characters of this string with even indices
(На английском языке что бы Вы научились понимать remember indexing starts at 0, so the characters are displayed starting with
the first).
In the sixth line, print all the characters of this string with odd indices (На английском языке что бы Вы научились понимать i.e.
starting with the second character in the string).
In the seventh line, print all the characters of the string in reverse order.
In the eighth line, print every second character of the string in reverse order,
starting from the last one.
In the ninth line, print the length of the given string.
"""
given_str = str(input('введите любое слово '))
print(given_str[2])
print(given_str[1:])
print(given_str[:5])
print(given_str[:-2])
print(given_str[1::2])
print(given_str[0::2])
print(given_str[::-1])
rev = given_str[::-1]
print(rev[1::2])
print(len(given_str))