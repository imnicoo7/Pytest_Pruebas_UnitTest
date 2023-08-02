import sys
import os
import pytest
# Obtener la ruta de la carpeta actual (que contiene src)
ruta_carpeta_actual = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Agregar la ruta de la carpeta actual al sys.path
sys.path.append(ruta_carpeta_actual)

from main import sumar, is_greater_than, login

def test_sum():
    assert sumar(2, 3) == 5 # assert hace que sea verdad


def test_is_greater_than():
    assert is_greater_than(10, 2)


@pytest.mark.parametrize(
    "input_x, input_y, espects",
    [
        (5, 1, 6),
        (5, sumar(3, 2), 10),
        (sumar(7, 3), 10, 20),
        (-7, 10, sumar(-7, 10)),
        
    ]
)    
def test_sum_params(input_x, input_y, espects):
    
    assert sumar(input_x, input_y) == espects


def test_login_():
    
    assert login("imnico_", "1234")
 

def test_login_fail():
    
    assert not login("imnico_", "12344")
    