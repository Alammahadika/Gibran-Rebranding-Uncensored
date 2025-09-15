# [Gibran-Rebranding-Uncensored](https://www.mudabicara.id/kajian/re-branding-gibran-dari-bagi-bagi-susu-hingga-jadi-youtuber-sorot-wacana/) 
### by [MudaBicara.id](https://www.mudabicara.id/)
**Project**: A digital investigation into public perception of Gibran Rakabuming Raka's "re-branding" efforts.
In recent months, Gibran Rakabuming Raka has appeared more consistent as a content creator on YouTube — abandoning his "unique" and somewhat eccentric communication style and shifting to a more formal and serious approach. Content such as "Generasi Muda," "Demographic Bonus," and "The Future of Indonesia" are clear examples of this change.

Muda Bicara presents an analysis of netizen comments on these content: many support Gibran's efforts to appear more mature and focused, while some suspect this move is more of a political maneuver than a genuine change in character. Some praise the content for being more informative and educational, but many also feel the changes feel contrived, as if an attempt to "appear different" for the sake of image.
## Objectives
- Collect public comments from public platforms (YouTube) regarding Gibran's new videos and content.
- Conduct sentiment, framing, and word network analysis to observe netizen reaction patterns.
- Assess whether the re-branding received a positive, negative, or was perceived as a political maneuver.

## Data Collection by Scrape
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
## Result Comment Scraped

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
## Cleaning Text Comment
```py
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
```

## Result Cleaning Text Comment
```
# A tibble: 55.988 × 1
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
# ℹ 55.988 more rows
# ℹ Use `print(n = ...)` to see more rows
```
