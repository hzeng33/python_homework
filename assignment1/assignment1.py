# Write your code here.

# Task 1: Hello
def hello():
    return "Hello!"

# print(hello())


# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

# print(greet("Hannah"))


# Task 3: Calculator
def calc(num1, num2, operation="multiply"):
    try:
        match operation:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                return num1 / num2
            case "modulo":
                return num1 % num2 
            case "int_divide":
                return num1 // num2
            case "power":
                return num1 ** num2
            case _:
                return "Invalid operation provided."
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
# print(calc(6, 2, "add"))


# Task 4: Data Type Conversion
def data_type_conversion(value, type):
    try:
        match type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
            case _:
                return "Invalid type provided."
    except ValueError:
        return f"You can't convert {value} into a {type}."
    
# print(data_type_conversion(7, "float"))


# Task 5: Grading System, Using *args
def grade(*args):
    try:
        total = sum(args)
        average = total // len(args)
        if average >= 90:
            return "A"
        elif average >= 80 and average < 90:
            return "B"
        elif average >= 70 and average < 80:
            return "C"
        elif average >= 60 and average < 70:
            return "D"
        else:
            return "F"
    except Exception:
        return "Invalid data was provided."
    
# print(grade(80, 85, 78, 88, 90))


# Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result

# print(repeat("Hello", 3))


# Task 7: Student Scores, Using **kwargs
def student_scores(position, **kwargs):
    if position == "best":
        return max(kwargs, key=kwargs.get)
    elif position == "mean":
        return round((sum(kwargs.values()) / len(kwargs)), 2)

# print(student_scores("mean", Alice=90, Bob=85, John=88, Jane=92))


# Task 8: Titleize, with String and List Operations
def titleize(string):
    words = string.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 :
            result.append(word.capitalize())
        if i > 0 :
            if word in [ "a", "on", "an", "the", "of", "and", "is", "in"] and word != words[-1]:
                result.append(word.lower())
            elif word == words[-1]:
                result.append(word.capitalize())
            else:
                result.append(word.capitalize())
    return " ".join(result)


# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    guess_list = list(guess)
    result = ""
    for char in secret:
        if char in guess_list:
            result += char
        else:
            result += "_"
    return result

# print(hangman("alphabet", "ab"))


# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(eng_string):
    result = []
    vowels = "aeiou"
    words = eng_string.split()
    
    for word in words:
        if word[0] in vowels:
            pig_word = word + "ay"
        else:
            i = 0
            while i < len(word):
                if word[i] in vowels:
                    break
                if word[i:i+2] == "qu":
                    i += 2
                    break
                i += 1
                
            pig_word = word[i:] + word[:i] + "ay"
        result.append(pig_word)
    
    return " ".join(result)






            
            