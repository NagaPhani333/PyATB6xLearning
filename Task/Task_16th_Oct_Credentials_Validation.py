# Check if the user can log in based on correct username and password.
#
# I/p
#
# username = "admin"
# password = "1234"
#
# O/p
# ✅ Login Successful
#
#
# For the Fail condition Other O/P = ❌ Invalid Credentials
u1 = "admin"
u2 = "1234"
username = input("Please enter username : ")
password = input("Please enter password : ")
if username == u1 and password == u2:
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")