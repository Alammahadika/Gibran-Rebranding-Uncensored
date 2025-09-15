# [Gibran-Rebranding-Uncensored](https://www.mudabicara.id/kajian/re-branding-gibran-dari-bagi-bagi-susu-hingga-jadi-youtuber-sorot-wacana/) 
### by [MudaBicara.id](https://www.mudabicara.id/)

**Project Overview**  
This project examines the digital "re-branding" of **Gibran Rakabuming Raka**, whose political persona has been steadily polished for wider public consumption.  
Once known for his awkward, sometimes quirky communication style, Gibran now presents himself as a more formal and serious figure on YouTube. Videos such as *Generasi Muda*, *Demographic Bonus*, and *The Future of Indonesia* suggest a deliberate effort to appear statesmanlike—an image not always consistent with his earlier public appearances.  

Netizen reactions highlight this tension. Supporters frame him as finally “maturing” into a thoughtful leader, while skeptics see the sudden transformation as **manufactured branding** rather than genuine character growth. Many even argue that the videos function less as public education and more as **political advertising in disguise**.  

---

## Objectives
- **Data Collection**: Gather and analyze YouTube comments on Gibran’s recent content.  
- **Analytical Approach**: Use sentiment, framing, and network analysis to reveal how the public perceives his transformation.  
- **Evaluation**: Determine whether the re-branding is received as a **positive development, a negative façade, or simply another calculated political maneuver**.  

## 📥 Data Collection by Scraping
We collected YouTube comments using the YouTube Data API v3 and googleapiclient.
The script retrieves comments from a specific video, with pagination and an optional limit (max_total).

```py
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

```
### Result Comment Scraped

```py
for i, comment in enumerate(comments, 1):
...     print(f"{i}. {comment}")
... 
1. jancook
2. Siapa yg peluang maling. Jabatanmu obsesi joget pajak
3. Bonus demografi. Sudah bayar pajak kah anakmu yg lahir 2014/ 2025 . Pajaknya 1 T. Prode joget pajak
4. Suara nya good❤‍🔥❤‍🔥
5. Pak wapres yg saya cintai.saya  pekerja penjahit di bagian borongan.tapi semakin kesini pekerjaan jait yg gajinya borongan.semakin merosot dari segi upah gajihnya . minta tolong.beri kami perlindungan.di bagian pekerja penjahit borongan.trimakasih semoga di dengar
6. Taekkkkk
7. Keren likesnya banyak banget, keluar anggaran berapa tuh buat beli likes 😂
8. Umur spesies manusia baru 200 ribu tahun di umur bumi yang 4,5 milyar tahun, 10 ribu tahun lalu mulai bertani, 5 ribu tahun lalu mulai beragama, 3 ribu tahun lalu mulai berpikir rasional, 500 tahun lalu mulai tahu bahwa bumi bukanlah pusat alam semesta, dan baru 100 tahun lalu manusia mulai tahu bahwa ada trilyunan galaksi dengan jutaan trilyun matahari dan planet di semesta. <br><br>Baru 100 tahun terakhir menghasilkan pesawat terbang, nuklir, komputer, internet, blockchain. 100 tahun mendatang manusia akan bisa hidup selamanya, menjelajah semesta, dan menciptakan semesta baru. 100 tahun ke depan akselerasi sains dan teknologi akan semakin cepat, deret eksponensialnya akan mengubah manusia ke dasar-dasarnya. Revolusi komputasi dan neurologi akan mengalahkan kematian, revolusi nano akan membuat manusia bisa menciptakan apapun yang diinginkan, dan revolusi genetik akan memudahkan manusia menciptakan tubuh apapun yang mereka inginkan. <br><br>Bersiaplah, roller coaster kemajuan akan membuat siapapun terpana, dan manusia akan menjadi penguasa semesta atau bisa juga punah karenanya, tergantung seberapa hebat dan dewasa manusia menguasai kemajuannya.
9. Makasih ya pak wapres.<br>Tapi saya  malah ngantuk.<br>hoammmm...
10. Tetap semangat, Mas Wapres, abaikan yg nyinyir tanpa otak.. 😂
11. Sumpah komen2 nya setelah dibaca... <br>Saya Auto istighfar langsung pake doa tutup aib... <br>Pembulian fyp sepanjang sejarah Konoha... 😢😢
12. Imam Adz-Dzahabi berkata, “Abu Bilal namanya adalah Mirdas bin Udiyyah, seorang Khawarij tulen. Karena kejahilannya, dia menganggap pakaian tipis bagi kaum pria adalah pakaiannya orang fasiq.” (Siyar A’lam Nubala’, 14: 508 oleh Imam Dzahabi)<br><br>Demikianlah Khawarij sepanjang zaman, mereka salah kaprah dalam metode mengingkari dan jahil akan hal yang diingkari.<br><br>Satu hal lagi yang perlu sekali saya sampaikan di sini bahwa hanya sekedar menghujat pemimpin muslim <del>sekalipun fasiq</del> merupakan ciri khas manhaj Khawarij, sebab manusia tidak akan memberontak pemimipin tanpa ada yang menyalakan api kebencian di hati mereka, walaupun dengan dalih menegakkan pilar amar ma’ruf nahi mungkar.<br><br>Oleh karenanya, para ulama menilai bahwa para penggerak pemberontakan, pengkritik, dan pencela pemimpin adalah Khawarij sekalipun sepanjang sejarah mereka tidak pernah memberontak. Dalam kitab sejarah dan firaq (kelompok dan golongan), mereka disebut Al-Qa’adiyyah.<br><br>Al-Hafizh Ibnu Hajar berkata mensifati sebagian jenis Khawarij, “Dan kaum Al-Qa’adiyyah yaitu kelompok yang melicinkan pemberontakan terhadap pemerintah sekalipun tidak langsung membrontak.”<br><br>Bahkan, kadang-kadang orang yang mengompori untuk berontak lebih jelek daripada yang langsung memberontak sebagaimana diriwayatkan Abu Dawud dalam Masail Ahmad (hal. 271) dari Abdullah bin Muhammad berkata, “Khawarij jenis Al-Qa’adiyyah adalah sejelek-jeleknya kelompok Khawarij!”<br><br>Para ulama masa kini juga telah membendung dan memerangi pemikiran-pemikiran Khawarij model Al-Qa’adiyyah ini.<br><br>Syaikh Muhammad bin Shalih Al-Utsaimin berkata tatkala menjelaskan hadits Dzil Huwaishiroh, “Hadits ini merupakan dalil yang sangat mendasar bahwa berontak pada pemimpin bukan hanya dengan pedang semata tapi bisa juga dengan perkataan dan ucapan. Perhatikanlah, orang ini (Dzul Huwaishrah), dia tidak mengangkat pedang guna membunuh Nabi, tapi dia hanya mengingkarinya (dengan terang-terangan). Apabila dijumpai dalam sebagian kitab ahli sunnah yang menyatakan bahwa berontak itu adalah dengan pedang, maka maksudnya adalah puncak pemberontakan.” (Lihat Fatawa Ulama Al-Akabir, hal. 94-96 dan Madarik An-Nadhar, hal. 272-275 oleh Syaikh Abdul Malik Ramadhani)
13. Mencela pemimpin merupakan ciri khas manhaj yang ditempuh oleh kaum Khawarij. Awalnya hanya sekedar mengkritik dan membeberkan aib pemimpin di atas mimbar, seminar, koran, dan medsos; tetapi membengkak hingga tiada lain terminal akhirnya kecuali memberontak pemimpin.<br><br>Jelas kiranya, metode ini menyelisihi petunjuk Nabi dalam mengingkari penguasa dan merupakan sumber segala fitnah/kerusakan sepanjang sejarah sebagaimana dikatakan Imam Ibnul Qayyim dalam I’lam Muwaqqi’in (3: 7).<br><br>Sebagai bukti bahwa metode seperti itu adalah metode yang diterapkan kaum Khawarij adalah riwayat Imam Tirmidzi dan selainnya dari Ziyad bin Kusaib Al-Adawi, katanya,<br><br>كُنْتُ مَعَ أَبِيْ بَكْرَةَ تَحْتَ مِنْبَرِ أَبِيْ عَامِرٍ وَهُوَ يَخْطُبُ وَعَلَيْهِ ثِيَابٌ رِقَاقٌ, فَقَالَ أَبُوْ بِلاَلٍ: انْظُرُوْا إِلَى أَمِيْرِنَا يَلْبَسُ لِبَاسَ الْفُسَّاقِ, فَقَالَ أَبُوْ بَكْرَةَ : اسْكُتْ! سَمِعْتُ رَسُوْلَ اللهِ يَقُوْلُ: مَنْ أَهَانَ سُلْطَانَ اللهِ فِيْ الأَرْضِ أَهَانَهُ اللهُ<br><br>“Saya pernah bersama Abu Bakrah di bawah mimbar Ibnu Amir yang sedang berkhutbah sambil mengenakan pakaian tipis. Abu Bilal berkata, “Lihatlah pemimipin kita, dia mengenakan pakaian orang-orang fasiq.” Abu Bakrah menegurnya seraya berkata, “Diamlah, saya mendengar Rasulullah bersabda, “Barangsiapa yang menghina pemimpin di muka bumi, niscaya Allah akan menghinakannya.“” (Lihat Shahih Sunan Tirmdzi no. 1812 oleh Al-Albani)
14. Buat anak abah, jangan ngaku islam <br>Tapi ushul aqidah n tauhid rusak loe pada <br><br>Emang khawarij loe pada <br><br>Hai orang-orang yang beriman hendaklah kamu jadi orang-orang yang selalu menegakkan (kebenaran) karena Allah, menjadi saksi dengan adil. Dan janganlah sekali-kali kebencianmu terhadap sesuatu kaum, mendorong kamu untuk berlaku tidak adil. Berlaku adillah, karena adil itu lebih dekat kepada takwa. Dan bertakwalah kepada Allah, sesungguhnya Allah Maha Mengetahui apa yang kamu kerjakan.<br><br>« Al-Ma&#39;idah 7 ✵ Al-Ma&#39;idah 9 »
15. Becik ketitik olo ketoro, kebenaran akan selalu menemukan jalannya
16. Oalah yang hadir banyak kaum RT 16 RW 24, cara berfikir gak pake Logika tapi pake halusinasi👍👍👍
17. ANAK MUDA BANYAK PRESTASINYA EMANG, LAH LU PRESTASINYA APA KOCAK? BEBAN NEGARA YANG ADA
```
## 🧹 Cleaning Text Comment
```py
import pandas as pd
import re 
import string

def clean_text(text):
    # 1. Remove special characters and emojis
    text = re.sub(r'[^\w\s]', '', str(text))
    text = text.encode('ascii', 'ignore').decode('utf-8')  # remove emojis
    
    # 2. Convert to lowercase
    text = text.lower()
    
    # 3. Remove digits
    text = re.sub(r'\d+', '', text)
    
    # 4. Remove extra whitespaces
    text = ' '.join(text.split())
    
    # 5. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    return text

# Apply cleaning
df['Cleaned_Comment'] = df['Comment'].apply(clean_text)

```

### Result Output
```
# A tibble: 55,988 × 1
   Comment                                                                          
   <chr>                                                                            
 1 ngemeng doang woiii aksi nya mane apa yg lo siapin untuk tap bonus demografi nya…
 2 ramalan cuaca untuk beberapa bulan kedepanbrarea jakarta pusat dsan sekitarnya b…
 3 ok laaah tombol dislike diumpetin jumlahnya jumlah viewers juta per hari ini jum…
 4 woy kenapa tombol dislikenya diumpetin jumlahnya                                 
 5 pembodohan rakyat produktif apa noh lihat generasi muda narkoba sdh meluas de ko…
 6 podcast sama ferryirwandi pak waperss                                            
 7 hahahahha lucu mas                                                               
 8 kaku amat pak                                                                    
 9 is it true that you will make indonesia proud in take care of the children in pa…
10 sadar diri pak tidak cocok jadi wakil presiden                                   
# ℹ 55,988 more rows
# ℹ Use `print(n = ...)` to see more rows

```

## Comment Result Translate to Engglish 

## 📊 Sentiment Analysis with TextBlob

### 📌 Overview
We applied TextBlob for sentiment classification on YouTube comments.
TextBlob generates two key scores:
Polarity → ranges from -1 (very negative) to +1 (very positive).
Subjectivity → ranges from 0 (objective) to 1 (subjective).

### 🔎 Labeling Rules
```
<= -0.05 → NEGATIVE
>= +0.05 → POSITIVE
Otherwise → NEGATIVE (neutral merged with negative for this dataset).
```
``` py
from textblob import TextBlob

def get_textblob_scores(text):
    blob = TextBlob(text)
    return pd.Series([blob.sentiment.polarity, blob.sentiment.subjectivity])

# Apply polarity & subjectivity extraction
df[['textblob_polarity', 'textblob_subjectivity']] = df['english_comment'].apply(get_textblob_scores)

# Sentiment labeling
def label_textblob(polarity):
    if polarity <= -0.05:
        return 'NEGATIVE'
    elif polarity >= 0.05:
        return 'POSITIVE'
    else:
        return 'NEGATIVE'

df['textblob_label'] = df['textblob_polarity'].apply(label_textblob)


```
### Result Sentiment TextBlob
```py
NEGATIVE    10493
POSITIVE     3940
Name: count, dtype: int64
```
```
NEGATIVE    73.0%
POSITIVE    27.0%

```


## Sentiment Analysis with Transformers
```py
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

```
### Result Sentiment Tranformers
```py
from transformers import pipeline
clf = pipeline("sentiment-analysis")
print(clf("Gibran sekarang lebih serius di YouTube."))
```
```py
[{'label': 'NEGATIVE', 'score': 0.8695}]
```
The model classified the input sentence as NEGATIVE with a confidence score of 0.87.
However, since the default model is trained on English data (SST-2), the result may not be fully reliable for Indonesian text. A multilingual or fine-tuned model on Indonesian datasets is recommended for more accurate results

## Data Text Accurate 
```py
  # Data accurate

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

y = df['transformer_label']

X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, stratify=y)

model = LogisticRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)

print("Akurasi dengan TF-IDF dari komentar:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))

```
### 📊 Sentiment Classification Result
```py
print(classification_report(y_test, preds))
Akurasi dengan TF-IDF dari komentar: 0.7755610972568578
              precision    recall  f1-score   support

    NEGATIVE       0.79      0.91      0.84      2391
    POSITIVE       0.74      0.51      0.61      1218

    accuracy                           0.78      3609
   macro avg       0.76      0.71      0.73      3609
weighted avg       0.77      0.78      0.76      3609

```
Experiments on YouTube comment sentiment analysis using TF-IDF + supervised classification achieved an accuracy of 77.5%.
The model performs well in identifying negative comments (precision 0.79, recall 0.91), while its performance on positive comments is comparatively lower (precision 0.74, recall 0.51).
The evaluation output using classification_report (sklearn) indicates that overall, the model is reasonably reliable for analyzing public discourse regarding Gibran’s re-branding.


## Visual Data 

```r
library(readxl)
textblobtransformeres2 <- read_excel("textblobtransformeres2.xlsx")
View(textblobtransformeres2)

# Sentiment Transformers 

library(ggplot2)

ggplot(textblobtransformeres2, aes(x = textblob_polarity, y = textblob_subjectivity, color = transformer_label)) +
  geom_point(size = 1.5) +
  scale_color_manual(  # Gunakan scale_color_manual 
    values = c("POSITIVE" = "blue", "NEGATIVE" = "red"),  # Pastikan nama kategori sesuai dengan data
    name = "Sentiment"  
  ) +
  labs(
    title = "Subjektivitas & Polaritas Konten YouTube Gibran Rakabuming",
    subtitle = "Generasi Muda, Bonus Demografi dan Masa Depan Indonesia",
    x = "Polaritas",
    y = "Subjektivitas"
  ) +
  theme_bw() +
  geom_vline(xintercept = 0, linetype = "dashed", color = "grey") +
  geom_hline(yintercept = 0.5, linetype = "dashed", color = "grey") +
  theme(plot.title = element_text(face = "bold")) 


```

![](sentiment/visual2.png)

## Sentiment Analysis: Polarity & Subjectivity Scatter Plot

### Interpretation
- **Polarity (X-axis):** -1 = very negative, +1 = very positive.  
- **Subjectivity (Y-axis):** 0 = objective/factual, 1 = subjective/opinion.  

**Key findings:**
1. Most comments fall in the **subjective area (>0.5)**, indicating that discussions are primarily based on personal opinions rather than factual statements.  
2. Red dots (negative) dominate the **left side** (polarities < 0), while blue dots (positive) cluster more on the **right side** (polarities > 0).  
3. The overall center of distribution leans toward **neutral–negative polarity with high subjectivity**, suggesting that critical opinions expressed in a subjective tone are common.  

### Overall Insights
- The discourse is **opinion-driven** rather than fact-based.  
- **Negative comments** are more diverse and scattered across the polarity spectrum.  
- **Positive comments**, while fewer, are more concentrated at higher polarities, showing stronger consistency in supportive expressions.  
