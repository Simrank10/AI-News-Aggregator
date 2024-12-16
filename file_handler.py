import csv


def save_categorized_news(categorized_news, filepath="categorized_news.csv"):
    try:
        with open(filepath, mode="w", newline=" ", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Title", "Description", "Source", "URL"])
            for category, articles, in categorized_news.items():
                writer.writerow([
                    category,
                    articles["title"],
                    articles["description"],
                    articles["source"], ["name"],
                    articles["url"]
                ])

        print("News saved successfully!")
    except Exception as e:
        print(f"Error saving news: {e}")
