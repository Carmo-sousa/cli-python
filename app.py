import click
import os

from src.colorsascii import *
from src.delete import remove
from src.listRepeatedFiles import repeated_files

@click.group()
def cli():
    pass

@cli.command()
@click.option('--length/--no-length', default=False)
def list_files(length):
    """Lista todos os arquivos repetidos do diretorio atual"""

    files = os.listdir('.')

    if length:
        files = os.listdir('.')
        click.echo(f"{verde}Size\t Nane{reset}")
        for file in files:
            click.echo(f"{vermelho}{os.path.getsize(file)//1024:4}K{reset}\t {file}")
        return

    repeated = repeated_files(files)

    if not repeated:
        return click.echo(f"{verde}Por aqui está tudo limpo! ✨✨✨{reset}")
    
    for file in repeated:
        click.echo(f"{vermelho}Arquivo duplicado: {file}{reset}")

@cli.command()
def delete():
    """Remove todos os arquivos duplicados"""
    remove()
