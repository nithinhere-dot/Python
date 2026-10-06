model = {
    "name": "ImageClassifier",
    "accuracy": 0.92,
    "version": 1
}

print(model["accuracy"])

model["version"]=2

model["framework"]="PyTorch"

del model["name"]

print(model)