from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, BookShop

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def hw_31(request):
    return render(request, "hw_31.html")

def hw_31_1(request):
    return render(request, "hw_31_1.html")

def hw_31_2(request):
    return render(request, "hw_31_2.html")

def books(request):
    books_list = BookShop.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    text = form["book_text"]
    avtor = form["book_author"]
    cost = form["book_price"]
    book = BookShop(title=text, author=avtor, price=cost)
    book.save()
    return redirect(books)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def delete_books(request, id):
    book = BookShop.objects.get(id=id)
    book.delete()
    return redirect(books)