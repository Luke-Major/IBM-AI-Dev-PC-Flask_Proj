from EmotionDetection import emotion_detector

dic = {'I am glad this happened':"joy",
'I am really mad about this':"anger",
'I feel disgusted just hearing about this':"disgust",
'I am so sad about this' : "sadness",
'I am really afraid that this will happen':"fear"}

dic_values = list(dic.values())

prompts = dic.keys()

predictions = []

for prompt in prompts:
    prediciton = emotion_detector(prompt)
    predictions.append(prediciton)

j = 0

for i in range(len(predictions)):
    keys = list(predictions[i].keys())
    values = list(predictions[i].values())
    j = values.index(max(values))
    if keys[j] == dic_values[i]:
        print(keys[j], " = ", dic_values[i], "so test", i + 1, " passed")
    else:
        print(keys[j], " != ", dic_values[i], "so test", i + 1, " failed")