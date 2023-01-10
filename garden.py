# importing spacy
import spacy

# loading the pre-trained spacy model
nlp = spacy.load("en_core_web_sm")

# creating a list of garden path sentences
gardenpathSentences = [
    "The old man the boat sailed out to sea.",
    "The complex houses married and single soldiers and their families.",
    "The horse raced past the barn fell.",
    "The farmer plants the seeds in the soil with the shovel.",
    "The teacher was busy grading papers when the students arrived.",
]

# tokenize and perform entity recognition on each sentence from the list
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    
    print("Sentence: ", sentence)
    print("Tokens: ", [token.text for token in doc])
    print("Entities: ", [(i, i.label, i.label) for i in doc.ents])
    print()

# The entity recognition is returning an empty list