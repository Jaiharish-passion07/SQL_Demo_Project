import pglet
from pglet import Button,Textbox,Dropdown,dropdown,Stack
with pglet.page("buttons-with-icons") as page:
    name = Textbox(label='Student Name')
    stu_id = Textbox(label='Student Id', required=True)
    dept_name = Dropdown(label='Department Name', placeholder='Select Your Department', options=[
        dropdown.Option('Mechanical Dept'),
        dropdown.Option('Computer Science Dept'),
        dropdown.Option('Data Science Dept')])
    def button_clicked(e):
        stu_add_b.data += 1
        view1 = Stack(controls=[name, stu_id, dept_name])
        page.add(view1)
        page.update()
    stu_add_b=Button("Add Student", icon='AddFriend',on_click=button_clicked,data=0,primary=True)
    page.add(stu_add_b)

    # stu_add_subj=Button("Add Subject", icon='Add', primary=True)
    # sub_name = Dropdown(label='Subject Name', placeholder='Select Your Subject', options=[
    #     dropdown.Option('Subject1'),
    #     dropdown.Option('Subject2'),
    #     dropdown.Option('Subject3')])
    # page.add(Stack(horizontal=True,controls=[view1,stu_add_subj,sub_name]))
    input()