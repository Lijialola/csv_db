from copy import copy
from unittest import TestCase

from csv_db import Table


class TableTests(TestCase):


    def setUp(self):
        self.mi_tabla_for_edit = Table(columns=["id", "nombre", "edad", "telefono"])
        self.created_row = copy(self.mi_tabla_for_edit.add(new_row=dict(nombre="Javi", telefono="99999999", edad=35)))


    def test_anyadir_columnas(self):
        mi_tabla = Table(columns=["nombre", "edad", "telefono"])

        self.assertEqual(mi_tabla.columns, ["id", "nombre", "edad", "telefono"])

    def test_anyadir_columnas_con_id(self):
        mi_tabla = Table(columns=["id", "nombre", "edad", "telefono"])

        self.assertEqual(mi_tabla.columns, ["id", "nombre", "edad", "telefono"])

    def test_editar_registro(self):
        new_data = dict(nombre="Pedro", telefono="888888888", edad=25)

        result = self.mi_tabla_for_edit.edit(
            id=self.created_row[0],
            row_update=new_data
        )

        self._check_updated_values(new_data, result)

    def test_editar_registro_parcialmente(self):
        new_data = dict(nombre="Pedro")

        result = self.mi_tabla_for_edit.edit(
            id=self.created_row[0],
            row_update=new_data
        )

        self._check_updated_values(
            new_data,
            result,
            not_update_columns=["telefono", "edad"]
        )

    def _check_updated_values(self, new_data: dict, result: list, not_update_columns: list = []):
        for index, key in enumerate(self.mi_tabla_for_edit.columns):
            if key == "id":
                continue

            self.assertNotEqual(result[index], self.created_row[index] if key in not_update_columns else new_data.get(key))

