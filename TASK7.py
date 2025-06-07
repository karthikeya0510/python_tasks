#break stmt
num = [25,30,20,40,15,25]
sum = 0
for i in num:
    sum += i
    if sum>=100:
        break
print(f"the sum exceeds 100 and the sum is {sum}")

#continue stmt
for i in range (1,600):
    if i%2!=0:
        print(i)
        continue

#pass stmt
num=int(input("enter the number :"))
if num%2==0 :
    print("even")
else:
    pass

#all stmts
code = ["hello", "skip", "world", "break", "python"]
for word in code:
    if word == "break":
        print("loop")
        break  # Exit the loop completely
    elif word == "skip":
        print("Skipping current")
        continue  # Skip the rest of this iteration
    else:
        print(word)  # Print the word
    

