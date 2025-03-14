import streamlit as st
import encrypt 

# Streamlit UI
st.title("🔐 Text Encryption & Decryption App")
st.write("This app encrypts and decrypts messages using a random substitution cipher.")

# Encryption 
st.header("🔹 Encrypt a Message")
plain_text = st.text_input("Enter a message to encrypt")
if st.button("Encrypt"):
    if plain_text:
        encrypted_text = encrypt.encrypt(plain_text)  #function from encryption.py
        st.success(f"🔑 Encrypted Message: {encrypted_text}")
    else:
        st.warning("Please enter text to encrypt.")

# Decryption 
st.header("🔹 Decrypt a Message")
cipher_text = st.text_input("Enter a message to decrypt")
if st.button("Decrypt"):
    if cipher_text:
        decrypted_text = encrypt.decrypt(cipher_text)  #function from encryption.py
        st.success(f"🔓 Original Message: {decrypted_text}")
    else:
        st.warning("Please enter text to decrypt.")

st.markdown("---")
st.markdown("💡 **Note:** This encryption method is simple and not secure for real-world use.")
