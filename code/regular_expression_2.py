import re
def check_time(text):
  pattern = r"^([1-9]|10|11|12):[0-5][0-9] ?(am|pm)$"
  result = re.search(pattern, text, re.IGNORECASE)
  return result != None


print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False