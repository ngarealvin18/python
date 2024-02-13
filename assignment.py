def palindrome():
    Text = input("Enter a Word:")
    if (Text == Text[::-1]):
          print("Palindrome")
    else:
          print("Not a Palindrome")
palindrome()

