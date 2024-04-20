str2 = "hello python world!"
idx = str2.index("python")
str2 = str2[:idx] + "happy" + str2[idx+len("python"):]
print(str2)
