# Import libraries
import re
import contractions
from num2words import num2words

def preprocessing_text(document):
    # Join the content of all pages into a single string
    text = " ".join(page.page_content for page in document)
    
    # Expand contractions in the text (e.g., "don't" => "do not")
    expanded_text = contractions.fix(text)
    
    # Convert numbers to words
    words = expanded_text.split()
    for index, word in enumerate(words):
        if word.isdigit():
            try:
                words[index] = num2words(int(word), lang = "en")
            except ValueError:
                pass
    expanded_text = " ".join(words)
    
    # Remove special characters from the text
    cleaned_text = re.sub(r"[^\w\s]", "", expanded_text)

    return cleaned_text