# views.py
from django.shortcuts import render, redirect
from .models import Obituary

def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST['author']
        slug = f"{name.lower().replace(' ', '-')}-{date_of_death}"

        try:
            obituary = Obituary.objects.create(
                name=name,
                date_of_birth=date_of_birth,
                date_of_death=date_of_death,
                content=content,
                author=author,
                slug=slug
            )
            obituary.save()
            return redirect('view_obituaries')
        except Exception as e:
            # Handle any errors that occur during data submission
            print(f"Error saving obituary: {e}")
            return render(request, 'obituary_form.html', {'error': 'An error occurred while submitting the obituary.'})

    return render(request, 'obituary_form.html')