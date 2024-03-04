# import streamlit as st
# import pickle
# import numpy as np

# # Load data from pickle files
# popular_df = pickle.load(open('popular.pk1', 'rb'))
# pt = pickle.load(open('pt.pk1','rb'))
# books = pickle.load(open('books.pk1','rb'))
# similarity_score = pickle.load(open('similarity_score.pk1','rb'))

# # Streamlit app code
# def main():
#     st.title("Book Recommendation App")

#     # Sidebar for user input
#     user_input = st.text_input("Enter a book title:", "")

#     if st.button("Recommend"):
#         recommend(user_input)

# def recommend(user_input):
#     indices = np.where(pt.index == user_input)[0]
#     if len(indices) > 0:
#         index = indices[0]
#         similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]

#         data = []
#         for i in similar_items:
#             item = []
#             temp_df = books[books['Book-Title'] == pt.index[i[0]]]
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

#             data.append(item)

#         # Display recommendations
#         for item in data:
#             st.write(item)
#     else:
#         st.write("Book not found. Please enter a valid book title.")

# if __name__ == '__main__':
#     main()




# import streamlit as st
# import pandas as pd
# import numpy as np

# # Load data from pickle files
# popular_df = pd.read_pickle('popular.pk1')
# pt = pd.read_pickle('pt.pk1')
# books = pd.read_pickle('books.pk1')
# similarity_score = pd.read_pickle('similarity_score.pk1')

# # Function to recommend books
# def recommend_books(user_input):
#     indices = np.where(pt.index == user_input)[0]
#     if len(indices) > 0:
#         index = indices[0]
#         similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]

#         data = []
#         for i in similar_items:
#             item = []
#             temp_df = books[books['Book-Title'] == pt.index[i[0]]]
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

#             data.append(item)

#         return data
#     else:
#         return []

# # Streamlit app code
# def main():
#     st.markdown(
#         """
#         <style>
#             .reportview-container {
#                 background: linear-gradient(to bottom right, black, golden);
#             }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.title("Book Recommendation App")

#     # Navbar
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", ("Home", "Recommend"))

#     if page == "Home":
#         st.write("# Home Page")
#         st.write("Welcome to the Book Recommendation App!")

#     elif page == "Recommend":
#         st.write("# Recommendation Page")
#         st.write("Enter a book title to get recommendations:")

#         # Sidebar for user input
#         user_input = st.text_input("Enter a book title:", "")

#         # Button to trigger recommendation
#         if st.button("Recommend"):
#             recommended_books = recommend_books(user_input)

#             if recommended_books:
#                 st.subheader("Recommended Books")
#                 for book in recommended_books:
#                     st.write("Title:", book[0])
#                     st.write("Author:", book[1])
#                     st.image(book[2], caption="Book Cover", width=150)
#             else:
#                 st.write("Book not found. Please enter a valid book title.")

# if __name__ == '__main__':
#     main()






#To display the top 50 books on the home page, you can modify the `main()` function to show the list of top books when the user navigates to the "Home" page. Below is the updated code:

import streamlit as st
import pandas as pd
import numpy as np

# Load data from pickle files
popular_df = pd.read_pickle('popular.pk1')

# Streamlit app code
def main():
    st.markdown(
        """
        <style>
            .reportview-container {
                background: linear-gradient(to bottom right, black, golden);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Book Recommendation App")

    # Navbar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "Recommend"))

    if page == "Home":
        st.write("# Top 50 Books")
        st.write("Here are the top 50 books:")
        st.write(popular_df.head(50))

    elif page == "Recommend":
        st.write("# Recommendation Page")
        st.write("Enter a book title to get recommendations:")

        # Sidebar for user input
        user_input = st.text_input("Enter a book title:", "")

        # Button to trigger recommendation
        if st.button("Recommend"):
            recommended_books = recommend_books(user_input)

            if recommended_books:
                st.subheader("Recommended Books")
                for book in recommended_books:
                    st.write("Title:", book[0])
                    st.write("Author:", book[1])
                    st.image(book[2], caption="Book Cover", width=150)  # Adjust the width here
            else:
                st.write("Book not found. Please enter a valid book title.")

if __name__ == '__main__':
    main()
