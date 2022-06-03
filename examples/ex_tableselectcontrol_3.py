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

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding import merge_key_bindings
from prompt_toolkit.layout.controls import FormattedTextControl


def main():
    data = example.get_data()
    table = TableSelectControl(data, global_key_bindings=False)
    response = FormattedTextControl("")

    kb = KeyBindings()

    @kb.add('space')
    def _(event):
        response.text = str(table.get_current_row())

    @kb.add('enter')
    def _(event):
        event.app.exit()

    kb = merge_key_bindings([kb, table.get_key_bindings()])

    body = HSplit([
        Window(content=table),
        Window(content=response)
    ])
    app = Application(layout=Layout(body), full_screen=True, key_bindings=kb)
    app.run()

    print(table.get_response())


if __name__ == "__main__":
    main()
