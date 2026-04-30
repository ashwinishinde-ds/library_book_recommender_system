from flask import Flask, render_template, request, redirect
import pickle
import numpy as np

books = pickle.load(open('books.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

popular_df = books.drop_duplicates('Book-Title').head(50)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=['N/A'] * len(popular_df),
        rating=['N/A'] * len(popular_df)
    )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['GET', 'POST'])
def recommend():

    if request.method == 'POST':
        user_input = request.form.get('user_input')

        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(
            list(enumerate(similarity_scores[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')

            item.append(temp_df['Book-Title'].values[0])
            item.append(temp_df['Book-Author'].values[0])
            item.append(temp_df['Image-URL-M'].values[0])

            data.append(item)

        return render_template('recommend.html', data=data)

    # if user directly opens URL (GET request)
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)