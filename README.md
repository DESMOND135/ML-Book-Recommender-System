# 📚 Desmond's Book Recommendation System

This is an **end-to-end Book Recommendation System** I built using **Python, Machine Learning, and Streamlit**.  
It uses **Collaborative Filtering (KNN-based approach)** to recommend books to users based on their interests and past ratings.

---

## 🔥 Key Features
- End-to-end ML pipeline (Data Ingestion → Validation → Transformation → Model Training → Recommendation).  
- Interactive **Streamlit web app** for real-time book recommendations.  
- Personalized recommendations with book covers & titles displayed beautifully.  
- Modular, production-ready code structure with logging, exception handling, and configuration management.  
- Dockerized for easy deployment anywhere.  

---

## ⚙️ Tech Stack
- **Python 3.10**  
- **Pandas, NumPy, Scikit-learn** (ML)  
- **Streamlit** (frontend app)  
- **Pickle** (model persistence)  
- **Docker** (for containerization)  

---

## 🚀 How It Works
1. Train the recommendation engine with book ratings dataset.  
2. Select a book in the Streamlit app.  
3. Instantly get **5 similar book recommendations** with their covers.  

---

## 🛠️ Getting Started

### Run Locally (Steps 1–4 in one go)
```bash
# 1. Clone repo
git clone https://github.com/DESMOND135/ML-Book-Recommender-System.git
cd ML-Book-Recommender-System

# 2. Create & activate conda environment
conda create -n recommender_env python=3.10 -y
conda activate recommender_env

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
