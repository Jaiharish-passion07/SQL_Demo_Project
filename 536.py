from pglet import Button,Stack

from webapp import signup_page
from webapp.signup_page import *

with pglet.page("suffix-prefix-textboxes") as page:
    def button_clicked(e):
        if tb1.value == '':
            tb1.error_message = 'Field is required'
        else:
            tb1.error_message = ''
        if tb2.value == '':
            tb2.error_message = 'Field is required'
        else:
            tb2.error_message = ''
        page.update()

    def button_clicked_(e):
        if tb11.value == '':
            tb11.error_message = 'Field is required'
        else:
            faculty_signup.signup()

        if tb21.value == '':
            tb21.error_message = 'Field is required'
        else:
            tb21.error_message = ''
        page.update()
    tb1 = Textbox(label='Faculty User-Id', required=True)
    tb2 = Textbox(label='Password', password=True, required=True)
    b = Button("Submit", on_click=button_clicked)

    tb11 = Textbox(label='Student User-Id', required=True)
    tb21 = Textbox(label='Password', password=True, required=True)
    b1 = Button("Submit", on_click=button_clicked_)
    faculty_form=Stack(controls=[tb1,tb2,b])
    stu_form = Stack(controls=[tb11, tb21, b1])


    page.add(Stack(horizontal=True,horizontal_align='space-between',controls=[faculty_form,stu_form]))
    input()