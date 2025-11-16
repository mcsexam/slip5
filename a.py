import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

try:
    WordNetLemmatizer()
except LookupError:
    print("Downloading NLTK resources (punkt, wordnet)...")
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    lemmatized_text = " ".join(lemmatized_words)
    return lemmatized_text, words, lemmatized_words

input_text = "The quick brown foxes were running and jumped over the sleeping dogs. She is having great ideas."

if __name__ == "__main__":
    print(f"Original Text: {input_text}")
    final_text, tokens, lemmas = lemmatize_text(input_text)
    print("\n--- Results ---")
    print(f"Tokenized Words: {tokens}")
    print(f"Lemmatized Words: {lemmas}")
    print(f"\nLemmatized Text: {final_text}")
