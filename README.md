# Library Book Recommendation System

A machine learning based web application that recommends books to users based on their selected book preferences. The project is built using Flask, Pandas, NumPy, and collaborative filtering techniques, with a clean web interface for searching and viewing recommendations.

## Live Demo

Hosted Project: https://library-book-recommendation-system-zkv8.onrender.com/

## Features

* Book recommendation system using similarity scores
* Popular books display on homepage
* Search and recommend books instantly
* Book cover images and author details
* Clean and responsive user interface
* Deployed online for public access

## Tech Stack

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* HTML
* CSS
* Bootstrap
* Gunicorn
* Render

## Project Structure

```text
library_book_recommender_system/
│── csvdata/
│── templates/
│── .gitattributes
│── README.md
│── app.py
│── book-recommender-system.ipynb
│── books.pkl
│── popular.pkl
│── pt.pkl
│── requirements.txt
│── similarity_scores.pkl
```


## Installation and Setup

1. Clone the repository:

```bash id="x0vrpi"
git clone <your-repository-url>
```

2. Move to project folder:

```bash id="h4nfgq"
cd library_book_recommender_system
```

3. Install dependencies:

```bash id="ll7d5m"
pip install -r requirements.txt
```

4. Run the project:

```bash id="d0h7zz"
python app.py
```

5. Open browser:

```text id="mjlwm4"
http://127.0.0.1:5000/
```

## Deployment

The project is deployed on Render.

Live URL: https://library-book-recommendation-system-zkv8.onrender.com/

## Future Improvements

* Personalized recommendations
* Better UI design
* User login system
* Search autocomplete
* More advanced filtering

## Author

Pratik Shere
