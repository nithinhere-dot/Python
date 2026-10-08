{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2a9bc0b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions=[0.91,0.23,0.87,0.45,0.76]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "abef5d79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.91, 0.87, 0.76]\n"
     ]
    }
   ],
   "source": [
    "high_predictions=[]\n",
    "\n",
    "for prediction in predictions:\n",
    "    if  prediction > 0.5:\n",
    "        high_predictions.append(prediction)\n",
    "print(high_predictions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "46c428f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "high_predictions=[\n",
    "    prediction\n",
    "    for prediction in predictions\n",
    "    if prediction>0.5\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "88b92f50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.91, 0.87, 0.76]\n"
     ]
    }
   ],
   "source": [
    "print(high_predictions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "066d427c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv (3.13.13)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
