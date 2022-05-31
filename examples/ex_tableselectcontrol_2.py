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

from libtable import TableSelectControl

from prompt_toolkit import Application
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.containers import HSplit
from prompt_toolkit.layout.containers import Window

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding import merge_key_bindings


def main():
    data = {
        "headers": [
            {"name": "IID", "width": 5, "rightalign": True},
            {"name": "TITLE"},
            {"name": "DESC", "weight": 2}
        ],
        "rows": [
            ("1", "<b>AAA</b> <i>BBB</i>", "Description of AAA", "e"),
            ("2", "BBB dsqd qsd qd qdq q dqs", "<aaa bg='red'>Description of BBB</aaa>"),
            ("3", 23, False),
            ("5", "DDD", "<aaa bg='blue'>Description of DDD</aaa>"),
            ("15", "EEE"),
        ]
    }

    table = TableSelectControl(data)

    kb = KeyBindings()

    @kb.add('space')
    def _(event):
        temp = list(data["rows"][0])
        temp[1] = "OK"
        data["rows"][0] = tuple(temp)

    kb = merge_key_bindings([kb, table.get_key_bindings()])

    body = HSplit([Window(content=table)])
    app = Application(layout=Layout(body), full_screen=True, key_bindings=kb)
    app.run()

    print(table.get_response())


if __name__ == "__main__":
    main()
