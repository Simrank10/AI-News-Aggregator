### **AI News Aggregator: Aggregates News and Categorizes Them**

For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!

This project will create an **AI-powered News Aggregator** that collects news from selected sources, categorizes it using NLP-based techniques, and displays the results in a user-friendly **Tkinter-based GUI**.

---

### **Features of the News Aggregator**

1. **News Aggregation**:
   - Fetch news articles from selected sources using **News API** or web scraping (e.g., BeautifulSoup).

2. **Categorization**:
   - Classify articles into categories like technology, sports, politics, business, etc., using **NLP techniques**.

3. **GUI**:
   - A clean and interactive **Tkinter** GUI to display aggregated and categorized news.

4. **Search and Filter**:
   - Allow users to search or filter news by keywords or categories.

5. **Save News**:
   - Option to save categorized news as a `.csv` file.

---

### **File and Folder Structure**

Here’s the folder structure for the project:

```bash
NewsAggregator/
├── data/
│   ├── sample_news/              # Folder for storing sample news articles
├── gui/
│   ├── __init__.py               # Initializes the GUI module
│   ├── news_gui.py               # GUI implementation using Tkinter
├── utils/
│   ├── __init__.py               # Initializes the utils module
│   ├── news_fetcher.py           # Fetches news from APIs or websites
│   ├── categorizer.py            # Categorizes news articles into predefined categories
│   ├── file_handler.py           # Handles file exports for saving categorized news
├── main.py                       # Entry point to run the application
├── requirements.txt              # Dependencies required for the project
├── README.md                     # Documentation for the project
```

---


### **Installation Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/thekartikeyamishra/AI-News-Aggregator.git
   cd NewsAggregator
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

---

### **Features**

1. Fetches news articles from trusted sources using the NewsAPI.
2. Categorizes articles into predefined categories using NLP.
3. Displays categorized articles in a clean GUI.
4. Allows saving categorized news into a `.csv` file.

This **basic version** of the News Aggregator is now ready. Let me know if you'd like to proceed with advanced features or further enhancements!
