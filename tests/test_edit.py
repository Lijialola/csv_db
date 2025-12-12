from unittest import TestCase

from csv_db import Table


class TestTableEdit(TestCase):

    def setUp(self):
        """Prepara una instancia de Table con datos iniciales antes de cada test."""
        columns = ["nombre", "edad", "ciudad"]
        self.table = Table(columns)

        # Añadir algunos datos
        self.table.add({"nombre": "Alice", "edad": 30, "ciudad": "NY"})  # ID 1
        self.table.add({"nombre": "Bob", "edad": 25, "ciudad": "LA"})  # ID 2
        self.table.add({"nombre": "Charlie", "edad": 35, "ciudad": "Chicago"})  # ID 3


    def test_edit_existing_row_full_update(self):
        """Debe actualizar completamente una fila existente por ID."""
        row_id = 2
        update_data = {"nombre": "Roberto", "edad": 26, "ciudad": "Miami"}

        expected_row = [2, "Roberto", 26, "Miami"]

        result = self.table.edit(row_id, update_data)

        self.assertEqual(result, expected_row)
        self.assertEqual(self.table.rows[1], expected_row)  # Verificar el estado interno
        self.assertEqual(self.table.get(row_id), expected_row)  # Verificar con el método get

    def test_edit_existing_row_partial_update(self):
        """Debe actualizar parcialmente una fila existente, dejando otras columnas intactas."""
        row_id = 1
        # Actualizar solo la ciudad
        update_data = {"ciudad": "Boston"}

        # Fila original: [1, 'Alice', 30, 'NY']
        expected_row = [1, "Alice", 30, "Boston"]

        result = self.table.edit(row_id, update_data)

        self.assertEqual(result, expected_row)
        self.assertEqual(self.table.rows[0], expected_row)

    def test_edit_existing_row_case_insensitive_keys(self):
        """Debe manejar las claves del diccionario de actualización sin importar el caso (case-insensitive)."""
        row_id = 3
        # Usar mayúsculas y espacios
        update_data = {" nombre ": " Charles ", " edad ": 36}

        # Fila original: [3, 'Charlie', 35, 'Chicago']
        expected_row = [3, " Charles ", 36, "Chicago"]

        result = self.table.edit(row_id, update_data)

        self.assertEqual(result, expected_row)
        self.assertEqual(self.table.rows[2], expected_row)

    def test_edit_ignores_non_existent_columns_in_update(self):
        """Debe ignorar las claves en row_update que no coinciden con las columnas de la tabla."""
        row_id = 1
        update_data = {"edad": 31, "ColumnaFalsa": "Valor Falso"}

        # Fila original: [1, 'Alice', 30, 'NY']
        expected_row = [1, "Alice", 31, "Boston"]  # ColumnaFalsa debe ser ignorada (Fallo de contaminación)

        result = self.table.edit(row_id, update_data)

        self.assertEqual(result, expected_row)
        self.assertEqual(self.table.rows[0], expected_row)
