import click

from utils import Spotify


@click.command()
@click.option('-v', '--verbose', count=True)
def play(verbose=0):
    Spotify.request('me/player/play', method='PUT')
    if verbose:
        from commands.status import status
        status.callback(verbose=verbose-1)

    return
