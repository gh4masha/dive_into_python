import sys
input = sys.argv[1]

number_of_stairs=int(input)
for i in range(1,number_of_stairs+1):
    print(" "*(number_of_stairs-i)+"#"*i)

