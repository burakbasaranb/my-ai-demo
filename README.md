# Sentiment Analysis AI Demo

This is a simple demo application that performs basic sentiment analysis using a Naive Bayes classifier.

## Features

- RESTful Flask API
- Naive Bayes classifier with `CountVectorizer`
- CORS support for frontend requests
- Simple HTML interface
- User feedback functionality to update and improve the model

## Requirements

Before you begin, make sure you have:

- **Python 3.8+** installed. You can download Python from [python.org](https://www.python.org/downloads/)
- Optionally: a tool like [pipenv](https://pipenv.pypa.io/en/latest/) or `venv` to create virtual environments (recommended)
- Git (for cloning the repository)

## Installation & Running the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/burakbasaranb/my-ai-demo.git
   cd my-ai-demo
   ```

2. **Install Python (if not already installed)**

   - Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Download and install Python 3.x
   - Make sure to check the option **"Add Python to PATH"** during installation.

   To verify:

   ```bash
   python --version
   ```

3. **(Optional but recommended) Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS / Linux
   venv\Scripts\activate         # Windows
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Start the Flask server**

   ```bash
   python app.py
   ```

6. **Open the application in your browser**

   Visit: [http://localhost:5000](http://localhost:5000)

   You'll see the Sentiment Analysis interface where you can enter text and get predictions.

---

## Folder Structure

```
my-ai-demo/
│
├── app.py                # Flask API
├── model_utils.py        # Model training and update logic
├── templates/
│   └── index.html        # Simple frontend
├── requirements.txt      # Dependencies
└── README.md             # Project instructions
```

---

## Feedback Support

After making a prediction, you can submit feedback about whether the model prediction was correct. This feedback updates the model dynamically and helps it learn from new inputs.

---

## License

MIT
