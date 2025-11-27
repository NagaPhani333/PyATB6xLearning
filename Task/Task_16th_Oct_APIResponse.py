print("API Response Codes\n 404 Failed Response\n 200 Passed Response")
code = int(input("Enter Response Code: "))
if code == 404:
    print("Failed API Request")
elif code == 200:
    print("Passed API Request", code)
else:
    print("Please enter valid Response code, you hav entered : ", code)