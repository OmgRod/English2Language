from transformers import MarianMTModel, MarianTokenizer
import os

# Define model names
models = {
    'ru': 'Helsinki-NLP/opus-mt-en-ru',
    'de': 'Helsinki-NLP/opus-mt-en-de',
    'ha': 'Helsinki-NLP/opus-mt-en-ha',
    'hu': 'Helsinki-NLP/opus-mt-en-hu',
    'mt': 'Helsinki-NLP/opus-mt-en-mt',
    'mul': 'Helsinki-NLP/opus-mt-en-mul',
    'celtic': 'Helsinki-NLP/opus-mt-en-CELTIC',
    'romance': 'Helsinki-NLP/opus-mt-en-ROMANCE',
    'aav': 'Helsinki-NLP/opus-mt-en-aav',
    'af': 'Helsinki-NLP/opus-mt-en-af',
    'afa': 'Helsinki-NLP/opus-mt-en-afa',
    'alv': 'Helsinki-NLP/opus-mt-en-alv',
    'ar': 'Helsinki-NLP/opus-mt-en-ar',
    'az': 'Helsinki-NLP/opus-mt-en-az',
    'bat': 'Helsinki-NLP/opus-mt-en-bat',
    'bcl': 'Helsinki-NLP/opus-mt-en-bcl',
    'bem': 'Helsinki-NLP/opus-mt-en-bem',
    'ber': 'Helsinki-NLP/opus-mt-en-ber',
    'bg': 'Helsinki-NLP/opus-mt-en-bg',
    'bi': 'Helsinki-NLP/opus-mt-en-bi',
    'bnt': 'Helsinki-NLP/opus-mt-en-bnt',
    'bzs': 'Helsinki-NLP/opus-mt-en-bzs',
    'ca': 'Helsinki-NLP/opus-mt-en-ca',
    'ceb': 'Helsinki-NLP/opus-mt-en-ceb',
    'cel': 'Helsinki-NLP/opus-mt-en-cel',
    'chk': 'Helsinki-NLP/opus-mt-en-chk',
    'cpf': 'Helsinki-NLP/opus-mt-en-cpf',
    'cpp': 'Helsinki-NLP/opus-mt-en-cpp',
    'crs': 'Helsinki-NLP/opus-mt-en-crs',
    'cs': 'Helsinki-NLP/opus-mt-en-cs',
    'cus': 'Helsinki-NLP/opus-mt-en-cus',
    'cy': 'Helsinki-NLP/opus-mt-en-cy',
    'da': 'Helsinki-NLP/opus-mt-en-da',
    'dra': 'Helsinki-NLP/opus-mt-en-dra',
    'ee': 'Helsinki-NLP/opus-mt-en-ee',
    'efi': 'Helsinki-NLP/opus-mt-en-efi',
    'el': 'Helsinki-NLP/opus-mt-en-el',
    'eo': 'Helsinki-NLP/opus-mt-en-eo',
    'es': 'Helsinki-NLP/opus-mt-en-es',
    'et': 'Helsinki-NLP/opus-mt-en-et',
    'eu': 'Helsinki-NLP/opus-mt-en-eu',
    'eun': 'Helsinki-NLP/opus-mt-en-euq',
    'fi': 'Helsinki-NLP/opus-mt-en-fi',
    'fiu': 'Helsinki-NLP/opus-mt-en-fiu',
    'fj': 'Helsinki-NLP/opus-mt-en-fj',
    'fr': 'Helsinki-NLP/opus-mt-en-fr',
    'ga': 'Helsinki-NLP/opus-mt-en-ga',
    'gaa': 'Helsinki-NLP/opus-mt-en-gaa',
    'gem': 'Helsinki-NLP/opus-mt-en-gem',
    'gil': 'Helsinki-NLP/opus-mt-en-gil',
    'gl': 'Helsinki-NLP/opus-mt-en-gl',
    'gmq': 'Helsinki-NLP/opus-mt-en-gmq',
    'gmw': 'Helsinki-NLP/opus-mt-en-gmw',
    'grk': 'Helsinki-NLP/opus-mt-en-grk',
    'guw': 'Helsinki-NLP/opus-mt-en-guw',
    'gv': 'Helsinki-NLP/opus-mt-en-gv',
    'he': 'Helsinki-NLP/opus-mt-en-he',
    'hi': 'Helsinki-NLP/opus-mt-en-hi',
    'hil': 'Helsinki-NLP/opus-mt-en-hil',
    'ho': 'Helsinki-NLP/opus-mt-en-ho',
    'ht': 'Helsinki-NLP/opus-mt-en-ht',
    'hy': 'Helsinki-NLP/opus-mt-en-hy',
    'id': 'Helsinki-NLP/opus-mt-en-id',
    'ig': 'Helsinki-NLP/opus-mt-en-ig',
    'iir': 'Helsinki-NLP/opus-mt-en-iir',
    'ilo': 'Helsinki-NLP/opus-mt-en-ilo',
    'inc': 'Helsinki-NLP/opus-mt-en-inc',
    'ine': 'Helsinki-NLP/opus-mt-en-ine',
    'is': 'Helsinki-NLP/opus-mt-en-is',
    'iso': 'Helsinki-NLP/opus-mt-en-iso',
    'it': 'Helsinki-NLP/opus-mt-en-it',
    'itc': 'Helsinki-NLP/opus-mt-en-itc',
    'jap': 'Helsinki-NLP/opus-mt-en-jap',
    'kg': 'Helsinki-NLP/opus-mt-en-kg',
    'kj': 'Helsinki-NLP/opus-mt-en-kj',
    'kqn': 'Helsinki-NLP/opus-mt-en-kqn',
    'kwn': 'Helsinki-NLP/opus-mt-en-kwn',
    'kwy': 'Helsinki-NLP/opus-mt-en-kwy',
    'lg': 'Helsinki-NLP/opus-mt-en-lg',
    'ln': 'Helsinki-NLP/opus-mt-en-ln',
    'loz': 'Helsinki-NLP/opus-mt-en-loz',
    'lu': 'Helsinki-NLP/opus-mt-en-lu',
    'lua': 'Helsinki-NLP/opus-mt-en-lua',
    'lue': 'Helsinki-NLP/opus-mt-en-lue',
    'lun': 'Helsinki-NLP/opus-mt-en-lun',
    'luo': 'Helsinki-NLP/opus-mt-en-luo',
    'lus': 'Helsinki-NLP/opus-mt-en-lus',
    'map': 'Helsinki-NLP/opus-mt-en-map',
    'mfe': 'Helsinki-NLP/opus-mt-en-mfe',
    'mg': 'Helsinki-NLP/opus-mt-en-mg',
    'mh': 'Helsinki-NLP/opus-mt-en-mh',
    'mk': 'Helsinki-NLP/opus-mt-en-mk',
    'mkh': 'Helsinki-NLP/opus-mt-en-mkh',
    'ml': 'Helsinki-NLP/opus-mt-en-ml',
    'mos': 'Helsinki-NLP/opus-mt-en-mos',
    'mr': 'Helsinki-NLP/opus-mt-en-mr',
    'ng': 'Helsinki-NLP/opus-mt-en-ng',
    'nic': 'Helsinki-NLP/opus-mt-en-nic',
    'niu': 'Helsinki-NLP/opus-mt-en-niu',
    'nl': 'Helsinki-NLP/opus-mt-en-nl',
    'nso': 'Helsinki-NLP/opus-mt-en-nso',
    'ny': 'Helsinki-NLP/opus-mt-en-ny',
    'nyk': 'Helsinki-NLP/opus-mt-en-nyk',
    'om': 'Helsinki-NLP/opus-mt-en-om',
    'pag': 'Helsinki-NLP/opus-mt-en-pag',
    'pap': 'Helsinki-NLP/opus-mt-en-pap',
    'phi': 'Helsinki-NLP/opus-mt-en-phi',
    'pis': 'Helsinki-NLP/opus-mt-en-pis',
    'pon': 'Helsinki-NLP/opus-mt-en-pon',
    'poz': 'Helsinki-NLP/opus-mt-en-poz',
    'ro': 'Helsinki-NLP/opus-mt-en-ro',
    'ru': 'Helsinki-NLP/opus-mt-en-ru',
    'rw': 'Helsinki-NLP/opus-mt-en-rw',
    'sg': 'Helsinki-NLP/opus-mt-en-sg',
    'sk': 'Helsinki-NLP/opus-mt-en-sk',
    'sm': 'Helsinki-NLP/opus-mt-en-sm',
    'sn': 'Helsinki-NLP/opus-mt-en-sn',
    'sq': 'Helsinki-NLP/opus-mt-en-sq',
    'st': 'Helsinki-NLP/opus-mt-en-st',
    'sw': 'Helsinki-NLP/opus-mt-en-sw',
    'tl': 'Helsinki-NLP/opus-mt-en-tl',
    'tn': 'Helsinki-NLP/opus-mt-en-tn',
    'to': 'Helsinki-NLP/opus-mt-en-to',
    'tw': 'Helsinki-NLP/opus-mt-en-tw',
    'uk': 'Helsinki-NLP/opus-mt-en-uk',
    'ur': 'Helsinki-NLP/opus-mt-en-ur',
    'vi': 'Helsinki-NLP/opus-mt-en-vi',
    'xh': 'Helsinki-NLP/opus-mt-en-xh'
}

# Directory to save the downloaded models
save_directory = 'models'
os.makedirs(save_directory, exist_ok=True)

def download_model_and_tokenizer(model_name, save_path):
    try:
        # Download model and tokenizer
        model = MarianMTModel.from_pretrained(model_name)
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        
        # Save the model and tokenizer
        model.save_pretrained(save_path)
        tokenizer.save_pretrained(save_path)
        
        print(f"Model and tokenizer for {model_name} downloaded and saved to {save_path}")
    except Exception as e:
        print(f"Error downloading model {model_name}: {e}")

# Download each model and tokenizer
for lang, model_name in models.items():
    model_save_path = os.path.join(save_directory, f"opus-mt-en-{lang}")
    if os.path.exists(model_save_path):
        print(f"Skipping {model_name}, already downloaded.")
        continue
    download_model_and_tokenizer(model_name, model_save_path)