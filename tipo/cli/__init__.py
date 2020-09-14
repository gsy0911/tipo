import click


from .factory import CliFactory


@click.group(invoke_without_command=True)
@click.option('--taki', is_flag=True)
@click.option('--japanese', is_flag=True)
@click.pass_context
def cmd(ctx, taki=False, japanese=False):
    # if ctx.invoked_subcommand is None:
    # click.echo('This is parent!')
    cli_factory = CliFactory()
    ctx.obj['factory'] = cli_factory

    if taki:
        if japanese:
            click.echo(cli_factory.insert_japanese_taki(click))
        else:
            click.echo(cli_factory.insert_english_taki(click))


def main():
    cmd(obj={})
