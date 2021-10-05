from jinja2 import Template

data = '''
{% raw %} 
My name is {{ name }}
{% endraw %}
'''
tm = Template(data)
msg = tm.render(name='Alex')
print(msg)
