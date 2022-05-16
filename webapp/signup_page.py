import pglet
from pglet import Textbox,Dropdown, dropdown,DatePicker,Stack
from datetime import datetime


def signup_display(label):
    with pglet.page("staff_sign") as student_signup_page:
        student_signup_page.theme_primary_color = '#6714b5'
        student_signup_page.theme_text_color = '#091382'
        student_signup_page.theme_background_color = '#daf035'
        student_signup_page.update()
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

            layout1_faculty = Stack(padding=100,border_style='dashed',border_color='black',width='40%',border_radius=10,controls=[name,email_id,fac_id,fac_role,phone_no])
            layout2_faculty = Stack(padding=100,border_style='dashed',border_color='black',width='40%',border_radius=10,controls=[address,pawd,rpwad,dept_name,dob])
            return student_signup_page.add(Stack(padding=100,horizontal=True,border_style='solid',border_color='black',horizontal_align='space-evenly',width='100%',controls=[layout1_faculty,layout2_faculty]))
        if label=="Student Name":
            stu_id = Textbox(label='Student Id', required=True)
            name = Textbox(label='Student Name')

            layout1_stu = Stack(padding=100,border_style='dashed',border_color='black',width='40%',border_radius=10,controls=[name, email_id, stu_id, phone_no])
            layout2_stu = Stack(padding=100,border_style='dashed',border_color='black',width='40%',border_radius=10,controls=[address, pawd, rpwad, dept_name, dob])

            return student_signup_page.add(Stack(padding=100,horizontal=True,border_style='solid',border_color='black',horizontal_align='space-evenly',width='100%',controls=[layout1_stu,layout2_stu]))

        input()
