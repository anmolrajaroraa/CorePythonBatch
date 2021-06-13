x, y = 10, 20
outputFile = open("output.txt", "w")

print("v=", 3, "cm :", x, ",", y+4, sep="_",
      end="\n\n$$$$$$$$$$\n\n", file=outputFile)
# v= 3 cm : 10 , 24
