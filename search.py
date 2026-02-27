import os
import time
from resume_parser import extract_text
from embedder import create_embedding
from database import store_resume, search_resume

# Folder where resumes are stored
RESUME_FOLDER = "resumes"


def index_resumes():
    """
    Index all resumes from the resumes folder into Endee vector database.
    Prevents duplicate indexing crashes and shows progress in terminal.
    """

    # Check if folder exists
    if not os.path.exists(RESUME_FOLDER):
        print(f"Resume folder '{RESUME_FOLDER}' does not exist.")
        return

    files = os.listdir(RESUME_FOLDER)

    if len(files) == 0:
        print("No resumes found to index.")
        return

    print(f"\nFound {len(files)} resumes")

    success_count = 0
    fail_count = 0

    for file in files:

        # Only process PDFs
        if not file.lower().endswith(".pdf"):
            continue

        path = os.path.join(RESUME_FOLDER, file)

        print(f"\nIndexing: {file}")

        try:
            start_total = time.time()

            # Step 1: Extract text
            start = time.time()
            text = extract_text(path)
            print(f"Text extraction time: {round(time.time()-start,2)} sec")

            if not text.strip():
                print("Empty resume, skipping")
                fail_count += 1
                continue

            # Step 2: Create embedding
            start = time.time()
            embedding = create_embedding(text)
            print(f"Embedding time: {round(time.time()-start,2)} sec")

            # Step 3: Store in Endee
            start = time.time()
            store_resume(file, embedding, text)
            print(f"Insert time: {round(time.time()-start,2)} sec")

            print(f"Total time: {round(time.time()-start_total,2)} sec")

            success_count += 1
            print(f"Inserted successfully: {file}")

        except Exception as e:
            fail_count += 1
            print(f"Failed or duplicate: {file}")
            print("Error:", e)

    print("\nIndexing complete")
    print(f"Successfully indexed: {success_count}")
    print(f"Failed/skipped: {fail_count}")


def query_resumes(query):
    """
    Search resumes using semantic vector search.
    """

    if not query.strip():
        print("Empty query received")
        return []

    try:
        embedding = create_embedding(query)

        results = search_resume(embedding)

        print(f"Search returned {len(results)} results")

        return results

    except Exception as e:
        print("Search failed:", e)
        return []