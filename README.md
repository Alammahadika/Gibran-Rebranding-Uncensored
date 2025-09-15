# [Gibran-Rebranding-Uncensored](https://www.mudabicara.id/kajian/re-branding-gibran-dari-bagi-bagi-susu-hingga-jadi-youtuber-sorot-wacana/)

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
