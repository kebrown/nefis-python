# -*- coding: utf-8 -*-

import click
import nefis.cnefis
from . import dataset


@click.command()
def main(args=None):
    """Console script for nefis"""
    error, version = nefis.cnefis.getnfv()
    click.echo("Welcome to nefis, the numerical model storage format.")
    click.echo(version)


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def dump(filename):
    """Inspect nefis files"""
    click.echo(click.format_filename(filename))
    ds = dataset.Nefis(filename)
    click.echo(ds.dump())


if __name__ == "__main__":
    main()