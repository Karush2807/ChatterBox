from django.shortcuts import render
from django.http import HttpResponse
from transformers import TFAutoModelForCausalLM, AutoTokenizer



# Create your views here.

def call_hugguFACE(message):
    model_name = "distilgpt2"  # Or "EleutherAI/gpt-neo-125M" for GPT-Neo
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = TFAutoModelForCausalLM.from_pretrained(model_name)
    
    # Encode the input message
    inputs = tokenizer.encode(message, return_tensors="tf")

    # Generate a response
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1, temperature=0.7)

    # Decode the response
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer


    

def chatbot(request):
    user_message = None
    ai_response = "Hi, I am your AI Chatbot, you can ask me anything."  # Default AI response
    
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        # Process the user's message and generate AI response here
        ai_response = call_hugguFACE(user_message)

        
    return render(request, 'bot_chat.html', {'user_message': user_message, 'ai_response': ai_response})