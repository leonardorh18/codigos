inp = input("String: ")
newString = "".join(inp[-i] for i in range(1, len(inp)+1))
print(newString)