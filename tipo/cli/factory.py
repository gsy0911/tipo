import subprocess

from tipo.utils import (
    insert_large_str
)

from tipo import constants


class CliFactory:
    IGNORE_CODE = ["E501", "E502"]

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

    def execute_flake8(self, file_path: str, prompter):
        flake8_command = ["flake8", file_path, f"--ignore={','.join(self.IGNORE_CODE)}"]
        try:
            response = subprocess.run(
                flake8_command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError as e:
            raise e
        else:
            if response.stdout:
                self.insert_english_taki(prompter=prompter)