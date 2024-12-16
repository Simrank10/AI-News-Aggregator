import tkinter as tk
from tkinter import  messagebox, filedialog
from utils.news_featcher import fetch_news
from utils.categorizer import categories_news
from utils.file_handler import save_categorized_news


class NewsAggregatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI News Aggregator")

        # Country Input
        tk.Label(self.root, text="Country Code:", font=("Helvetica",12)).pack(pady=5)
        self.country_entry = tk.Entry(self.root,width=30)
        self.country_entry.insert(0, "in")
        self.country_entry.pack(pady=5)

        #Category Input
        tk.Label(self.root, text="News Category (Optional):", font=("Helvetica",12)).pack(pady=5)
        self.category_entry = tk.Entry(self.root, width=30)
        self.category_entry.pack(pady=5)

        #Fetch News Button
        tk.Button(self.root, text="Fetch News", command=self.fetch_and_display_news).pack(pady=10)

        #News Display
        self.news_display = tk.Text(self.root, height=20, width=80, wrap=tk.WORD, state=tk.DISABLED)
        self.news_display.pack(pady=10)

        #Save News Button

        tk.Button(self.root, text="Save Categorized News", command=self.save_news).pack(pady=10)
        self.categorized_news = None

    def fetch_and_display_news(self):
        country = self.country_entry.get()
        category = self.category_entry.get()
        articles = fetch_news(country=country, category=category)

        if not articles:
            messagebox.showerror("Error", "No news found. Please try again.")
            return
        self.categorized_news = categories_news(articles)

        self.news_display.config(state=tk.NORMAL)
        self.news_display.delete(1.0, tk.END)

        for category, articles in self.categorized_news.items():
            self.news_display.insert(tk.END, f"Category: {category}\n")
            for article in articles:
                self.news_display.insert(tk.END, f"- {article['title']}\n")
            self.news_display.insert(tk.END, "\n")

        self.news_display.config(state=tk.DISABLED)

    def save_news(self):
        if not self.categorized_news:
            messagebox.showerror("Error", "No news to save.")
            return
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if filepath:
            save_categorized_news(self.categorized_news, filepath)
            messagebox.showinfo("Success", "News saved successfully!")

    def run(self):
        self.root.mainloop()
