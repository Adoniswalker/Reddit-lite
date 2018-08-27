import click


@click.command()
@click.option('--email')
@click.option('--username')
@click.option('--password')
def register(email, username, password):
    click.echo("%s %s %s" % (email, username, password))


@click.command()
@click.option('--username')
@click.option('--password')
def login(username, password):
    click.echo("%s %s" % (username, password))


@click.command()
def logout():
    click.echo("logout")


@click.command()
@click.option('--body')
def comment(body):
    click.echo("comment %s" % body)


@click.group()
def cli():
    pass


cli.add_command(login)
cli.add_command(register)
cli.add_command(logout)
cli.add_command(comment)


if __name__ == '__main__':
    cli()
