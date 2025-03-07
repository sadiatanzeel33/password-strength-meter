import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    return strength

def main():
    st.title("Password Strength Meter")

    password = st.text_input("Enter your password", type="password")
    if password:
        strength = check_password_strength(password)
        st.write(f"Password strength: {strength}/5")

        if strength == 5:
            st.success("Your password is very strong!")
        elif strength >= 3:
            st.info("Your password is moderate.")
        else:
            st.warning("Your password is weak.")

if __name__ == "__main__":
    main()
