import streamlit as st
from kendra_bedrock_query import kendraSearch

st.markdown("<h1 style='text-align: center; color: red;'>RAG with Amazon Kendra </h1>", unsafe_allow_html=True)


def main():
    if "query_text" not in st.session_state:
        st.session_state["query_text"] = []

    if "query" not in st.session_state:
        st.session_state["query"] = []

    if "past" not in st.session_state:
        st.session_state["past"] = []

    # col1 = st.column([10], gap="medium")
    # with col1:
    with st.container():
        input_text = st.text_input("Ask a question:",
                                   "",
                                   key="query_text",
                                   placeholder="What can I help you with?",
                                   on_change=clear_text()
                                   )
        user_input = st.session_state["query"]

        if user_input:
            st.session_state.past.append(user_input)
            st.write(kendraSearch(user_input))

    with st.container():
        st.button("clear chat", on_click=clear_session)


def clear_text():
    st.session_state["query"] = st.session_state["query_text"]
    st.session_state["query_text"] = ""


def clear_session():
    for key in st.session_state.keys():
        del st.session_state[key]


if __name__ == "__main__":
    main()
