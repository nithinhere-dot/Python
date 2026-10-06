predictions = [0.91, 0.23, 0.87, 0.45, 0.76]

high_predictions = []

for prediction in predictions:
    if prediction > 0.5:
        high_predictions.append(prediction)

print(high_predictions)

def list_compre():
    high_predictions = [
    prediction
    for prediction in predictions
    if prediction > 0.5
    ]
    return high_predictions