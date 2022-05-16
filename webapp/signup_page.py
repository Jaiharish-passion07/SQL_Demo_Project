import pglet
from pglet import Textbox,Dropdown, dropdown,DatePicker
from datetime import datetime


def signup_display(label):
    with pglet.page("staff_sign") as student_signup_page:
        now = datetime.now()
        email_id= Textbox(label='Email-Id',suffix="@gmail.com")
        phone_no = Textbox(label='Phone Number', required=True)
        address=Textbox(label='Address', multiline=True, auto_adjust_height=True)
        pawd = Textbox(label='Password', password=True, required=True)
        rpwad=Textbox(label='Re-Enter Password', password=True, required=True)
        dept_name=Dropdown(label='Department Name', placeholder='Select Your Department', options=[
            dropdown.Option('Mechanical Dept'),
            dropdown.Option('Computer Science Dept'),
            dropdown.Option('Data Science Dept')])

        dob = DatePicker(label="Start date", value=now, width=150)

        if label=="Faculty Name":
            fac_id = Textbox(label='Faculty Id', required=True)
            name = Textbox(label='Faculty Name')
            fac_role = Dropdown(label='Faculty Role', placeholder='Select Your Role', options=[
                dropdown.Option('Head of Dept'),
                dropdown.Option('Senior Professor'),
                dropdown.Option('Assistant Professor'), dropdown.Option('Technician')])

            return student_signup_page.add(name,email_id,fac_id,fac_role,phone_no,address,pawd,rpwad,dept_name,dob)
        if label=="Student Name":
            stu_id = Textbox(label='Student Id', required=True)
            name = Textbox(label='Student Name')

            return student_signup_page.add(name,email_id,stu_id,phone_no,address,pawd,rpwad,dept_name,dob)

