import streamlit as st
import requests

st.title("RAG PDF CHAT")
query =st.text_input("Ask a question:")
if st.button("Ask"):
    if query.strip():
        response = requests.post(
            "http://localhost:8000/ask",
            json = {"query":query}
        )
        data = response.json()
        
        st.write("### Answer")
        st.write(data.get("answer"))

        st.write("### Sources")
        for s in data.get("sources",[]):
            st.write(f"{s["sources"]} - Pages: {s["pages"]}")

else:
    st.warning("Enter a valid question")