from jinja2 import Template
age=28
name='Billy'
tm=Template('Hello {{name}} and i want to remind you that you are {{age}} right now!!' )
msg=tm.render(name=name,age=age)
print(msg)