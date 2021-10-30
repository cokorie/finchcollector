from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'Java Sparrow', 'Speed Demon', 0),
  Finch('Sachi', 'Gouldian', 'Free Spirit', 6),
  Finch('Raven', 'Bengalese', 'Spotted Beek', 3)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })