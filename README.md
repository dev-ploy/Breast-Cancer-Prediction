# Breast-Cancer-Prediction
A web application for predicting breast cancer using machine learning.  
Built with Flask, scikit-learn, and Bootstrap.

## Features

- Predicts cancerous or non-cancerous based on user input features
- Clean, responsive UI with Bootstrap
- Displays result images for "Cancerous" and "Not Cancerous"
- Ready for deployment on Vercel

## Project Structure

```
Breast-Cancer-Prediction/
│
├── backend/
│   └── app.py                # Flask application
├── model/
│   └── model.pkl             # Trained ML model (pickle file)
├── static/
│   ├── main.jpg              # Main header image
│   ├── img.jpg               # Cancerous result image
│   └── img1.jpg              # Not cancerous result image
├── templates/
│   └── index.html            # Main HTML template
├── requirements.txt          # Python dependencies
├── vercel.json               # Vercel deployment config
└── .gitignore                # Git ignore file
```

## Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/<your-username>/Breast-Cancer-Prediction.git
   cd Breast-Cancer-Prediction
   ```

2. **Create and activate a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```
   python backend/app.py
   ```
   Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Deployment (Vercel)

- The project includes a `vercel.json` for deployment.
- Push your code to GitHub and import the repo in Vercel.
- Vercel will automatically detect the Python serverless function and deploy.

## Usage

- Enter medical features (comma separated) in the input box.
- Click **Predict** to see the result and corresponding image.

## License

MIT

---

**Note:**  
- Make sure `model/model.pkl` exists and is a valid trained model.
- Place your result images in the `static/` folder as described above.
