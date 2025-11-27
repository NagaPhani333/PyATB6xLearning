import time


Page_Load = False
wait_time = 0
while wait_time < 5:
    res = input("Please enter your response(True/False) : ").strip().upper()

    if res == "TRUE":
        Page_Load = True

    if Page_Load:
        print("success")
        break

    time.sleep(1)
    wait_time = wait_time + 1

if not Page_Load:
    print("Timeout")

