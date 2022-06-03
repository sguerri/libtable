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
from libtable import TablePrompt


def main():
    data = example.get_data()

    table = TablePrompt(data, show_auto=False, index_column="iid")
    (index, item) = table.show()
    if index == -1:
        print("ERROR")
        print(item)
    else:
        print("RESPONSE")
        print(item)


if __name__ == "__main__":
    main()
