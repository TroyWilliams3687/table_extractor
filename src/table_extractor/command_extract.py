#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Troy Williams

# uuid   = 94c6b7c4-91c1-11ec-adc0-a37618ec6a58
# author = Troy Williams
# email  = troy.williams@bluebill.net
# date   = 2022-02-19
# -----------

"""
"""

# ------------
# System Modules - Included with Python

from pathlib import Path
from datetime import datetime

# ------------
# 3rd Party - From pip

import click

from rich.console import Console
console = Console()

import camelot

# ------------
# Custom Modules

# -------------


@click.command()
@click.pass_context
@click.argument(
    "pdf",
    type=click.Path(
        exists=True,
        dir_okay=False,
        readable=True,
        path_type=Path,
    ),
)
@click.option(
    "--export",
    type=click.Choice(['csv', 'excel', 'html', 'json', 'markdown', 'sqlite'], case_sensitive=False),
    multiple=True,  # allow them to specify multiple solvers to use
    help="Export the tables to a particular format (CSV, Excel, HTML, JSON, markdown, sqlite).",
)
@click.option(
    "--pages",
    type=str,
    default='all',
    help="Choose the pages to search. Example: ‘1,3,4’ or ‘1,4-end’ or ‘all’. Default: 'all'",
)
@click.option(
    "--compress",
    is_flag=True,
    help="Compress the output data to a zip file. Only use compress with one export option at a time. Or it will overwrite other exports.",
)
def extract(*args, **kwargs):
    """
    Given a PDF file, extract all of the tables to various formats.

    # Usage

    $ te extract ./data/foo.pdf

    $ te extract ./data/foo.pdf --export=csv --export=excel --compress --pages='75-85'

    $ te extract ./data/foo.pdf --export=csv --export=excel --export=html --export=json --export=markdown --export=sqlite

    NOTE: The `--compress` option should only be used with one export option at a time. It will overwrite the other options.

    """
    ctx = args[0]

    build_start_time = datetime.now()

    pdf = kwargs['pdf']

    # https://camelot-py.readthedocs.io/en/master/user/quickstart.html
    tables = camelot.read_pdf(str(pdf), pages=kwargs['pages'])

    console.print(f'Found: {len(tables)} tables.')

    if len(tables) > 0:

        # https://camelot-py.readthedocs.io/en/master/api.html

        for export_format in kwargs['export']:

            extension = export_format.lower()

            if export_format == 'excel':
                extension = 'xlsx'

            if export_format == 'markdown':
                extension = 'md'

            output = pdf.parent / Path(f'{pdf.stem}.{extension}')
            # output = pdf.parent / Path('table_output') / Path(f'{pdf.stem}.{extension}')
            # output.parent.mkdir(parents=True, exists_ok=True)

            console.print(f'Export to {output}...')
            tables.export(str(output), f=export_format, compress=kwargs['compress'])

        console.print()
        console.print('Complete...')
        console.print()

        build_end_time = datetime.now()
        console.print(f"Started:   {build_start_time}")
        console.print(f"Finished:  {build_end_time}")
        console.print(f"Elapsed:   {build_end_time - build_start_time}")
        console.print()


