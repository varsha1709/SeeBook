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

# import streamlit as st
# import pandas as pd
# import numpy as np

# # Load data from pickle files
# popular_df = pd.read_pickle('popular.pk1')

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
#         st.write("# Top 50 Books")
#         st.write("Here are the top 50 books:")
#         st.write(popular_df.head(50))

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
#                     st.image(book[2], caption="Book Cover", width=150)  # Adjust the width here
#             else:
#                 st.write("Book not found. Please enter a valid book title.")

# if __name__ == '__main__':
#     main()









# import streamlit as st
# import pandas as pd
# import numpy as np

# # Load data from pickle files
# popular_df = pd.read_pickle('popular.pk1')

# # Streamlit app code
# def main():
#     st.markdown(
#         """
#         <style>
#             .reportview-container {
#                 background: linear-gradient(to bottom right, black, golden);
#             }
#             .logo {
#                 display: flex;
#                 align-items: center;
#             }
#             .logo img {
#                 width: 50px;
#                 margin-right: 10px;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.title("Book Recommendation App")

#     # Logo
#     st.markdown('<div class="logo"><img src="https://example.com/logo.png" alt="Seabook Logo"> Seabook</div>', unsafe_allow_html=True)

#     # Navbar
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", ("Home", "Recommend", "Contact"))

#     if page == "Home":
#         st.write("# Top 50 Books")
#         st.write("Here are the top 50 books:")

#         # Display top 50 books with images, names, votes, and ratings
#         col_count = 4
#         for i in range(0, len(popular_df), col_count):
#             books_subset = popular_df.iloc[i:i+col_count]
#             st.write("<div style='display: flex;'>", unsafe_allow_html=True)
#             for index, row in books_subset.iterrows():
#                 st.write("<div style='margin-right: 20px;'>", unsafe_allow_html=True)
#                 st.image(row['Image-URL-M'], caption=row['Book-Title'], use_column_width=True)
#                 st.write(f"**{row['Book-Title']}**")
#                 st.write(f"Votes: {row['num_rating']}")
#                 st.write(f"Rating: {row['avg_rating']}")
#                 st.write("</div>", unsafe_allow_html=True)
#             st.write("</div>", unsafe_allow_html=True)

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
#                     st.image(book[2], caption="Book Cover", width=150)  # Adjust the width here
#             else:
#                 st.write("Book not found. Please enter a valid book title.")

#     elif page == "Contact":
#         st.write("# Contact Us")
#         st.write("For inquiries, please contact us at contact@example.com.")

# if __name__ == '__main__':
#     main()
















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
            .logo {
                display: flex;
                align-items: center;
            }
            .logo img {
                width: 50px;
                margin-right: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Book Recommendation App")

    # Logo
    st.markdown('<div class="logo"><img src="https://example.com/logo.png" alt="Seabook Logo"> Seabook</div>', unsafe_allow_html=True)

    # Navbar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "Recommend", "Contact", "Code"))

    if page == "Home":
        st.write("# Top 50 Books")
        st.write("Here are the top 50 books:")

        # Display top 50 books with images, names, votes, and ratings
        col_count = 4
        for i in range(0, len(popular_df), col_count):
            books_subset = popular_df.iloc[i:i+col_count]
            st.write("<div style='display: flex;'>", unsafe_allow_html=True)
            for index, row in books_subset.iterrows():
                st.write("<div style='margin-right: 20px;'>", unsafe_allow_html=True)
                st.image(row['Image-URL-M'], caption=row['Book-Title'], width=150)
                st.write(f"**{row['Book-Title']}**")
                st.write(f"Votes: {row['num_rating']}")
                st.write(f"Rating: {row['avg_rating']}")
                st.write("</div>", unsafe_allow_html=True)
            st.write("</div>", unsafe_allow_html=True)

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

    elif page == "Contact":
        st.write("# Contact Us")
        st.write("For inquiries, please contact us at contact@example.com.")

    elif page == "Code":
        st.write("# Python Code")
        with open(__file__, 'r') as f:
            code = f.read()
        st.code(code, language='python')

if __name__ == '__main__':
    main()
