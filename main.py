import streamlit as st
from FacebookPostsScraper import FacebookPostsScraper as Fps
from pprint import pprint as pp

st.title('FB Scrape')

def main():
    # Enter your Facebook email and password
    email = 'danielk568@gmail.com'
    password = 'leinadqwer'

    # Instantiate an object
    fps = Fps(email, password, post_url_text='Full Story')

    # Example with single profile
    single_profile = 'https://www.facebook.com/groups/dadventureDO'
    data = fps.get_posts_from_profile(single_profile)
    pp(data)


    fps.posts_to_csv('my_posts')  # You can export the posts as CSV document
    # fps.posts_to_excel('my_posts')  # You can export the posts as Excel document
    # fps.posts_to_json('my_posts')  # You can export the posts as JSON document


if __name__ == '__main__':
    main()
