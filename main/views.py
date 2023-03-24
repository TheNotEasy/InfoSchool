from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html', {'index': True, 'range31': range(1, 32), 'user': request.user})
