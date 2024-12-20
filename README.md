

# K-Drama Recommendation App 🎬  

A Python Flask-based web application where users can input their preferred **genre** and **rating** to get a list of recommended K-Dramas. Users can then choose a specific drama to view detailed information such as the synopsis, poster, and more. The app uses the **TMDB API** to fetch dynamic data.  

# Demo : 

https://kdrama-recom-m18lsyme7-chaudhary-hasims-projects.vercel.app/

---

## 🌟 Features  
- **Genre-Based Filtering**: Choose your favorite genre to find matching K-Dramas.  
- **Rating-Based Recommendations**: Filter dramas based on your preferred rating threshold.  
- **Detailed Information**: Get a synopsis, poster, and other details for each drama.  
- **Dynamic Data**: Real-time fetching of information using the TMDB API.  
- **Interactive Experience**: Simple and intuitive interface for an enjoyable user experience.  

---

## 🛠️ Technologies Used  
- **Backend**: Python Flask  
- **Frontend**: Flask Templates (HTML, Jinja2, CSS)  
- **API Integration**: TMDB API for fetching K-Drama details  
- **Database**: SQLite (for storing user preferences, if needed)  

---

## 🚀 Getting Started  

### Prerequisites  
- Python 3.7 or above  
- Flask installed (`pip install flask`)  
- TMDB API Key (Create an account at [TMDB](https://www.themoviedb.org/) to get your API key)  

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/Justhasim/Kdrama-recommendation.git  
   cd Kdrama-recommendation

2. Install required dependencies:

pip install -r requirements.txt


3. Set up your environment variables:

Create a .env file in the root directory and add:

TMDB_API_KEY=your_tmdb_api_key  
FLASK_ENV=development



4. Run the application:

flask run

The app will be available at http://127.0.0.1:5000.




---

📂 Project Structure

Kdrama-recommendation/  
├── static/  
│   └── css/  
├── templates/  
│   ├── drama_details.html  
│   ├── home.html  
│   ├── index.html   
├── app.py  
├── requirements.txt  
├── .env  
└── README.md


---

🖼️ How It Works

1. Enter Genre and Rating:

Users input their preferred genre (e.g., Romance, Thriller) and a rating threshold (e.g., 8+).



2. View Recommendations:

A list of matching K-Dramas is displayed with posters and titles.



3. Select a Drama:

Clicking on a drama provides detailed information, including the synopsis and poster.



4. Explore More:

Search for additional dramas based on new preferences.





🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.


2. Create a new branch: git checkout -b feature-name.


3. Commit your changes: git commit -m 'Add feature'.


4. Push to the branch: git push origin feature-name.


5. Open a pull request.




---

💬 Contact

For any questions or suggestions, feel free to reach out:

GitHub: Justhasim



---

⭐ Don't forget to star the repository if you find it helpful!

This updated version highlights the genre and rating-based functionality and the step-by-step workflow of the app. Let me know if you'd like further customization!

