db = [
    {
        "question": "I zimoy i letom odniom cvetom.",
        "answers": [
            {
                "text": "Elka",
                "is_correct": True,
            },
            {
                "text": "Belka",
                "is_correct": False,
            },
            {
                "text": "Dub",
                "is_correct": False,
            },
            {
                "text": "strelka",
                "is_correct": False,
            },
        ],
    }
]

# db = [
#     {
#         "question": "I zimoy i letom odniom cvetom.",
#         "answers": {
#             "correct": "Elka",
#             "uncorrect": ["Belka", "Dub", "strelka"]
#         }
#     }
# ]

# db = [
#     {
#         "question": "I zimoy i letom odniom cvetom.",
#         "answer_correct": "Elka",
#         "answer_uncorrect": ["Belka", "Dub", "strelka"]
#     }
# ]


letters = "ABCDEFG"

for i in range(len(db[0]["answers"])):
    print(f'{letters[i]}. {db[0]["answers"][i]["text"]}')


print()
print("more pythonic way.")

import string

for i, obj in enumerate(db[0]["answers"]):
    print(f'{string.ascii_uppercase[i]}. {obj["text"]}')


print()
print()
# example of checking
answer = "B"
obj = db[0]["answers"][letters.index(answer)]
print("User inputed", answer, "which is", obj["text"], "that's", obj["is_correct"])
