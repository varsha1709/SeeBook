from flask import Flask,render_template,request
import pickle
import numpy as np

#rb= read binary
popular_df = pickle.load(open('popular.pk1', 'rb'))
pt = pickle.load(open('pt.pk1','rb'))
books = pickle.load(open('books.pk1','rb'))
similarity_score = pickle.load(open('similarity_score.pk1','rb'))


app = Flask(__name__)
#Making GUI and then displaying data in it
#HTML,CSS and BOOTSTRAP will be used in GUI
@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           image = list(popular_df['Image-URL-M'].values),
                           votes = list(popular_df['num_rating'].values),
                           rating = list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    try:
        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)

        return render_template('recommend.html', data=data)
    except IndexError:
        # Handle the case where user input doesn't match any books
        error_message = "No matching books found."
        return render_template('recommend.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
