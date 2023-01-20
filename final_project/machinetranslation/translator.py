# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 12:43:58 2023

@author: cinde
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']
APIKEY='0jt0BsC0R06lNwQLt3pgt99UUf8FbSACm6oomh6TVYFs'
URL='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/7846f77c-831c-4b71-a9aa-49b358065bdf'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)



def english_to_french(english_text):
    '''This function translates an English string to French'''
    translation_response = language_translator.translate(text=english_text,model_id='en-fr')
    translation = translation_response.get_result()['translations'][0]['translation']
    return translation
    #return(f"The translation of {englishText} is {translation}" )

def french_to_english(french_text):
    '''This function translates an French string to English'''
    translation_response = language_translator.translate(text=french_text,model_id='fr-en')
    translation = translation_response.get_result()['translations'][0]['translation']
    return translation
    #return(f"The translation of {frenchText} is {translation}" )
