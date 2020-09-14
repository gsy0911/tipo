import click


from .factory import CliFactory


@click.group(invoke_without_command=True)
@click.pass_context
def cmd(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('This is parent!')
    ctx.obj['factory'] = CliFactory()


def main():
    cmd(obj={})
