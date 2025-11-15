# You want to check whether a web page loads within 3 seconds (performance test condition).
#
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

LoadTime = float(input("Please enter load time in seconds: "))
if 3 >= LoadTime > 0:
    print("Page load is perfect")
elif LoadTime > 3:
    print("Page load is too slow")
else:
    print("Please enter a valid load time")




