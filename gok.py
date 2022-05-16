import streamlit as st

# #Signup page faculty container
# def signup_facul_page():
#     login_page.empty()
#     signup_faculty_page=st.empty()
#
#     with signup_faculty_page.container():
#         st.title("Faculty Sign-Up Page ")
#         col1, col2 = st.columns(2)
#         with col1:
#             name = col1.text_input("Name:",placeholder="Enter your name")
#             phone_no=col1.text_input("Phone Numer:",placeholder="Enter your Phone Number")
#             email_id=col1.text_input("Email-Id:",placeholder="Enter your Email_Id")
#             address=col1.text_area("Address:",placeholder="Enter Address")
#             faculty_id_signup=col1.text_input("Faulty-Id:",placeholder="Enter Faculty ID")
#
#         with col2:
#
#             dept_name = col2.selectbox(
#                 'Select Your Department',
#                 ('Mechanical Dept','Electronics Dept','Data Science Dept','Computer Science Dept'))
#
#             faculty_role = col2.selectbox(
#                 'Select Your Role',
#                 ('Senior Professor','Assistant Professor','HOD','Technicain'))
#             fac_signup_pwd = col2.text_input("Password", type='password', placeholder="Enter Password", key="<uniquevalueofsomesort>")
#             fac_signup_pwd_renter = col2.text_input("", type='password', placeholder="Re-Enter Password",
#                                                     key="<uniquevalueofsomesort>")

#Signup page student container

# def signup_stu_page():
#     login_page.empty()
#     signup_student_page=st.empty()
#
#     with signup_student_page.container():
#         st.title("Student Sign-Up Page")
#         col1_, col2_ = st.columns(2)
#         with col1_:
#             stu_name = col1_.text_input("Name:",placeholder="Enter your name")
#             stu_phone_no=col1_.text_input("Phone Numer:",placeholder="Enter your Phone Number")
#             stu_email_id=col1_.text_input("Email-Id:",placeholder="Enter your Email_Id")
#             stu_address=col1_.text_area("Address:",placeholder="Enter Address")
#             stu_faculty_id_signup=col1_.text_input("Faulty-Id:",placeholder="Enter Student ID")
#
#         with col2_:
#
#             stu_dept_name = col2_.selectbox(
#                 'Select Your Department',
#                 ('Mechanical Dept','Electronics Dept','Data Science Dept','Computer Science Dept'))
#
#             stu_signup_pwd = col2_.text_input("Password", type='password', placeholder="Enter Password", key="<uniquevalueofsomesort>")
#             stu_signup_pwd_renter = col2_.text_input("", type='password', placeholder="Re-Enter Password",
#                                                     key="<uniquevalueofsomesort>")

def signup_facul_page():
    st.write("Hello")

def signup_stu_page():
    st.write("OMGG")


#Login page container

login_page=st.empty()
with login_page.container():
    st.title("Login Page")
    col1, col2 = st.columns(2)

    with col1:
        faculty_id = col1.text_input("Faculty ID", type='default', placeholder="Enter Faculty ID or Email-Id:")
        faculty_pwd= col1.text_input("Password",type='password',placeholder="Enter Password")
        signup_facul_button=col1.button("Clik to Sign-up as Faculty")
        if signup_facul_button:
            login_page.empty()
            signup_facul_page()
        else:pass

    with col2:
        stu_id = col2.text_input("Student ID", type='default', placeholder="Enter Student ID or Email-Id:")
        stu_pwd = col2.text_input("Password", type='password', placeholder="Enter Password",key="<uniquevalueofsomesort>")
        signup_stu_button=col2.button("Clik to Sign-up as Student")
        if signup_stu_button:
            login_page.empty()
            signup_stu_button()
        else:pass

