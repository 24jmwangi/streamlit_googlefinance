import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("Welcome to my Streamlit application!")

    # Add your Streamlit components here
    if st.button("Say Hello"):
        st.write("Hello, World! This is an update")

if __name__ == "__main__":
    main()