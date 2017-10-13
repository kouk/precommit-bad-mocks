#!/usr/bin/python
from __future__ import print_function
import ast
import optparse
import sys


class MockChecker(ast.NodeVisitor):
    def __init__(self):
        self.errors = 0
        self.current_filename = ""
        self.non_existent_methods = [
            'assert_calls',
            'assert_not_called',
            'assert_called',
            'assert_called_once',
            'not_called',
            'called_once',
            'called_once_with',
        ]

    def check_files(self, files):
        for file in files:
            self.check_file(file)

    def check_file(self, filename):
        self.current_filename = filename
        try:
            with open(filename) as f:
                node = ast.parse(f.read())
        except SyntaxError as error:
            print("SyntaxError on file {}:{}".format(filename, error.lineno),
                  file=sys.stderr)
            return
        self.visit(node)

    def visit_Call(self, node):
        if not hasattr(node.func, 'attr'):
            return
        if node.func.attr in self.non_existent_methods:
            print("{}:{}: maybe you called a nonexistent mock method".format(
                self.current_filename, node.lineno), file=sys.stderr)
            self.errors += 1


def main():
    parser = optparse.OptionParser(
        usage="%prog [options] file [files]",
        description=("Checks that the test file does "
                     "not contain non-existent mock methods"))
    (opts, files) = parser.parse_args()
    if len(files) == 0:
        parser.error("No filenames provided")

    checker = MockChecker()
    checker.check_files(files)
    return 1 if checker.errors else 0


if __name__ == '__main__':
    sys.exit(main())
