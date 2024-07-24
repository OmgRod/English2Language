from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from transformers import MarianMTModel, MarianTokenizer
import torch
import os

# Path to the models directory
models_dir = 'models'

# Load models and tokenizers
model_dict = {}
tokenizer_dict = {}

def load_model_and_tokenizer(lang_code):
    model_path = os.path.join(models_dir, f"opus-mt-en-{lang_code}")
    if lang_code not in model_dict:
        model = MarianMTModel.from_pretrained(model_path)
        tokenizer = MarianTokenizer.from_pretrained(model_path)
        model_dict[lang_code] = model
        tokenizer_dict[lang_code] = tokenizer

@require_http_methods(["GET"])
def translate(request):
    lang_code = request.GET.get('lang')
    text = request.GET.get('text')
    
    if not lang_code or not text:
        return HttpResponse('Please provide both lang and text parameters.', status=400)

    load_model_and_tokenizer(lang_code)

    if lang_code not in model_dict:
        return HttpResponse(f'Model for language {lang_code} not found.', status=404)

    model = model_dict[lang_code]
    tokenizer = tokenizer_dict[lang_code]

    inputs = tokenizer(text, return_tensors='pt')
    
    with torch.no_grad():
        translated_tokens = model.generate(**inputs)
    
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    
    return HttpResponse(translated_text)
