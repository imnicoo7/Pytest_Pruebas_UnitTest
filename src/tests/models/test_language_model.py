import sys
import os

# Obtener la ruta de la carpeta actual (que contiene src)
ruta_carpeta_actual = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Agregar la ruta de la carpeta actual al sys.path
sys.path.append(ruta_carpeta_actual)
# Models
from models.LanguageModel import LanguageModel

# Prueba que sean diferentes de None
def test_get_languages_not_none():
    languages = LanguageModel.get_languages()
    assert languages != None
    

# Prueba que contenga elementos
def test_get_languages_has_elements():
    languages = LanguageModel.get_languages()
    assert len(languages) > 0


# Prueba de longitud de elementos
def test_get_languages_check_elements_length():
    languages = LanguageModel.get_languages()
    for language in languages:
        assert len(language) > 0
