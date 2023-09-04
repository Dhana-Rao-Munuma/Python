import re
def rearrange_name(name):
  result = re.search(r"^([\w -\.]*), ([\w \.-]*)$", name)
 
  if result == None:
    return name
  print("result " + result[0])
  print(result[1])
  print(result[2])
  #print(result[3])
  #print(result[4])
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy F., John")
print("name:" + name)

name=rearrange_name("Kennedy, John F.")
print("name:" + name)
