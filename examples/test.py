import json


class BaseTableHeader:
    def __init__(self,
                 column: str,
                 name: str,
                 width: int = -1,
                 weight: int = 1,
                 rightalign: bool = False
                 ) -> None:
        self.column: str = column
        self.name: str = name
        self.width: int = width
        self.weight: int = weight
        self.rightalign: bool = rightalign

    def to_json(self) -> json:
        return {
            "column": self.column,
            "name": self.name,
            "width": self.width,
            "weight": self.weight,
            "rightalign": self.rightalign
        }

    def __str__(self) -> str:
        return json.dumps(self.to_json(), indent=4)


class BaseTableOptions():
    def __init__(self,
                 span: int = 1,
                 show_auto: bool = False,
                 show_even: bool = True,
                 show_header: bool = True,
                 show_selection: bool = True,
                 header_style: str = "bold ansimagenta underline",
                 selection_style: str = "bg:ansiblue"
                 ) -> None:
        self.span: int = span
        self.show_auto: bool = show_auto
        self.show_even: bool = show_even
        self.show_header: bool = show_header
        self.show_selection: bool = show_selection
        self.header_style: str = header_style
        self.selection_style: str = selection_style

    def to_json(self) -> json:
        return {
            "span": self.span,
            "show_auto": self.show_auto,
            "show_even": self.show_even,
            "show_header": self.show_header,
            "show_selection": self.show_selection,
            "header_style": self.header_style,
            "selection_style": self.selection_style
        }

    def __str__(self) -> str:
        return json.dumps(self.to_json(), indent=4)


class BaseTableData:
    def __init__(self,
                 headers: [BaseTableHeader] = [],
                 rows: json = {},
                 options: BaseTableOptions = BaseTableOptions()
                 ) -> None:
        self.headers: [BaseTableHeader] = headers
        self.rows: json = rows
        self.options: BaseTableOptions = options

    def to_json(self) -> json:
        return {
            "headers": list(map(lambda header: header.to_json(), self.headers)),
            "rows": self.rows,
            "options": self.options.to_json()
        }

    def __str__(self) -> str:
        return json.dumps(self.to_json(), indent=4)


toto = BaseTableData()
toto.headers.append(BaseTableHeader("iid", "IID"))

#print(toto)


a: json = {
    "aaa": "aaa",
    "bbb": 12,
    "ccc": {"aa": "aa", "dd": True}
}



for (key, value) in a.items():
    print(key, str(value))
