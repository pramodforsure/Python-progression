# question_1
text = "PROGRAMMING"

print(text[0])
print(text[-1])
print(text[2:7])
print(text[::-1])
# answer_1
P
G
OGRAM
GNIMMARGORP
# question_2
text = "Python"
text[0] = "J"

print(text)
# answer_2
TypeError
# question_3
text = "  hello python  "

print(text.strip())
print(text.upper())
print(text.title())
print(text.replace("python", "world"))
# answer_3
hello python
HELLO PYTHON
Hello Python
hello world
# question_4
data = "Python,Java,C++,JavaScript"

languages = data.split(",")

print(languages)
print(" | ".join(languages))
# answer_4
['Python', 'Java', 'C++', 'JavaScript']
Python | Java | C++ | JavaScript
# question_5
a = "Python123"
b = "12345"
c = "Python"

print(a.isalnum())
print(b.isdigit())
print(c.isalpha())
# answer_5
True
True
True
# question_6
text = "apple"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)
# answer_6
{'a': 1, 'p': 2, 'l': 1, 'e': 1}
# question_7
'''Write a Python program that:
1. Accepts a sentence from the user.
2. Converts the sentence to lowercase.
3. Counts the number of words.
4. Counts the number of characters, excluding spaces.
5. Prints the sentence in reverse order.'''
# answer_7
sentence = input("Enter a sentence: ")


sentence = sentence.lower()


word_count = len(sentence.split())


char_count = len(sentence.replace(" ", ""))

reverse_sentence = sentence[::-1]

print("Lowercase sentence:", sentence)
print("Number of words:", word_count)
print("Number of characters (excluding spaces):", char_count)
print("Reversed sentence:", reverse_sentence)
