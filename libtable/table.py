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

from ._baseclass import BaseTableData
from .tablecontrol import TableControl
from prompt_toolkit import print_formatted_text


class Table:
    def __init__(self,
                 table: BaseTableData,
                 show_header: bool = None,
                 show_auto: bool = None
                 ):
        self.table = table
        self.table_control = TableControl(table, show_header=show_header, show_auto=show_auto)

    def show(self):
        print_formatted_text(self.table_control.to_formatted_text())
