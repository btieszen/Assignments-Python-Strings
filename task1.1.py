#Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.

input1 = "This product is really good. I'm impressed with its quality."
input2 = "The performance of this product is excellent. Highly recommended!"
input3 = "I had a bad experience with this product. It didn't meet my expectations."
input4 = "Poor quality product. Wouldn't recommend it to anyone."
input5 = "The product was average. Nothing extraordinary about it"
new_input1 = input1.replace("good","GOOD")
new_input2 = input2.replace("excellent","EXCELLENT")
new_input3 = input3.replace("bad","BAD")
new_input4 = input4.replace("Poor","POOR")
new_input5 = input5.replace("average","AVERAGE")
print (new_input1)
print (new_input2)
print (new_input3)
print (new_input4)
print (new_input5)

