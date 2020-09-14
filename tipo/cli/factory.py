from tipo.utils import (
    insert_large_str
)

from tipo import constants


class CliFactory:

    def __init__(self, cli_width=120):
        self.cli_width = cli_width

    def insert_english_taki(self, prompter):
        if self.cli_width >= 120:
            r1 = insert_large_str(constants.TAKI, constants.WHAT, 3, 3)
            r2 = insert_large_str(r1, constants.IS, 3, 9)
            r3 = insert_large_str(r2, constants.THIS, 3, 15)
            prompter.echo(r3)

    def insert_japanese_taki(self, prompter):
        if self.cli_width >= 120:
            r1 = insert_large_str(constants.TAKI, constants.NANDESUKA, 3, 3)
            r2 = insert_large_str(r1, constants.KORE, 3, 14)
            prompter.echo(r2)
