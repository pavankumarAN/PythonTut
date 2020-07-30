wish = open("/Users/pavankumaran/PythonTut/Self_Reading/files/sample.txt")

# for i in range(21):
# print(len(wish.readline()))
# for line in wish:
#     print(line)
#     print(len(line))
# wish.close()
wish = open("/Users/pavankumaran/PythonTut/Self_Reading/files/sample.txt","a")
wish.write("\nAt last I want to make use of every penny I earn to india with my brother and wife")
wish.close()
wish1 = open("/Users/pavankumaran/PythonTut/Self_Reading/files/sample.txt")
for linNew in wish1:
    print(linNew)
wish1.close()
# print(wish.read(10))
