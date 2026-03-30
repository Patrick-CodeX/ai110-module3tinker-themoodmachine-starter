# Model Card: Mood Machine 

I built this for the Week 5 lab to see how basic sentiment analysis works. I tested out a rule-based model and a simple machine learning model.

## 1. Model Overview
**Model type:** I compared both models. The first is a rule-based system using keyword matching, and the second is a basic Machine Learning classifier.
**Intended purpose:** To classify short posts into four moods: positive, negative, neutral, or mixed.
**How it works:** 
- **Rule-Based:** It uses a preprocess function to clean text. It gives +1 for good words and -1 for bad words. I added a negation rule so "not happy" counts as negative.
- **ML Version:** It uses a "Bag of Words" approach to find patterns between words and labels.

## 2. Data
**Dataset description:** My dataset currently has **14 labeled posts**. I expanded the starter list to include slang like "fr fr," "ngl," and "lmaooo," plus emojis like 💀 and 😑.
**Labeling process:** I labeled them based on what I thought the person meant. Sarcasm was the hardest to label because the words are "good" but the feeling is "bad."

## 3. How the Rule Based Model Works
**Your scoring rules:** 
- It uses a simple loop to check tokens against word lists.
- **Negation:** If "not" or "never" is found, it flips the sentiment of the next word.
- **Mixed:** If a sentence has both a positive word and a negative word, it returns "mixed."
**Strengths:** It is very clear. It got "I am not happy" right, which is cool.
**Weaknesses:** It is totally blind to sarcasm. It sees "love" and assumes the person is happy even if they are complaining about traffic.

## 4. How the ML Model Works
**Features used:** CountVectorizer (Bag of Words).
**Strengths and weaknesses:** The ML model is good because it learns emojis automatically, but with only 14 posts, it's not very smart yet.

## 5. Evaluation
**Results:** My rule-based model got **71% accuracy (0.71)** in the terminal.
**Correct predictions:** 
- *"I love this class so much"* -> Predicted **positive**. (Keyword match).
- *"I am not happy about this"* -> Predicted **negative**. (Negation logic worked).
**Incorrect predictions:** 
- *"Oh great, my alarm didn't go off."* -> Predicted **positive**. (It doesn't understand sarcasm).
- *"I absolutely love sitting in traffic"* -> Predicted **positive**. (Again, sarcasm fail).

## 6. Limitations
The model is way too small. It doesn't know words like "graduated" yet (which is why that one came back neutral), and it can't tell when someone is being ironic or sarcastic.

## 7. Ethical Considerations
If this were used in a real app, it might misinterpret people from different cultures or people who use a lot of sarcasm, which could lead to bad data or ignoring someone's actual feelings.

## 8. Ideas for Improvement
1. Add more words like "graduated" or "miss" to the lists.
2. Get way more data (like 100+ posts) for the ML model to learn from.
3. Make the negation rule handle more than one word.