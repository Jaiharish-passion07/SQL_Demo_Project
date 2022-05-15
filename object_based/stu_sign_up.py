import pglet
from pglet import Textbox,Dropdown, dropdown,DatePicker
from datetime import datetime

def student_signup():
    with pglet.page("student_sign") as student_signup_page:
        now = datetime.now()
        name = Textbox(label='Student Name')
        email_id= Textbox(label='Email-Id',suffix="@gmail.com")
        stu_id= Textbox(label='Student Id',required=True)
        phone_no = Textbox(label='Phone Number', required=True)
        address=Textbox(label='Address', multiline=True, auto_adjust_height=True)
        pawd = Textbox(label='Password', password=True, required=True)
        rpwad=Textbox(label='Re-Enter Password', password=True, required=True)
        dept_name=Dropdown(label='Department Name', placeholder='Select Your Department', options=[
            dropdown.Option('Mechanical Dept'),
            dropdown.Option('Computer Science Dept'),
            dropdown.Option('Data Science Dept')])
        dob = DatePicker(label="Start date", value=now, width=150)

        return student_signup_page.add(name,email_id,stu_id,phone_no,address,pawd,rpwad,dept_name,dob)


