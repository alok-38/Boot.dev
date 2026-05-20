string = "racecar"
left = 0
right = len(string) - 1

while left < right:
    if string[left] != string[right]:
        print("Not a palindrome")
        break

    left += 1
    right -= 1
else:
    print("Palindrome")
