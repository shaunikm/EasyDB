import json
import os


class Table:
    def __init__(self, filename, tablename):
        self.filename = filename
        self.tablename = tablename
        self.deleted = False
        self.set = False

    def setup_table(self, args: list = None, already_set: bool = False):
        if not already_set:
            table = {
                self.tablename: {},
                "tabledata": {
                    "arguments": [i for i in args],
                    "filename": self.filename
                }
            }

            with open(self.filename, 'w') as f:
                json.dump(table, f, indent=2)
        self.set = True

    def apdata(self, primary_key: str, args: list):
        self.check_if_table_setup()
        self.check_if_table_is_deleted()
        data = json.load(open(self.filename))
        arguments = data['tabledata']['arguments']
        data[self.tablename][primary_key] = {}
        if len(data['tabledata']['arguments']) != len(args):
            raise ValueError('Different number of arguments than required arguments to make row in table')
        for i, arg in zip(args, arguments):
            data[self.tablename][primary_key][arg] = i
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)

    def get_keys(self, *key: str):
        self.check_if_table_setup()
        self.check_if_table_is_deleted()
        ret = []
        data = json.load(open(self.filename))
        for x in data:
            ret.append({j: x[j] for j in key})
        return ret

    def get(self, primary_key: str):
        self.check_if_table_setup()
        self.check_if_table_is_deleted()
        data = json.load(open(self.filename))
        return data[self.tablename][primary_key]

    def delete(self, primary_key: str):
        self.check_if_table_setup()
        self.check_if_table_is_deleted()
        data = json.load(open(self.filename))
        del data[self.tablename][primary_key]
        json.dump(data, open(self.filename, 'w'), indent=2)

    def req_args(self):
        self.check_if_table_setup()
        self.check_if_table_is_deleted()
        data = json.load(open(self.filename))
        return data['tabledata']['arguments']

    def check_if_table_setup(self):
        if self.set:
            return
        else:
            raise ValueError('Table not setup')

    def deltable(self):
        self.check_if_table_setup()
        os.remove(os.path.join(os.getcwd(), self.filename))
        self.deleted = False

    def check_if_table_is_deleted(self):
        if not self.deleted:
            return
        else:
            raise AttributeError('Table has been deleted and does not exist anymore. Setup a new table.')

    def number_of_args(self):
        self.check_if_table_setup()
        self.check_if_table_is_deleted()
        data = json.load(open(self.filename))
        return len(data['tabledata']['arguments'])

    def number_of_rows(self):
        self.check_if_table_setup()
        self.check_if_table_is_deleted()
        data = json.load(self.filename)
        return len(data[self.tablename])
