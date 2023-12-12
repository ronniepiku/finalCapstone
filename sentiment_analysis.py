# import required modules
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd

# Load in .csv file and convert to a pandas dataframe
df = pd.read_csv("amazon_product_reviews.csv")

# Drop any values that contain NaN in the reviews.text column
reviews_data = df['reviews.text'].dropna()

# Load the spacy model to perform nlp
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')  # Add text blob to the pipeline of the nlp, so we can get polarity. Polarity is preferred
# here since the reviews are un-labeled, making it difficult to predict sentiment based on similarity.


# Define a function which takes a review as input and outputs the sentiment of that review.
def predict_sentiment(review):
    # Process the review text using SpaCy
    doc = nlp(review)

    # Remove stop words, convert to lowercase, and strip whitespace.
    clean_tokens = [token.text.lower().strip() for token in doc if not token.is_stop]

    # Join cleaned tokens back into a string
    cleaned_review = ' '.join(clean_tokens)

    # Process the cleaned review text using SpaCy
    cleaned_doc = nlp(cleaned_review)

    # Get the polarity score
    polarity_score = cleaned_doc._.blob.polarity

    # Set a threshold for polarity score which determines if something is positive, negative or neutral
    if polarity_score >= 0.3333333333:  # This value is selected to split the three categories evenly. If you wanted to
        # only see strong sentiment scores appear for positive and negative, you can increase these values
        return 'Positive'
    elif polarity_score <= -0.3333333333:
        return 'Negative'
    else:
        return 'Neutral'  # Anything not in those bounds is neutral


# Apply the cleaning steps to the entire reviews_data variable
cleaned_reviews_data = reviews_data.apply(predict_sentiment)

# Define some sample reviews to test on
sample_reviews = ["I absolutely love this product. It's amazing!",
                  "The product was average and delivery was slow. Ok at best.",
                  "I hated this! Never buying again.",
                  "I liked it... Maybe a bit over priced but a good product overall.",
                  "Would recommend to a friend."]

# Loop through each review and print sentiment
for sample_review in sample_reviews:
    predicted_sentiment = predict_sentiment(sample_review)
    print(f'The predicted sentiment is: {predicted_sentiment}')
