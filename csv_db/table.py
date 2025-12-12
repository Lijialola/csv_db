from typing import Any

from csv_db.errors import DuplicateColumnsError, EmptyColumnNameError, NotANumberError, NotFoundItemError


class Table:

    def __init__(self, columns: list, rows: list = []):
        self.last_id = 0
        self.rows = rows
        self.columns = self._set_columns(columns)

    def _set_columns(self, columns: list) -> list:
        unique_columns = self.__get_unique_columns(columns)

        if len(unique_columns) != len(columns):
            raise DuplicateColumnsError

        return ["id"] + list(
            filter(
                lambda column: column != "id",
                unique_columns
            )
        )


    def __get_unique_columns(self, columns: list) -> list:
        unique_columns = list()

        for colmun in columns:
            formatted_column = self._format_item(colmun)

            if not formatted_column:
                raise EmptyColumnNameError()

            if formatted_column in unique_columns:
                continue

            unique_columns.append(formatted_column)
        return unique_columns

    def add(self, new_row: dict) -> list:
        list_row = []

        for key in self.columns:
            if key == "id":
                new_row["id"] = self._get_new_id()

            list_row.append(new_row.get(key))

        self.rows.append(list_row)

        return list_row

    def _get_new_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def get(self, id: int) -> list:
        try:
            id = int(id)

        except ValueError:
            raise NotANumberError()

        for row in self.rows:
            if row[0] != id:
                continue

            return row

        return []

    def edit(self, id: int, row_update: dict) -> list:
        row_update = {
            self._format_item(key): value
            for key, value in row_update.items()
        }

        for index, row in enumerate(self.rows):
            selected = row

            if selected[0] != id:
                continue

            for item_index, key in enumerate(self.columns):
                if key == "id":
                    continue

                if key not in row_update.keys():
                    continue

                self.rows[index][item_index] = row_update[key]

            return self.rows[index]

        return []

    def delete(self, id: int) -> list:
        raise NotImplemented

    def filter(self, conditions: dict) -> list:
        raise NotImplemented

    @staticmethod
    def _format_item(item: Any) -> str:
        return str(item).lower().strip()
