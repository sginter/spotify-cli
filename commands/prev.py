import click

from utils import Spotify


@click.command()
@click.option('-v', '--verbose', count=True)
@click.option('-q', '--quiet', is_flag=True)
def prev(verbose=0, quiet=False):
    Spotify.request('me/player/previous', method='POST')
    if not quiet:
        from commands.status import status
        status.callback(verbose=verbose)

    return
