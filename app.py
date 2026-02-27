import streamlit as st
import os
from search import index_resumes, query_resumes
from database import delete_resume

st.set_page_config(page_title="Endee Resume Intelligence", layout="wide")

st.title("Endee Resume Intelligence System")

RESUME_FOLDER = "resumes"
os.makedirs(RESUME_FOLDER, exist_ok=True)

# Upload resumes
st.header("Upload Resumes")

uploaded_files = st.file_uploader(
    "Upload PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    for file in uploaded_files:

        path = os.path.join(RESUME_FOLDER, file.name)

        if not os.path.exists(path):

            with open(path, "wb") as f:
                f.write(file.getbuffer())

            st.success(f"{file.name} uploaded")


# Show resumes with delete
st.header("Uploaded Resumes")

files = os.listdir(RESUME_FOLDER)

for file in files:

    col1, col2 = st.columns([4,1])

    col1.write(file)

    if col2.button("Delete", key=file):

        os.remove(os.path.join(RESUME_FOLDER, file))

        delete_resume(file)

        st.success("Deleted")

        st.rerun()


# Index
st.header("Index Database")

if "indexed" not in st.session_state:
    st.session_state.indexed = False

if "indexing_done" not in st.session_state:
    st.session_state.indexing_done = False

if st.button("Index Resumes"):

    if st.session_state.indexing_done:
        st.success("Resumes already indexed.")
    else:

        st.write("Starting indexing...")

        index_resumes()

        st.session_state.indexing_done = True

        st.success("Indexing completed successfully.")
    if st.session_state.indexed:
        st.warning("Resumes already indexed")
    else:

        with st.spinner("Indexing resumes..."):
            index_resumes()

        st.session_state.indexed = True
        st.success("Indexing completed successfully")

# Search
st.header("Search")

query = st.text_input("Enter search query")

if st.button("Search"):

    results = query_resumes(query)

    if not results:

        st.warning("No results found")

    else:

        st.subheader(f"Found {len(results)} results")

        for rank, (score, result) in enumerate(results, 1):

            st.write(f"Rank #{rank}")
            st.write(f"Resume: {result['id']}")
            st.write(f"Similarity Score: {round(score,4)}")
            st.write("---")