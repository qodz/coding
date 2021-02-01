#check if the set of
def isValid(s):
    stack = []
    dict = {"]":"[","}":"{",")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []
print(" The expression []{} is valid?:"+ str(isValid("[]{}")))
