import pandas as pd
# df= pd.read_csv("F:\Project Sentiview Practice\ Model Training\text.csv", encoding="ISO-8859-1")?\
df = pd.read_csv(r"F:\Project Sentiview Practice\ Model Training\text.csv", encoding="ISO-8859-1")


# from sklearn.naive_bayes import MultinomialNB

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test= train_test_split(df.text, df.target, test_size=0.25) 

X_train = X_train.fillna("") 
X_train = X_train.astype(str)
X_test = X_test.fillna("") 
X_test = X_test.astype(str)


clf= Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

clf.fit(X_train, y_train)

# import pickle
# with open('sentiment_model.pkl', 'wb') as model_file:
#     pickle.dump(clf, model_file)

text=['Hello, i am sooo happy today, i just want to dance']
print(clf.predict(text))