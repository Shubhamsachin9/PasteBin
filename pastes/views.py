from django.shortcuts import render, redirect, get_object_or_404
from .models import Paste

def home(request):
    new_paste = None

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            new_paste = Paste.objects.create(content=content)

    pastes = Paste.objects.order_by('-created_at')[:10]
    return render(request, 'paste/home.html', {
        'pastes': pastes,
        'new_paste': new_paste
    })

def paste_edit(request, pk):
    paste = get_object_or_404(Paste, pk=pk)
    if request.method == "POST":
        paste.content = request.POST.get("content")
        paste.save()
        return redirect('home')
    return render(request, 'paste/paste_form.html', {'paste': paste})

def paste_delete(request, pk):
    paste = get_object_or_404(Paste, pk=pk)
    paste.delete()
    return redirect('home')
