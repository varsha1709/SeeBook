import streamlit as st
import pickle
import numpy as np

# Load data from pickle files
popular_df = pickle.load(open('popular.pk1', 'rb'))
pt = pickle.load(open('pt.pk1','rb'))
books = pickle.load(open('books.pk1','rb'))
similarity_score = pickle.load(open('similarity_score.pk1','rb'))

# Streamlit app code
def main():
    st.title("Book Recommendation App")

    # Sidebar for user input
    user_input = st.text_input("Enter a book title:", "")

    if st.button("Recommend"):
        recommend(user_input)

def recommend(user_input):
    indices = np.where(pt.index == user_input)[0]
    if len(indices) > 0:
        index = indices[0]
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)

        # Display recommendations
        for item in data:
            st.write(item)
    else:
        st.write("Book not found. Please enter a valid book title.")

if __name__ == '__main__':
    main()

