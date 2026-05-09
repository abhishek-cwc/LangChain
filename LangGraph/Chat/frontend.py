import streamlit as st
#from backend import workflow
from backend_ai import workflow
import uuid
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage

################### helper ################

def genrate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = genrate_thread_id()
    add_thread(thread_id)
    st.session_state.thread_id = thread_id
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)  

def load_conversation(thread_id):
    config = {"configurable": {"thread_id": thread_id}}
    st.session_state['thread_id'] = thread_id
    result = workflow.get_state(config=config)
    return result.values



################## setup message ##########
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    thread_id = genrate_thread_id()
    st.session_state['thread_id'] = thread_id

if 'chat_threads' not in  st.session_state:
    st.session_state['chat_threads'] = []


add_thread(st.session_state['thread_id'])

##### ##################  Sidebar #####################

st.sidebar.title('Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header("Recents")

for thread_id in st.session_state['chat_threads']:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        tmp_message = []


        for msg in messages['message']:
            if isinstance(msg, HumanMessage):
                role = 'User'
            else:
                role = 'Ai'
            
            tmp_message.append({'role': role, 'content': msg.content})
  
        st.session_state['message_history'] = tmp_message

    #st.sidebar.text(thread_id)


for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])
            
 
user_input = st.chat_input('Type here')

config = {"configurable": {"thread_id": st.session_state['thread_id']}}

if user_input:
    st.session_state['message_history'].append({'role': 'User', 'content': user_input})
    with st.chat_message("User"):
        st.text(user_input)

    result = workflow.invoke({'message': user_input}, config=config)
    ai_message = result['message'][-1].content

    st.session_state['message_history'].append({'role': 'AI', 'content': ai_message})
    with st.chat_message("AI"):
        st.text(ai_message)     


