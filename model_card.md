# Model Card: Mood Machine 

I built this for the Week 5 lab to see how basic sentiment analysis works. I tested out a rule-based model and a simple machine learning model to see which one was better at guessing moods.

## 1. Model Overview

**Model type:**  
I compared both models. The first one is just a bunch of "if/else" rules I wrote in Python, and the second one is a basic Machine Learning classifier using scikit-learn.

**Intended purpose:**  
The goal is to take short social media-style posts and label them as **positive**, **negative**, **neutral**, or **mixed**. 

**How it works:**  
- **Rule-Based:** It looks through the sentence for specific keywords. Good words get +1 and bad words get -1. I also added a rule so if it sees a word like "not," it flips the score of the next word.
- **ML Version:** This one uses a "Bag of Words" approach. It basically counts how many times each word appears and tries to find a mathematical pattern between those words and the labels I gave it.

## 2. Data

**Dataset description:**  
There are **14 posts** in the dataset right now. I expanded the starter list to include things like "ngl," "fr fr," and some emojis like "💀" and "🔥" because that's how people actually talk.

**Labeling process:**  
I labeled them myself based on what I thought the person meant. Some were hard, like "I failed my quiz lmaooo 💀😂." Even though there are laughing emojis, I labeled it as **negative** because failing a quiz is obviously bad.

**Characteristics of the data:**  
- It has a lot of Gen Z slang.
- It includes some sarcasm.
- It has "mixed" feelings where someone says something good and bad in the same sentence.

**Possible issues:**  
The biggest problem is that the dataset is tiny. Since there are only 14 examples, the ML model is probably just memorizing the specific words I used instead of actually "learning" sentiment.

## 3. How the Rule Based Model Works

**Your scoring rules:**  
- I used a `preprocess` function to make everything lowercase so "HAPPY" and "happy" count the same.
- **Negation:** If the model sees "not," "never," or "isnt," it flips the score of the word right after it.
- **Mixed Moods:** I wrote a rule that says if a sentence has both a positive word and a negative word, just label it "mixed."
- **Thresholds:** If the final score is above 0, it's positive. Below 0 is negative. 0 is neutral.

**Strengths:**  
It’s really easy to see why it made a choice. It also handled the "not happy" example correctly because of my negation rule.

**Weaknesses:**  
It’s terrible at sarcasm. If I say "Oh great, I love traffic," it just sees the words "great" and "love" and thinks I'm having a blast.

## 4. How the ML Model Works

**Features used:**  
It uses `CountVectorizer` to turn the words into numbers.

**Training data:**  
It trained on the same 14 posts from `dataset.py`.

**Strengths and weaknesses:**  
The ML model is cool because it can pick up on emojis being negative (like the skull emoji) without me having to write a specific rule for it. But because the data is so small, it gets confused if I type a word it hasn't seen before.

## 5. Evaluation

**How you evaluated the model:**  
I just ran the `main.py` and `ml_experiments.py` scripts and looked at the accuracy percentage at the end.

**Correct predictions:**  
- *"I love this class so much"* -> Predicted **positive**. (Easy keyword match).
- *"I am not happy about this"* -> Predicted **negative**. (My negation logic actually worked here).

**Incorrect predictions:**  
- *"Oh great, my alarm didn't go off."* -> Predicted **positive**. (It doesn't understand that I'm actually annoyed).

## 6. Limitations

The biggest limitation is that the model is only as smart as my word lists. If I don't include a word like "ecstatic," the rule-based model has no idea what it means. Also, the dataset is way too small to be useful for real-world stuff.

## 7. Ethical Considerations

If a company used this to scan customer messages, they might miss people who are being sarcastic and angry. Also, if it's used for something serious like mental health, misclassifying a "mixed" post as "neutral" could mean someone's distress gets ignored.

## 8. Ideas for Improvement

1. Add way more data (like hundreds of rows).
2. Use a better library that already knows about millions of words (like VADER).
3. Make the negation rule smarter so it affects more than just the very next word.
4. Add more slang and emojis to the lists.