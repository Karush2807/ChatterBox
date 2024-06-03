from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def chatbot(request):
    user_message = None
    ai_response = "Hi, I am your AI Chatbot, you can ask me anything."  # Default AI response
    
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        # Process the user's message and generate AI response here
        ai_response = "This is the AI's response to: " + user_message

        
    return render(request, 'bot_chat.html', {'user_message': user_message, 'ai_response': ai_response})