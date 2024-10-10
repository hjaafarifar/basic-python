listnumbers = [-1, 59, 32, 1, 0, 20, 544, 6]
n = len(listnumbers)
for i in range(n):
    for j in range(0, n-i-1):
        if listnumbers[j+1] < listnumbers[j]:
            listnumbers[j+1], listnumbers[j] = listnumbers[j], listnumbers[j+1]
print(listnumbers)


# The program takes a list and sorts it
# برنامه یک لیست را گرفته و ان را مرتب میکند