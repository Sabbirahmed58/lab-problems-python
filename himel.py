# Number Sorting (Ascending)
num_list = list(map(int, input().split()))
for x in range(len(num_list)):
  for y in range(x+1, len(num_list)):
    if num_list[x] > num_list[y]:
      num_list[x], num_list[y] = num_list[y], num_list[x]
print(num_list)

# Number Sorting (Descending)
num_list = list(map(int, input().split()))
for x in range(len(num_list)):
  for y in range(x+1, len(num_list)):
    if num_list[x] < num_list[y]:
      num_list[x], num_list[y] = num_list[y], num_list[x]
print(num_list)

# Octal to Binary
oct_num = input()
bin_num = ""
for x in oct_num:
  if x == ".":
    bin_num += x
  else:
    bin_digit = ""
    x = int(x)
    while x != 0:
      bin_digit += str(x % 2)
      x //= 2
    bin_num += bin_digit[::-1].zfill(3)
print(bin_num)

# Diamond Printing
row = int(input())
if row % 2 == 0:
  print("Only odd number applicable for draw a diamond shape.")
elif row > 9:
  print("You can't draw diamond with number when row number is upper then 9")
else:
  for x in range(row//2 + 1):
    print(" " * (row//2 - x), f"{2*x + 1}" * (2*x + 1), " " * (row//2 - x), sep="")
  for x in range(row//2):
    print(" " * (x+1), f"{row - 2*(x+1)}" * (row - 2*(x+1)), " " * (x+1), sep="")
