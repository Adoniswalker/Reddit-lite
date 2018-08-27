import click
from users.users import User, signin


@click.command()
@click.option('--username')
@click.option('--password')
@click.option('--role')
def register(username, password, role):
    user = User(username, '', role)
    user.create_user(password)


@click.command()
@click.option('--username')
@click.option('--password')
def login(username, password):
    click.echo("%s %s" % (username, password))
    print(signin(username, password))


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
