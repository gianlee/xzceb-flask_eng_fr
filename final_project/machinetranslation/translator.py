'''Translator module with IBM Watson'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-05-04',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Takes an English strings, returns the French translated strings'''
    ret = ""
    if not english_text:
        print("np data")
    else:
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

        if(not translation or not translation["translations"]
        or not translation["translations"][0]
        or not translation["translations"][0]["translation"]):
            print("Nothing translated")
        else:
            ret = translation["translations"][0]["translation"]

    return ret

def french_to_english(french_text):
    '''Takes a French strings, returns an English translated strings'''
    ret = ""
    if not french_text:
        print("np data")
    else:
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

        if(not translation or not translation["translations"]
        or not translation["translations"][0]
        or not translation["translations"][0]["translation"]):
            print("Nothing translated")
        else:
            ret = translation["translations"][0]["translation"]

    return ret
    