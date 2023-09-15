import pandas as pd

json_data = pd.read_json("samantha-1.1.json")

questions = []
answers = []

# Iterate through the DataFrame to reformat the data
for _, row in json_data.iterrows():
    conversations = row['conversations']
    for i in range(0, len(conversations) - 1):
        if i + 1 < len(conversations):
            questions.append(conversations[i]['value'])
            answers.append(conversations[i + 1]['value'])

# Create a new DataFrame with the reformatted data
new_data = pd.DataFrame({'question': questions, 'answer': answers})

# Save the reformatted DataFrame to a CSV file
new_data.to_csv('formated_data.csv', index=False)

# Display the reformatted DataFrame (optional)
print(new_data)

