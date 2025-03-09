import config
import pandas as pd

print(config.CONFIG)

scores = pd.read_csv('scores.csv', header = 0)
round_score = [config.CONFIG["unique_id"], config.CONFIG["treatment"]]

for i in range(17):
    round_score.append(i)

print(len(round_score))

new_row = pd.DataFrame([round_score], columns = scores.columns)
file = pd.concat([scores,new_row], ignore_index = True)
file.to_csv('scores.csv', index = False)