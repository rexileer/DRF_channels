from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from llama_cpp import Llama

# Загрузка модели
# llm = Llama(model_path="./llama-2-7b-chat.ggmlv3.q4_0.bin", n_ctx=2048, use_mlock=True, n_threads=8)

# class LLMChatAPIView(APIView):
#     """
#     Эндпоинт для работы с LLaMA через GROQ.
#     """
#     def post(self, request, *args, **kwargs):
#         user_message = request.data.get("message")
#         if not user_message:
#             return Response({"error": "Message is required."}, status=400)
        
#         response = llm(user_message, max_tokens=200, stop=["\n"])
#         llm_response = response['choices'][0]['text'].strip()
        
#         return Response({"response": llm_response})

def llm_response(request):
    return render(request, "llm/response.html")