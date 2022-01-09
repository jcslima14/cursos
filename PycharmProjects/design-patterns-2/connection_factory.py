# -*- coding: utf-8 -*-
import sqlite3


class Connection_factory(object):

    def get_connection(self):
        # tratamento de erro omitido
        return sqlite3.connect("alura.db")
