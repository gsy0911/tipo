import click


from .factory import CliFactory


@click.group(invoke_without_command=True)
@click.argument("file_path")
@click.option('--taki', is_flag=True)
@click.option('--japanese', is_flag=True)
@click.pass_context
def cmd(ctx, file_path, taki=False, japanese=False):
    # if ctx.invoked_subcommand is None:
    # click.echo('This is parent!')
    cli_factory = CliFactory()
    ctx.obj['factory'] = cli_factory

    response = cli_factory.execute_flake8(file_path=file_path)
    if response:
        if taki:
            if japanese:
                click.echo(cli_factory.insert_japanese_taki(click))
            else:
                click.echo(cli_factory.insert_english_taki(click))
        click.echo(response)


def main():
    cmd(obj={})
