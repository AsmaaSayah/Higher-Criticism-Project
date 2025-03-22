import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Download NLTK resources (run these once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def advanced_text_processing(text, do_stemming=False, do_lemmatization=True, remove_stopwords=True):
    """
    Processes raw text by performing:
      - Lowercasing
      - Tokenization (preserving hyphenated words)
      - Punctuation and non-alphanumeric filtering
      - Optional stopword removal
      - Optional stemming or lemmatization

    Parameters:
      text (str): The raw text to process.
      do_stemming (bool): Whether to apply stemming.
      do_lemmatization (bool): Whether to apply lemmatization.
      remove_stopwords (bool): Whether to remove stopwords.
      
    Returns:
      List[str]: A list of processed tokens.
    """
    # Convert text to lowercase
    text = text.lower()
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Tokenize text (this preserves hyphenated words as a single token)
    tokens = word_tokenize(text)
    
    # Remove tokens that do not contain any alphanumeric character
    tokens = [token for token in tokens if re.search(r'[a-z0-9]', token)]
    
    # Optionally remove stopwords
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]
    
    # Optionally apply stemming or lemmatization
    if do_stemming:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(token) for token in tokens]
    elif do_lemmatization:
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return tokens
