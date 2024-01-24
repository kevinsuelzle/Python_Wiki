a = 100
b = 150

if a < b:
    result = a + b
    if result > 30:
        result = result + 5
    else:
        result = result - 3
else:
    result = a - b
    if result < 10:
        result = result * 2
    else:
        result = result // 2
print(result)
