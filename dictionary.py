from jinja2 import Template
person={('name'):'Alex',('Gender'):'Male'}
tm=Template('My name is {{per.name}} and I identify myself as {{per.Gender}}')
msg=tm.render(per=person)
print(msg)
