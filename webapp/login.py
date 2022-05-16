from pglet import Button,Stack
from webapp.signup_page import *


with pglet.page("Management") as page:
    page.theme_primary_color = '#6714b5'
    page.theme_text_color = '#091382'
    page.theme_background_color = '#daf035'
    page.update()

    class display_login():
        def __init__(self,user):
            self.task=[]
            self.user=user
            self.tb1 = Textbox(label=self.user, required=True,align='center')
            self.tb2 = Textbox(label='Password', password=True, required=True,align='center')
            self.b = Button("Submit", on_click=self.button_clicked,primary=True)
            self.view = Stack(padding=100,border_style='dashed',border_color='black',width='40%',border_radius=10,controls=[self.tb1, self.tb2, self.b])


        def button_clicked(self,e):
            if self.tb1.value == '':
                self.tb1.error_message = 'Field is required'
            else:
                self.task.append(self.tb1.value)
                self.tb1.error_message = ''
            if self.tb2.value == '':
                self.tb2.error_message = 'Field is required'
            else:
                self.task.append(self.tb2.value)
                self.tb2.error_message = ''

            if self.tb1.value!='' and self.tb2.value!='':
                if self.user=="Faculty User-Id":
                    signup_display(label="Faculty Name")
                    #page.disabled(True)
                elif self.user=="Student -Id":
                    signup_display(label="Student Name")
                    #page.disabled(True)

            self.view.update()

    # create application instance
    app1 =display_login("Faculty User-Id")
    app2=display_login("Student -Id")
    # add application's root control to the page
    page.add(Stack(padding=100,horizontal=True,border_style='solid',border_color='black',horizontal_align='space-evenly',width='100%',controls=[app1.view,app2.view]))
    input()




