# Model Card: Mood Machine

This model card covers both the rule-based analyzer and the machine learning classifier developed for the Mood Machine project.

## 1. Model Overview

**Model type:**  
I compared both a **rule-based model** (keyword matching with scoring) and a **machine learning model** (Logistic Regression).

**Intended purpose:**  
The model is designed to classify short social media style text messages into four mood categories: positive, negative, neutral, or mixed.

**How it works (brief):**  
- **Rule-based:** Scans text for specific keywords from predefined lists. It adds 1 point for positive words and subtracts 1 point for negative words. It includes negation logic (flipping the score if "not" is detected).
- **ML version:** Uses a "Bag of Words" approach. It converts text into a grid of word counts (CountVectorizer) and uses Logistic Regression to find mathematical patterns between those words and the human-assigned labels.

## 2. Data

**Dataset description:**  
The dataset contains **20 labeled posts** in `SAMPLE_POSTS`. I expanded the starter set by adding 10 new examples that include modern slang, emojis, and sarcastic tones.

**Labeling process:**  
I manually assigned labels based on the "True Intent" of the message. For example, I labeled sarcastic posts as "negative" even if they contained positive words like "love," because the human meaning was negative.

**Important characteristics of your dataset:**  
- **Slang:** Includes terms like "fr fr", "no cap", "mid", and "highkey".
- **Emojis:** Includes sentiment-heavy icons like 🔥, ✨, 💀, and 🤡.
- **Sarcasm:** Contains examples where the literal words contradict the mood.
- **Mixed Feelings:** Contains sentences like "I graduated but I miss school," which contain both positive and negative signals.

**Possible issues with the dataset:**  
The primary issue is **imbalance and size**. With only 20 examples, the ML model "overfits," meaning it might think the word "Monday" is always negative just because it saw it once in a negative sentence.

## 3. How the Rule Based Model Works

**Your scoring rules:**  
- **Keyword Scoring:** Positive words = +1, Negative words = -1.
- **Negation Handling:** If a word like "not" or "never" precedes a keyword, the score for that keyword is multiplied by -1.
- **Mixed Logic:** If the system detects at least one positive word AND at least one negative word, it automatically defaults to a "mixed" label.
- **Thresholds:** Total Score > 0 is positive; Total Score < 0 is negative; 0 is neutral.

**Strengths of this approach:**  
It is highly transparent and easy to debug. It works perfectly for simple, direct sentences like "I am happy" or "I am not happy."

**Weaknesses of this approach:**  
It is completely "sarcasm-blind." It cannot understand context. For example, "Love that for me" in a sarcastic context is scored as positive because it sees the word "love."

## 4. How the ML Model Works

**Features used:**  
Bag of words representation using `CountVectorizer`.

**Training data:**  
The model was trained on the 20 examples in `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
As I added more data, the ML model became more stable. However, because the dataset is so small, it often achieves 100% accuracy on the training data but fails on new user inputs because it hasn't seen enough variety.

**Strengths and weaknesses:**  
- **Strengths:** It can learn that "💀" or "mid" are negative without me having to write a specific `if` statement for them.
- **Weaknesses:** It is a "black box" compared to the rule-based version; it's harder to explain exactly *why* it made a specific choice.

## 5. Evaluation

**How you evaluated the model:**  
I evaluated both models using the `main.py` and `ml_experiments.py` scripts, which compare predicted labels against my human-assigned labels.

**Examples of correct predictions:**  
1. *"I love this class so much"* -> Predicted: Positive. Correct because "love" is a strong positive signal.
2. *"This project is highkey fire ✨"* -> Predicted: Positive. Correct because the model recognized "fire" and the emoji.

**Examples of incorrect predictions:**  
1. *"Waking up at 5am is definitely my favorite thing ever"* -> Predicted: Positive (Rule-based). Incorrect because the model doesn't understand the sarcasm.
2. *"This day hit different fr fr 💀"* -> The ML model struggled here initially until I added more examples of the "💀" emoji being used negatively.

## 6. Limitations

- **Sarcasm:** Neither model can reliably detect when a user is being sarcastic.
- **Context:** The models look at words in isolation and don't understand the broader story of a post.
- **Size:** The dataset is far too small for the ML model to be used in a real-world production environment.

## 7. Ethical Considerations

If this model were used to monitor student mental health, misclassifying a "mixed" or "negative" post as "neutral" could lead to ignoring someone in distress. Additionally, the model is biased toward the specific slang I used (Gen Z/Internet slang), so it might not work for older users or different cultural groups.

## 8. Ideas for Improvement

- **More Data:** Expanding the dataset to 1,000+ examples would significantly improve the ML model's reliability.
- **VADER or Transformers:** Using a more advanced library like VADER (which is built for social media) or a Transformer (like BERT) would help with sarcasm and context.
- **Intensity Weighting:** Giving words like "terrible" a higher negative weight (-3) than words like "tired" (-1).