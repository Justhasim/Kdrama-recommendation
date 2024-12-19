from flask import Flask, render_template, request, session
import pandas as pd
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session

# Load the dataset
df = pd.read_csv('kdrama.csv')

# Clean and preprocess the data
df['Genre'] = df['Genre'].apply(lambda x: x.split(', '))
df['Genre'] = df['Genre'].apply(lambda x: [genre.strip().lower() for genre in x])
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# TMDB API Key
API_KEY = 'b9117333df86153373d3ea62657f6b3c'

def get_tmdb_poster(drama_name):
    search_url = f'https://api.themoviedb.org/3/search/tv?api_key={API_KEY}&query={drama_name.replace(" ", "+")}'
    response = requests.get(search_url)
    data = response.json()

    if data['results']:
        poster_path = data['results'][0].get('poster_path', None)
        if poster_path:
            return f'https://image.tmdb.org/t/p/w500{poster_path}'
    return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_genres_input = request.form['genres']
    user_rating_input = float(request.form['rating'])

    user_genres = [genre.strip().lower() for genre in user_genres_input.split(',')]

    # Filter dramas based on the user's selected genres and rating
    filtered_dramas = df[df['Genre'].apply(lambda genre: any(gen in genre for gen in user_genres))]
    filtered_dramas = filtered_dramas[filtered_dramas['Rating'] >= user_rating_input]

    # Store the filtered list in the session for later use
    session['filtered_dramas'] = filtered_dramas[['Name', 'Year of release', 'Number of Episodes', 'Rating']].to_dict('records')

    if session['filtered_dramas']:
        return render_template('index.html', dramas=session['filtered_dramas'])
    else:
        return render_template('index.html', dramas=[], message="No dramas found matching your criteria.")

@app.route('/detail', methods=['POST'])
def drama_detail():
    try:
        # Get the selected number from the form
        selected_number = int(request.form['drama_number'])

        # Retrieve filtered dramas from the session
        filtered_dramas = session.get('filtered_dramas', [])

        # Check if the selected number is valid
        if selected_number < 1 or selected_number > len(filtered_dramas):
            return "Invalid number, please choose a valid drama number."

        # Get the selected drama from the filtered list
        selected_drama = filtered_dramas[selected_number - 1]

        # Get the drama details
        drama_name = selected_drama['Name']
        year = selected_drama['Year of release']
        episodes = selected_drama['Number of Episodes']
        rating = selected_drama['Rating']
        synopsis = df[df['Name'] == drama_name]['Synopsis'].values[0]  # Fetch the synopsis from the original df

        # Get the poster from TMDB
        poster_url = get_tmdb_poster(drama_name)

        # Render the details page with all the data
        return render_template('drama_detail.html', name=drama_name, year=year, episodes=episodes, rating=rating, synopsis=synopsis, poster_url=poster_url)

    except ValueError:
        return "Please enter a valid number."

if __name__ == '__main__':
    app.run(debug=True)
