from jinja2 import Template

t= Template("hello {{something}}!")
print(t.render(something="world"))

t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
print(t.render())
