# #In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.
#
# expected_title = "Dashboard"
# actual_title = "Dashboard "
#
# ✅ Test Passed – Title matches
#
#
# True - why >  Strip and convert them into the lowercase = both of them are equal.

expected_title = 'Naga Phani'
actual_title = (input('Please enter the title')).lower().strip()
if actual_title == expected_title.lower():
    print("Title Matched")
else:
    print("Title Not Matched")