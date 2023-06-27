import json

# Open the JSON file
# Open the JSON file
with open('json_file.json', 'r') as file:
    content = file.read()
    final_data = json.loads(content)

def question(quest):
    print(quest["question"])
    print("choices:", quest['choices'])
    ans = input('Enter the Correct answer:')
    return ans.lower() == quest["correct_ans"].lower()


#main method
score = 0
total_quest = 0
for i in final_data:
    total_quest += 1
    if question(i) is True:
        score += 1
        print("!Correct Answer")
        print("-"*60)
    else:
        print("Wrong answer")
        print("-" * 60)
print()

print("---------QUIZ COMPLETED---------")
print("Total Question where:", total_quest)
print("Your Score", score)
print((score/total_quest)*100, "% of your answer where correct")