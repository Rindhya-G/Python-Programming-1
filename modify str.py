def modify_str(s):
    result = "" 
    for char in s:
        frequency = s.count(char)
        new_char = chr((ord(char) - ord('a') + frequency) % 26 + ord('a'))
        result += new_char
    return result
input_str= input("enter a string:")
output_str = modify_str(input_str)
print("Output:", output_str)


