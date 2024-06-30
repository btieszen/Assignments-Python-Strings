#Task 2: Sentiment Tally
input1 = "This product is really good. I'm impressed with its quality."
input2 = "The performance of this product is excellent. Highly recommended!"
input3 = "I had a bad experience with this product. It didn't meet my expectations."
input4 = "Poor quality product. Wouldn't recommend it to anyone."
input5 = "The product was average. Nothing extraordinary about it"
total_input = input1 + input2 + input3 + input4 + input5

positive_result = total_input.count("good") + total_input.count("excellent") + total_input.count("great") + total_input.count("awesome") + total_input.count("fantaastic") + total_input.count("superb") + total_input.count("amazing")
negative_result = total_input.count("bad") + total_input.count("Poor") + total_input.count("terrible") + total_input.count("horrible") + total_input.count("awful") + total_input.count("disappointing") + total_input.count("subpar")
 

print(f"There are {positive_result} positive words in the review")
print(f"There are {negative_result} negative words in the review")
