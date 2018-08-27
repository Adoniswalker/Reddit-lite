import click
from users.users import User, signin


@click.command()
@click.option('--username')
@click.option('--password')
@click.option('--role')
def register(username, password, role):
    user = User(username, '', role)
    response = user.create_user(password)
    if response == 'success':
        click.echo(click.style('Successfully created user ' + username, fg='green'))
    else:
        click.echo(click.style('Failed to create user', fg='red'))


@click.command()
@click.option('--username')
@click.option('--password')
def login(username, password):
    response = signin(username, password)
    if response == 'success':
        click.echo(click.style('Successfully logged in as ' + username, fg='green'))
    elif response == 'invalid':
        click.echo(click.style('Invalid username/password', fg='red'))
    else:
        click.echo(click.style('Login failed', fg='red'))


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
