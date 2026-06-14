import streamlit as st
from google import genai
from google.genai import types
import io

# 1. Setup Page Configuration
st.set_page_config(page_title="My Glitter Dash", page_icon="✨", layout="wide")

# 2. Background Wallpaper Injector Function
def add_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        /* Applies the wallpaper to the entire application background */
        .stApp {{
            background-image: url("{image_url}");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }}
        
        /* Gives chat text bubbles a clean backdrop so they stay readable */
        .stChatMessage {{
            background-color: rgba(255, 255, 255, 0.6) !important;
            border-radius: 15px;
            padding: 10px;
            margin-bottom: 10px;
        }}
        
        /* Makes the chat input bar stand out over the wallpaper */
        .stChatInputContainer {{
            background-color: rgba(255, 255, 255, 0.8) !important;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 3. Activate the Background Wallpaper
wallpaper_url = "https://cdn.displate.com/artwork/270x380/2026-02-18/d0420264-cf3c-4aaa-b85f-afdf1531f3e4.jpg"

add_bg_from_url(wallpaper_url)

# 4. App Title
st.title("✨ My Glitter Dash")

# 5. Configure Unified Gemini API Client
# ⚠️ REPLACE WITH YOUR NEW API KEY FROM GOOGLE AI STUDIO
API_KEY = "My API Key"
client = genai.Client(api_key=API_KEY)


# 6. Sidebar: Document & Image Generation Tools
st.sidebar.header("🎨 Creation Station")

# --- DOCUMENT GENERATION SECTION ---
st.sidebar.subheader("📄 Export Document")
doc_title = st.sidebar.text_input("Document Title", "Glitter Dash Notes")
doc_content = st.sidebar.text_area("Document Content", "Type or paste what you want to save...")

if st.sidebar.button("Generate & Download Doc"):
    # Create a simple text file format structure
    full_doc = f"=== {doc_title} ===\n\n{doc_content}"
    
    # Provide the download button
    st.sidebar.download_button(
        label="📥 Download Text File",
        data=full_doc,
        file_name=f"{doc_title}.txt",
        mime="text/plain"
    )

# --- IMAGE GENERATION SECTION ---
st.sidebar.subheader("🖼Generate Image")
image_prompt = st.sidebar.text_input("Describe the image you want:", "A sparkly unicorn jumping over a rainbow")

if st.sidebar.button("✨ Create Image"):
    with st.sidebar.spinner("Generating magic..."):
        try:
            # Using the official modern client format for image generation
            result = client.models.generate_images(
                model='imagen-4.0-generate-002',
                prompt=image_prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio="1:1"
                )
            )
            
            # Extract raw image bytes from the response object
            generated_image = result.generated_images[0]
            image_bytes = generated_image.image.image_bytes
            
            # Display the image in the sidebar
            st.sidebar.image(image_bytes, caption=image_prompt)
            
            # Add a download button for the generated image
            st.sidebar.download_button(
                label="📥 Download Image",
                data=image_bytes,
                file_name="glitter_dash_image.png",
                mime="image/png"
            )
        except Exception as e:
            st.sidebar.error(f"Could not generate image: {e}")
            st.sidebar.info("💡 Note: Image generation may require a paid/tier-1 billing account attached to your Google AI Studio project.")


# 7. Main Chatbot Interface
st.subheader("💬 Chat with My Glitter Dash")

# Initialize chat history memory store
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user chat input
if chat_prompt := st.chat_input("Say something sparkly..."):
    # Display user message on screen
    st.session_state.messages.append({"role": "user", "content": chat_prompt})
    with st.chat_message("user"):
        st.markdown(chat_prompt)

    # Generate and display AI response using the text model
    with st.spinner("Thinking..."):
        try:
            # Using the modern client syntax for text generation
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=chat_prompt,
            )
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error communicating with Gemini: {e}")
