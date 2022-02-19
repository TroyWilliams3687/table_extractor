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
    type=click.Choice(['CSV', 'Excel', 'HTML', 'JSON', 'MD', 'SQL'], case_sensitive=False),
    multiple=True,  # allow them to specify multiple solvers to use
    help="Export the tables to a particular format (CSV, Excel, HTML, JSON, md, SQL).",
)
def extract(*args, **kwargs):
    """
    Given a PDF file, extract all of the tables.

    # Usage

    $ te extract ./data/foo.pdf

    $ te extract ./data/foo.pdf --export=csv --export=excel


    """
    ctx = args[0]

    pdf = kwargs['pdf']

    tables = camelot.read_pdf(str(pdf))

    console.print(f'Found: {len(tables)} tables.')

    for i, table in enumerate(tables):
        console.print(f'Table {i} parsing report:')
        console.print(table.parsing_report)
        console.print()
        console.print(table.df)

        # https://camelot-py.readthedocs.io/en/master/api.html
        for export_format in kwargs['export']:

            if export_format.lower() == 'csv':
                output = pdf.parent / Path(f'{pdf.stem}.{i}.csv')
                console.print(f'Export to {output}...')
                table.to_csv(str(output))

            elif export_format.lower() == 'excel':

                output = pdf.parent / Path(f'{pdf.stem}.{i}.xlsx')
                console.print(f'Export to {output}...')
                table.to_excel(str(output))

            elif export_format.lower() == 'html':

                output = pdf.parent / Path(f'{pdf.stem}.{i}.html')
                console.print(f'Export to {output}...')
                table.to_html(str(output))

            elif export_format.lower() == 'json':

                output = pdf.parent / Path(f'{pdf.stem}.{i}.json')
                console.print(f'Export to {output}...')
                table.to_json(str(output))

            elif export_format.lower() == 'md':

                output = pdf.parent / Path(f'{pdf.stem}.{i}.md')
                console.print(f'Export to {output}...')
                table.to_markdown(str(output))

            elif export_format.lower() == 'sql':

                output = pdf.parent / Path(f'{pdf.stem}.{i}.sqlite')
                console.print(f'Export to {output}...')
                table.to_sqlite(str(output))
