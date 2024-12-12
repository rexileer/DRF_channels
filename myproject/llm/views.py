from django.shortcuts import render

# Create your views here.
def llm_response(request):
    return render(request, 'llm/response.html')