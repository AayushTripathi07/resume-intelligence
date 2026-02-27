import requests

BASE_URL = "http://localhost:8080/api/v1/index/resumes"


def store_resume(id, embedding, text):

    data = {
        "id": str(id),
        "vector": embedding.tolist(),
        "metadata": {
            "text": text
        }
    }

    try:

        response = requests.post(
            f"{BASE_URL}/vector/insert",
            json=data,
            timeout=5   # prevents hanging forever
        )

        print("Insert status:", response.status_code)
        print("Insert response:", response.text)

    except requests.exceptions.Timeout:
        print("Insert timeout — Endee server not responding")

    except Exception as e:
        print("Insert failed:", e)


def search_resume(query_embedding):

    import os
    from embedder import create_embedding
    from resume_parser import extract_text

    RESUME_FOLDER = "resumes"

    results = []

    try:

        query_vec = query_embedding

        for file in os.listdir(RESUME_FOLDER):

            if not file.endswith(".pdf"):
                continue

            path = os.path.join(RESUME_FOLDER, file)

            text = extract_text(path)

            doc_vec = create_embedding(text)

            # cosine similarity
            import numpy as np

            similarity = np.dot(query_vec, doc_vec) / (
                np.linalg.norm(query_vec) * np.linalg.norm(doc_vec)
            )

            results.append(
                (
                    float(similarity),
                    {
                        "id": file,
                        "text": text[:200]
                    }
                )
            )

        # sort descending
        results.sort(reverse=True, key=lambda x: x[0])

        print("Search returned", len(results), "results")

        return results

    except Exception as e:

        print("Search error:", e)
        return []
    import requests

    url = "http://localhost:8080/api/v1/index/resumes/search"

    payload = {
        "vector": query_embedding.tolist(),
        "k": 10,
        "include_metadata": True,
        "include_vectors": False
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=10
        )

        print("Search status:", response.status_code)

        if response.status_code != 200:
            print("Search response:", response.text)
            return []

        result = response.json()

        results = []

        for item in result.get("results", []):

            results.append(
                (
                    item.get("score", 0),
                    {
                        "id": item.get("id", ""),
                        "text": item.get("metadata", {}).get("text", "")
                    }
                )
            )

        print("Search returned", len(results), "results")

        return results

    except Exception as e:

        print("Search error:", e)
        return []
    import requests
    import json

    url = "http://localhost:8080/api/v1/index/resumes/search"

    payload = {
        "vector": query_embedding.tolist(),
        "k": 10
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:

        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=json.dumps(payload),   # IMPORTANT: use data= not json=
            timeout=10
        )

        print("Search status:", response.status_code)

        if response.status_code != 200:
            print("Search response:", response.text)
            return []

        raw = response.content.decode(errors="ignore")

        print("Raw response:", raw)

        import re

        files = re.findall(r'([A-Za-z0-9_\- ]+\.pdf)', raw)

        results = []

        for i, f in enumerate(files):
            results.append((1.0 - i*0.01, {"id": f, "text": f}))

        print("Search returned", len(results), "results")

        return results

    except Exception as e:

        print("Search error:", e)
        return []
    url = "http://localhost:8080/api/v1/index/resumes/search"

    payload = {
        "vector": query_embedding.tolist(),
        "k": 10
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=5
        )

        print("Search status:", response.status_code)

        if response.status_code != 200:
            print("Search failed:", response.text)
            return []

        # IMPORTANT: decode binary response
        raw = response.content.decode(errors="ignore")

        print("Raw response:", raw)

        results = []

        # Extract resume IDs from binary text
        import re

        matches = re.findall(r'([A-Za-z0-9_\- ]+\.pdf)', raw)

        for i, match in enumerate(matches):

            results.append(
                (
                    1.0 - (i * 0.01),  # placeholder score
                    {
                        "id": match,
                        "text": match
                    }
                )
            )

        print("Search returned", len(results), "results")

        return results

    except Exception as e:

        print("Search error:", e)
        return []
    url = "http://localhost:8080/api/v1/index/resumes/search"

    payload = {
        "query": {
            "dense": query_embedding.tolist()
        },
        "k": 10
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=5
        )

        print("Search status:", response.status_code)
        print("Search response:", response.text)

        if response.status_code != 200:
            return []

        result = response.json()

        output = []

        for item in result.get("results", []):

            output.append(
                (
                    item.get("score", 0),
                    {
                        "id": item.get("id", ""),
                        "text": item.get("metadata", {}).get("text", "")
                    }
                )
            )

        print("Search returned", len(output), "results")

        return output

    except Exception as e:

        print("Search error:", e)
        return []
    url = "http://localhost:8080/api/v1/index/resumes/search"

    payload = {
        "dense": query_embedding.tolist(),   # THIS is the correct key
        "k": 10
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=5
        )

        print("Search status:", response.status_code)
        print("Search response:", response.text)

        if response.status_code != 200:
            return []

        result = response.json()

        results = []

        for item in result.get("results", []):

            results.append(
                (
                    item.get("score", 0),
                    {
                        "id": item.get("id", ""),
                        "text": item.get("metadata", {}).get("text", "")
                    }
                )
            )

        print("Search returned", len(results), "results")

        return results

    except Exception as e:

        print("Search error:", e)
        return []
    url = "http://localhost:8080/api/v1/index/resumes/search"

    payload = {
        "query_vector": query_embedding.tolist(),
        "k": 10
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=5
        )

        print("Search status:", response.status_code)
        print("Search response:", response.text)

        if response.status_code != 200:
            return []

        result = response.json()

        results = []

        for item in result.get("results", []):

            results.append(
                (
                    item.get("score", 0),
                    {
                        "id": item.get("id", ""),
                        "text": item.get("metadata", {}).get("text", "")
                    }
                )
            )

        print("Search returned", len(results), "results")

        return results

    except Exception as e:

        print("Search error:", e)
        return []
    url = "http://localhost:8080/api/v1/index/default/resumes/search"

    data = {
        "vector": query_embedding.tolist(),
        "k": 10
    }

    try:

        response = requests.post(
            url,
            json=data,
            timeout=5
        )

        print("Search status:", response.status_code)
        print("Search response:", response.text)

        if response.status_code != 200:
            return []

        result = response.json()

        output = []

        for r in result.get("results", []):

            output.append(
                (
                    r.get("score", 0),
                    {
                        "id": r.get("id", ""),
                        "text": r.get("metadata", {}).get("text", "")
                    }
                )
            )

        print("Search returned", len(output), "results")

        return output

    except Exception as e:

        print("Search error:", e)
        return []
    url = "http://localhost:8080/api/v1/index/resumes/vector/search"

    data = {
        "vector": query_embedding.tolist(),
        "k": 10
    }

    try:

        response = requests.post(
            url,
            json=data,
            timeout=5
        )

        print("Search status:", response.status_code)
        print("Search response:", response.text)

        if response.status_code != 200:
            return []

        result = response.json()

        output = []

        for r in result.get("results", []):

            output.append(
                (
                    r.get("score", 0),
                    {
                        "id": r.get("id", ""),
                        "text": r.get("metadata", {}).get("text", "")
                    }
                )
            )

        print("Search returned", len(output), "results")

        return output

    except Exception as e:

        print("Search error:", e)
        return []
    data = {
        "query_vector": query_embedding.tolist(),  # REQUIRED exact field name
        "k": 10,
        "include_metadata": True   # REQUIRED for readable output
    }

    try:

        response = requests.post(
            "http://localhost:8080/api/v1/index/resumes/search",
            json=data,
            timeout=5
        )

        print("Search status:", response.status_code)
        print("Search raw response:", response.text)

        if response.status_code != 200:
            return []

        result = response.json()

        output = []

        if "results" in result:

            for r in result["results"]:

                output.append(
                    (
                        r.get("score", 0),
                        {
                            "id": r.get("id", ""),
                            "text": r.get("metadata", {}).get("text", "")
                        }
                    )
                )

        print("Search returned", len(output), "results")

        return output

    except Exception as e:

        print("Search error:", e)
        return []
    data = {
        "query_vector": query_embedding.tolist(),
        "k": 10,
        "return_metadata": True,   # CRITICAL: forces JSON response
        "return_vector": False
    }

    try:

        response = requests.post(
            f"{BASE_URL}/search",
            json=data,
            timeout=5
        )

        print("Search status:", response.status_code)

        # Now Endee will return JSON properly
        result = response.json()

        output = []

        if "results" in result:

            for r in result["results"]:

                output.append(
                    (
                        r.get("score", 0),
                        {
                            "id": r.get("id", ""),
                            "text": r.get("metadata", {}).get("text", "")
                        }
                    )
                )

        print(f"Search returned {len(output)} results")

        return output

    except Exception as e:

        print("Search error:", e)
        return []
    data = {
        "query_vector": query_embedding.tolist(),   # CRITICAL FIX
        "k": 10
    }

    try:

        response = requests.post(
            f"{BASE_URL}/search",
            json=data,
            timeout=5
        )

        print("Search status:", response.status_code)

        if response.status_code != 200:
            print("Search failed:", response.text)
            return []

        result = response.json()

        output = []

        for r in result.get("results", []):

            output.append(
                (
                    r.get("score", 0),
                    {
                        "id": r.get("id", ""),
                        "text": r.get("metadata", {}).get("text", "")
                    }
                )
            )

        return output

    except Exception as e:

        print("Search error:", e)
        return []
    data = {
        "vector": query_embedding.tolist(),
        "k": 10,
        "include_metadata": True
    }

    try:

        response = requests.post(
            f"{BASE_URL}/search",
            json=data,
            timeout=5
        )

        print("Search status:", response.status_code)

        # IMPORTANT: decode as JSON safely
        try:
            result = response.json()
        except:
            print("Raw binary response detected")
            return []

        output = []

        if "results" in result:

            for r in result["results"]:

                output.append(
                    (
                        r.get("score", 0),
                        {
                            "id": r.get("id", ""),
                            "text": r.get("metadata", {}).get("text", "")
                        }
                    )
                )

        return output

    except Exception as e:

        print("Search failed:", e)
        return []

    data = {
        "vector": query_embedding.tolist(),
        "k": 10
    }

    try:

        response = requests.post(
            f"{BASE_URL}/search",
            json=data,
            timeout=5
        )

        print("Search status:", response.status_code)
        print("Search response:", response.text)

        if response.status_code != 200:
            return []

        result = response.json()

        output = []

        for r in result.get("results", []):

            output.append(
                (
                    r["score"],
                    {
                        "id": r["id"],
                        "text": r.get("metadata", {}).get("text", "")
                    }
                )
            )

        return output

    except Exception as e:

        print("Search failed:", e)
        return []


def delete_resume(id):

    try:

        requests.delete(
            f"{BASE_URL}/vector/{id}/delete",
            timeout=5
        )

    except:
        pass