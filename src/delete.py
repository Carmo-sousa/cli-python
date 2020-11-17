import click
import os
import time

from src.colorsascii import *
from src.listRepeatedFiles import repeated_files

def remove():
    """Remove os arquivos"""
    repeated = repeated_files(os.listdir("."))
    length = len(repeated)
    click.echo(f"{verde}Arquivos duplicados: {vermelho}{length}{reset}\n")

    if not repeated:
        click.echo(f"{ciano_claro}✔ Não existe trabalho aqui ✨{reset}")
        return

    for file in repeated:
        click.echo(f"{vermelho}✖ {verde}Removendo o arquivo: {vermelho}{file}{reset}")

        time.sleep(0.1)
        os.remove(file)
        click.echo(f"{verde}✔ Arquivo removido!{reset}")

    click.echo(f"{ciano_claro}✔ Tudo limpinho ✨{reset}")