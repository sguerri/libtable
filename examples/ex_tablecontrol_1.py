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

from libtable import TableControl

from prompt_toolkit import print_formatted_text


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

    table = TableControl(data)

    print_formatted_text(table.to_formatted_text())


if __name__ == "__main__":
    main()
