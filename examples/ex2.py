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

#!/usr/bin/env python3

from libtable import TableSelect


def main():
    data = {
        "headers": [
            {"name": "IID", "width": 5, "rightalign": True},
            {"name": "TITLE"},
            {"name": "DESC", "weight": 2}
        ],
        "rows": [
            ("1", "AAA", "Description of AAA", "e"),
            ("2", "BBB dsqd qsd qd qdq q dqs", "Description of BBB"),
            ("3", 23, False),
            ("5", "DDD", "Description of DDD"),
            ("15", "EEE"),
        ]
    }

    table = TableSelect(data, full_screen=False, erase_when_done=True, show_auto=False)
    selected = table.show()
    print(selected)


if __name__ == "__main__":
    main()
