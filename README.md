# NLP PubMed Journal Articles Recommendation System on Vegetarian/Plant-Based Diets
Bingbing Zhang

## Abstract
The goal of this project was to create a content-based recommendation system for PubMed journal articles on vegetarian/plant-based diets. This unsupervised learning model employs a natural language processing algorithm. The dataset was downloaded from PubMed Central databases that contained key search terms on vegetarian, vegan, and plant-based diets. The data was cleaned and prepared for modeling due to the nature of txt format that was originally pulled. The topic modeling process supported the NMF model with TF-IDF vectorizer which yields the best topics. The recommendation system used cosine similarity between abstracts to create the top five results, in this context the abstracts, according to the key words and/or phrases (text input).


## Design
People who are interested in experimenting with various diets/lifestyle changes could benefit from a collection of evidence based and scientific data-driven studies to facilitate their exploration. This recommendation system may support their search on journal articles of interests. For readers who are practicing vegetarian/plant-based diets/lifestyles, the benefits of reading up-to-date scientific journals on the benefit and risk factors could facilitate wellbeing. The traditional database search engine may be daunting for those who are not familiar with the academic style and the streamlit app (TBA) serves as a user-friendly interface to make the scientific results more accessible to the public. 

## Data
The dataset is pulled from the PubMed Central website https://www.ncbi.nlm.nih.gov/pmc/ The raw dataset contains 5,6024 abstracts of journal articles on PubMed up to 2022 with the search keywords including vegetarian(s), vegan(s), and plant-based.

## Algorithms
**Cleaning:**
During exploratory data analysis, I discovered that some abstracts were related to non-human diet related search words. I excluded abstracts that did not explicitly contain the above mentioned search words. The exclusive dataset contained 3684 abstracts.

**Text Preprocessing:**
The text processing started with the removal of numbers and punctuation. The next step taken was tokenizer. After carefully examined the parts of speech (POS) tagging, adverbs were removed. Three categories of words were lemmatized, noun, adverb, and adjective. 

**Topic Modeling:**
Baseline models were created with different vectorizers (CountVectorizer & TF-IDF) and models (LSA, LDA, and NMF). Other model explored was CorEc but was not used after the examine and comparison of generated topics. The TF-IDF vectorizer and NMF model were eventually selected and the number of topics produced was 9. Custom stop words were added to the standard stop words. 

**Recommendation System:**
The recommendation system was built using the cosine similarity between ranked abstracts’ topic profiles that was selected based on the topic words examples. 

## Tools
Numpy and Pandas for data manipulation
NLTK for text processing
Scikit-learn for preprocessing and modeling
Matplotlib for plotting

## Conclusions
The conclusion is the recommendation system.
