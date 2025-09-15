library(readxl)
textblobtransformeres2 <- read_excel("textblobtransformeres2.xlsx")
View(textblobtransformeres2)

# Sentiment Transformers 

library(ggplot2)

ggplot(textblobtransformeres2, aes(x = transformer_score, fill = transformer_label)) +
  geom_density(alpha = 0.5, adjust = 6) +
  scale_fill_manual(values = c("POSITIVE" = "blue", "NEGATIVE" = "red")) +
  scale_x_continuous(limits = c(0.6, 1.05), expand = c(0.01, 0.02)) +
  labs(
    title = "Analisis Sentimen Konten YouTube Gibran Rakabuming",
    subtitle = "Generasi Muda, Bonus Demografi dan Masa Depan Indonesia",
    x = "Sentiment Score",
    y = "Density",
    fill = "Sentiment"
  ) +
  theme_bw()


# Sentiment Text Blob >> Polarity & Subjectivity 

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
