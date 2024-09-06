from pb_rater_example import rater

json_input = {"Asset Size": 1_200_000, "Limit": 5_000_000, "Retention": 1_000_000,"Industry": "Hazard Group 2"}

result = rater.execute(json_input)

print(result)