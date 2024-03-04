import streamlit as st
import pandas as pd

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
            .book-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
            }
            .book {
                width: 48%; /* Adjust width to fit two books per row */
                margin-bottom: 20px;
                padding: 10px;
                background-color: white; /* Ensure background color for better visibility */
                border-radius: 5px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* Add shadow effect */
            }
            .book img {
                max-width: 100%;
                height: auto;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Book Recommendation App")

    # Logo
    logo_url = "https://github.com/varsha1709/seaBook/raw/main/logo.png"
    st.markdown(f'<div class="logo"><img src="{logo_url}" alt="SeaBook Logo"> SeaBook</div>', unsafe_allow_html=True)

    # Navbar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "Recommend", "Contact", "Code"))

    if page == "Home":
        st.write("# Top 50 Books")
        st.write("Here are the top 50 books:")

        # Display top 50 books with images, names, votes, and ratings
        st.write('<div class="book-container">', unsafe_allow_html=True)
        for index, row in popular_df.iterrows():
            st.write('<div class="book">', unsafe_allow_html=True)
            st.image(row['Image-URL-M'], caption=row['Book-Title'], width=150)
            st.write(f"**{row['Book-Title']}**")
            st.write(f"Votes: {row['num_rating']}")
            st.write(f"Rating: {row['avg_rating']}")
            st.write('</div>', unsafe_allow_html=True)
        st.write('</div>', unsafe_allow_html=True)

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
        st.write("For inquiries, please contact us at varsha1709v@gmail.com.")

    elif page == "Code":
        st.write("# Python Code")
        with open(__file__, 'r') as f:
            code = f.read()
        st.code(code, language='python')

if __name__ == '__main__':
    main()
