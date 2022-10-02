import streamlit as st

st.header("Login")

username_="admin"#username used
password_="password"#password used

with st.form("Login"):
    username=st.text_input("Enter Username")
    password=st.text_input("Enter Password",type='password')
    submit=st.form_submit_button("Login")

    if submit:
        if username!="admin":
            st.write("Username is not 'admin'")
        elif len(password)>8 or len(password)<8:
            st.write("The length of password is not 8")
        elif password[0]!='p':
            st.write("Password wrong in the zeroth index")
        elif password[1]!='a':
            st.write("Password wrong in the first index")
        elif password[2]!='s':
            st.write("Password wrong in the second index")
        elif password[3]!='s':
            st.write("Password wrong in the third index")
        elif password[4]!='w':
            st.write("Password wrong in the fourth index")
        elif password[5]!='o':
            st.write("Password wrong in the fifth index")
        elif password[6]!='r':
                st.write("Password wrong in the sixth index")
        elif password[7]!='d':
                st.write("Password wrong in the seventh index")
        else:
            st.write("The Flag is '_CTF'")