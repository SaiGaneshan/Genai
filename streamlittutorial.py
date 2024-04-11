import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  
os.environ['GOOGLE_API_KEY'] = "YOUR_GOOGLE_API_KEY"
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except genai.errors.APIError as e:
        st.error("API error: {}".format(e))
        return None

@st.cache_data
def get_cached_content(selected_option, prompt):
    return get_gemini_response(f"Generate a {selected_option.lower()} based on the following prompt: {prompt}")

st.set_page_config(page_title="Content Generator")

st.header("Content Generator")

selected_platform = st.session_state.get("selected_platform", None)

if st.button("YouTube"):  # Correct placement
    # ...

    selected_platform = "youtube"
    st.session_state.selected_platform = selected_platform
if st.button("Medium"):
    selected_platform = "medium"
    st.session_state.selected_platform = selected_platform
if st.button("reddit"):
    selected_platform = "reddit"
    st.session_state.selected_platform = selected_platform
if st.button("Indie Hackers"):
    selected_platform = "Indie Hackers"
    st.session_state.selected_platform = selected_platform
if st.button("Blog"):
    selected_platform = "Blog"
    st.session_state.selected_platform = selected_platform
if selected_platform == "youtube":
    selected_option = st.radio(
        "What do you want to generate?",
        ("Video Ideas", "Headlines", "Descriptions", "Hashtags")
    )
    if selected_option:
        prompt = st.text_input("Describe what you want to generate:", key="medium_prompt")

        if prompt:
            if st.button("Generate Medium Content"):
                generated_content = get_cached_content(selected_option, prompt)
                if generated_content:  
                    st.subheader(f"Generated Medium {selected_option.title()}:")
                    st.write(generated_content)
                else:
                    st.error("There was an error generating content. Please try again.")


elif selected_platform == "medium":
    selected_option = st.radio(
        "What do you want to generate?",
        ("Headlines", "CTAs")
    )
    if selected_option:
        prompt = st.text_input("Describe what you want to generate:", key="medium_prompt")

        if prompt:
            if st.button("Generate Medium Content"):
                generated_content = get_cached_content(selected_option, prompt)
                if generated_content: 
                    st.subheader(f"Generated Medium {selected_option.title()}:")
                    st.write(generated_content)
                else:
                    st.error("There was an error generating content. Please try again.")

elif selected_platform == "reddit":
    selected_option = st.radio(
        "What do you want to generate?",
        ("Headlines", "CTAs")
    )
    if selected_option:
        prompt = st.text_input("Describe what you want to generate:", key="medium_prompt")

        if prompt:
            if st.button("Generate Medium Content"):
                generated_content = get_cached_content(selected_option, prompt)
                if generated_content: 
                    st.subheader(f"Generated Medium {selected_option.title()}:")
                    st.write(generated_content)
                else:
                    st.error("There was an error generating content. Please try again.")
elif selected_platform == "Indie Hackers":
    selected_option = st.radio(
        "What do you want to generate?",
        ("Headlines", "CTAs")
    )
    if selected_option:
        prompt = st.text_input("Describe what you want to generate:", key="medium_prompt")

        if prompt:
            if st.button("Generate Medium Content"):
                generated_content = get_cached_content(selected_option, prompt)
                if generated_content:
                    st.subheader(f"Generated Medium {selected_option.title()}:")
                    st.write(generated_content)
                else:
                    st.error("There was an error generating content. Please try again.")
            
elif selected_platform == "Blog":
    selected_option = st.radio(
        "What do you want to generate?",
        ("Headlines", "CTAs")
    )
    if selected_option:
        prompt = st.text_input("Describe what you want to generate:", key="medium_prompt")

        if prompt:
            if st.button("Generate Medium Content"):
                generated_content = get_cached_content(selected_option, prompt)
                if generated_content: 
                    st.subheader(f"Generated Medium {selected_option.title()}:")
                    st.write(generated_content)
                else:
                    st.error("There was an error generating content. Please try again.")






   
