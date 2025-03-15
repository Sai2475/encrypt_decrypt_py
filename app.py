import gradio as gr
from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encryption 
def encrypt_text(text: str) -> str:
    if not text:
        return "Error: Please enter text to encrypt!"
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text.decode()

# Decryption 
def decrypt_text(encrypted_text: str) -> str:
    try:
        decrypted_text = cipher_suite.decrypt(encrypted_text.encode())
        return decrypted_text.decode()
    except:
        return "Error: Invalid encrypted text!"

#CSS 
custom_css = """
<style>
    body { 
        background: url('https://source.unsplash.com/1600x900/?technology,security') no-repeat center center fixed; 
        background-size: cover;
        font-family: Arial, sans-serif;
    }
    #title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: white;
        padding: 15px;
        background: rgba(0, 0, 0, 0.7);
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .gradio-container {
        max-width: 600px;
        margin: auto;
    }
</style>
"""

# Gradio UI
with gr.Blocks() as demo:
    gr.HTML(custom_css)  # Injecting CSS
    gr.Markdown("# 🔐 Secure Text Encryption & Decryption", elem_id="title")
    
    with gr.Tab("Encrypt"):
        gr.Markdown("### 🔏 Encrypt your text securely")
        text_input = gr.Textbox(label="Enter text to encrypt", placeholder="Type here...")
        encrypt_button = gr.Button("Encrypt 🔒", variant="primary")
        encrypted_output = gr.Textbox(label="Encrypted Text", interactive=False, placeholder="Your encrypted text will appear here.")
        encrypt_button.click(encrypt_text, inputs=text_input, outputs=encrypted_output)
    
    with gr.Tab("Decrypt"):
        gr.Markdown("### 🔓 Decrypt your text")
        encrypted_input = gr.Textbox(label="Enter encrypted text", placeholder="Paste encrypted text here...")
        decrypt_button = gr.Button("Decrypt 🔑", variant="secondary")
        decrypted_output = gr.Textbox(label="Decrypted Text", interactive=False, placeholder="Your decrypted text will appear here.")
        decrypt_button.click(decrypt_text, inputs=encrypted_input, outputs=decrypted_output)

demo.launch()
