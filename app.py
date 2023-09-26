import streamlit as st
from kendra_bedrock_query import kendraSearch

st.markdown("<h1 style='text-align: center; color: red;'>RAG with Amazon Kendra </h1>", unsafe_allow_html=True)

def main():
    # configuring default values for session state
    if "query_text" not in st.session_state:
        st.session_state["query_text"] = []

    if "query" not in st.session_state:
        st.session_state["query"] = []

    if "past" not in st.session_state:
        st.session_state["past"] = []

    with st.container():
        # primary container that has text input box
        input_text = st.text_input("Ask a question:",
                                   "",
                                   key="query_text",
                                   placeholder="What can I help you with?",
                                   on_change=clear_text()
                                   )
        # if the user inputs a question change the session state
        user_input = st.session_state["query"]

        if user_input:
            # after the user inputs a question, append it to the session state
            st.session_state.past.append(user_input)
            # pass that question into the Kendra Search function located in the kendra_bedrock_query.py file
            st.write(kendraSearch(user_input))
    # clear chat button
    with st.container():
        st.button("clear chat", on_click=clear_session)
#  this function clears all of the text
def clear_text():
    st.session_state["query"] = st.session_state["query_text"]
    st.session_state["query_text"] = ""

# This function clears all of the data from the session
def clear_session():
    for key in st.session_state.keys():
        del st.session_state[key]


if __name__ == "__main__":
    main()
