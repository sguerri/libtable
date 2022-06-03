#!/usr/bin/env python3

# Copyright (C) 2022 Sebastien Guerri
#
# This file is part of libtable.
#
# libtable is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# libtable is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import data as example
from libtable import TableSelectControl

from prompt_toolkit import Application
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.containers import HSplit
from prompt_toolkit.layout.containers import Window


def main():
    data = example.get_data()

    def sort_iid(row):
        return int(row['iid'])

    def sort_desc(row):
        try:
            desc = str(row['desc'])
        except Exception:
            desc = ""
        if "Desc" in desc:
            return 0
        else:
            return 1

    table = TableSelectControl(data, show_auto=True, show_sort=True)
    table.add_sort_method(0, fn=sort_iid)
    table.add_sort_method(2, fn=sort_desc)

    body = HSplit([Window(content=table)])
    app = Application(layout=Layout(body), full_screen=True, key_bindings=table.get_key_bindings())
    app.run()

    print(table.get_response())


if __name__ == "__main__":
    main()
