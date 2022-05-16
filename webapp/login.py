from pglet import Button,Stack


from webapp.stu_sign_up import *
from webapp.faculty_signup import *


with pglet.page("Management") as page:
    class display_login():
        def __init__(self,user):
            self.task=[]
            self.user=user
            self.tb1 = Textbox(label=self.user, required=True)
            self.tb2 = Textbox(label='Password', password=True, required=True)
            self.b = Button("Submit", on_click=self.button_clicked)
            self.view = Stack(controls=[self.tb1, self.tb2, self.b])


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
                    staff_signup()
                elif self.user=="Student -Id":
                    student_signup()

            self.view.update()

    # create application instance
    app1 =display_login("Faculty User-Id")
    app2=display_login("Student -Id")
    # add application's root control to the page
    page.add(Stack(horizontal=True,horizontal_align = "start",controls=[app1.view,app2.view]))
    input()



