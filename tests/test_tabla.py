from csv_db import Table
from csv_db.errors import DuplicateColumnsError, EmptyColumnNameError, NotANumberError


def assert_error(element: callable, params: dict, expected_error: callable):
    try:
        element(**params)
    except Exception as error:
        assert isinstance(error, expected_error), error


mi_tabla = Table(columns=["nombre", "edad", "telefono"])
assert mi_tabla.columns == ["id", "nombre", "edad", "telefono"], mi_tabla.columns

mi_tabla = Table(columns=["id", "nombre", "edad", "telefono"])
assert mi_tabla.columns == ["id", "nombre", "edad", "telefono"], mi_tabla.columns

try:
    mi_tabla = Table(columns=["id", "nombre", "nombre", "edad", "telefono"])
except Exception as error:
    assert isinstance(error, DuplicateColumnsError), error

assert_error(
    element=Table,
    params=dict(columns=[""]),
    expected_error=EmptyColumnNameError
)

mi_tabla = Table(columns=["id", "nombre", "edad", "telefono"])

assert (
    mi_tabla.add(new_row=dict(nombre="Javi", telefono="99999999", edad=35))
    == [1, "Javi", 35, "99999999"]
)

result = mi_tabla.add(new_row=dict(nombre="Javi", telefono="99999999", edad=35, apellidos="Pérez"))
assert result == [2, "Javi", 35, "99999999"], result

result = mi_tabla.get(1)
assert result == [1, "Javi", 35, "99999999"], result

assert_error(element=mi_tabla.get, params=dict(id="a"), expected_error=NotANumberError)

result = mi_tabla.get(10)
assert result == [], result

assert_error(element=mi_tabla.get, params=dict(id=""), expected_error=NotANumberError)