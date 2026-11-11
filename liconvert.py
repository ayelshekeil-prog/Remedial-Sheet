print("Enter the list you wanna convert: \n")
lines = []
while True:
    line = input()
    if line == "dddd":
        break
    if line == "":
        continue
    lines.append(line)
    
print("------------------------------------------------------\n")
for li in lines:
    li = f"<li>{li}</li>"
    print(li)
