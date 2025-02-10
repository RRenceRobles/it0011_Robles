with open("Midterms/numbers.txt", 'r') as file:
    lines = file.readlines()

for index, line in enumerate(lines, start=1):
    values = [num.strip() for num in line.split(',')]
    
    if all(value.isdigit() for value in values):
        numbers = list(map(int, values))
        total = sum(numbers)
        result = "Palindrome" if str(total) == str(total)[::-1] else "Not a palindrome"
        
        print(f"Line {index}: {', '.join(values)} (sum {total}) - {result}")