# ==============================================================================
# Youtube 
# Generasi Muda, Bonus Demografi dan Masa Depan Indonesia #
# https://www.youtube.com/watch?v=SzXMacu80o8 # ID Viedo
# https://console.cloud.google.com/welcome API KEY
#===============================================================================
                            

from googleapiclient.discovery import build
import pandas as pd

# API key and video ID
api_key = ""
video_id = "SzXMacu80o8"

# Inisialisasi API YouTube 
youtube = build('youtube', 'v3', developerKey=api_key)

def get_all_comments(video_id, max_total=1000):
    comments = []
    next_page_token = None

    while True:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,  # max allowed per request
            pageToken=next_page_token
        ).execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        next_page_token = response.get("nextPageToken")

        #  stop and next page
        if not next_page_token:
            break

        # limit comment
        if len(comments) >= max_total:
            comments = comments[:max_total]
            break

    return comments

#  show comment
comments = get_all_comments(video_id, max_total=50)  # change total 
for i, comment in enumerate(comments, 1):
    print(f"{i}. {comment}")


# === save result ===
df.to_excel("comments.xlsx", index=False)

#===============================================================================
                                # Cleaning Text Comment
# ==============================================================================


import pandas as pd
import re 
import string

def clean_text(text):
    # 1. Hilangkan karakter khusus dan emoji
    text = re.sub(r'[^\w\s]', '', str(text))
    text = text.encode('ascii', 'ignore').decode('utf-8')  # Hapus emoji
    
    # 2. Ubah ke huruf kecil
    text = text.lower()
    
    # 3. Hilangkan angka
    text = re.sub(r'\d+', '', text)
    
    # 4. Hilangkan whitespace berlebih
    text = ' '.join(text.split())
    
    # 5. Hilangkan tanda baca
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    return text

df['Cleaned_Comment'] = df['Comment'].apply(clean_text)


#===============================================================================
                                # Analysis TextBlob
# ==============================================================================

from textblob import TextBlob


def get_textblob_scores(text):
    blob = TextBlob(text)
    return pd.Series([blob.sentiment.polarity, blob.sentiment.subjectivity])

# Terapkan ke kolom komentar
df[['textblob_polarity', 'textblob_subjectivity']] = df['english_comment'].apply(get_textblob_scores)

# Fungsi untuk memberi label sentimen berdasarkan polarity
def label_textblob(polarity):
    if polarity <= -0.05:
        return 'NEGATIVE'
    elif polarity >= 0.05:
        return 'POSITIVE'
    else:
        return 'NEGATIVE'  

# Terapkan label sentimen
df['textblob_label'] = df['textblob_polarity'].apply(label_textblob)

# Tampilkan distribusi dan persentase
print("Distribusi label TextBlob:")
print(df['textblob_label'].value_counts())

print("\nPersentase:")
print(df['textblob_label'].value_counts(normalize=True).round(2) * 100)



#===============================================================================
                                # Transformers
# ==============================================================================

from transformers import pipeline
import pandas as pd

# Inisialisasi model transformer
transformer_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Fungsi klasifikasi sentimen
def get_transformer_sentiment(text):
    result = transformer_classifier(text[:512])[0]  # Max token limit
    return result['label'], result['score']

# Terapkan ke kolom komentar
transformer_results = df['english_comment'].apply(get_transformer_sentiment)

# Masukkan hasil ke dataframe
df['transformer_label'] = transformer_results.apply(lambda x: x[0])
df['transformer_score'] = transformer_results.apply(lambda x: x[1])

# Cek hasil
print(df[['english_comment', 'transformer_label', 'transformer_score']].head(10))

# Hitung total dan persentase
total_counts = df['transformer_label'].value_counts()
percentage_counts = df['transformer_label'].value_counts(normalize=True) * 100

print("\nTotal Hasil Sentimen dari Transformer:")
print(total_counts)

print("\nPersentase Hasil Sentimen dari Transformer:")
print(percentage_counts.round(2))


#===============================================================================
                                # Data Acurrate
# ==============================================================================

# Import data
import pandas as pd

df = pd.read_excel("/Users/mymac/Desktop/textblobtransformeres2.xlsx")


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LogisticRegression  
from sklearn.metrics import accuracy_score  
from sklearn.metrics import classification_report

vectorizer = TfidfVectorizer(max_features=1000) # sesuai kebutuah 
X_tfidf = vectorizer.fit_transform(df['english_comment'])

y = df['textblob_label']
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, stratify=y)

model = LogisticRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)

print("Akurasi dengan TF-IDF dari komentar:", accuracy_score(y_test, preds))


print(classification_report(y_test, preds))

print(df.columns)
# Ganti nama kolom yang tidak ada dengan nama yang benar
y = df['transformer_label']

# Kode selanjutnya yang sekarang akan berhasil dijalankan
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, stratify=y)

model = LogisticRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)

print("Akurasi dengan TF-IDF dari komentar:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))


