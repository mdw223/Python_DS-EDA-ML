# 5) Output 3 arguments in a single print statement without spaces between? (2 options)

print("Hello" + "World" + "Python")
# Output: HelloWorldPython
print("Hello", "World", "Python", sep="")
# Output: HelloWorldPython

# Bonus Ways:

a = "Hello"
b = "World"
c = "Python"
print(f"{a}{b}{c}")
# Output: HelloWorldPython

print("%s%s%s" % ("Hello","World","Python"))
# Output: HelloWorldPython

print("".join(["Hello","World","Python"]))
# Output: HelloWorldPython