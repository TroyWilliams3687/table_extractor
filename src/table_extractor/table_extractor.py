#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Troy Williams

# uuid       = f3f0a2b0-91c0-11ec-adc0-a37618ec6a58
# author     = Troy Williams
# email      = troy.williams@bluebill.net
# date       = 2022-02-19
# -----------

"""
"""

# ------------
# System Modules - Included with Python

from pathlib import Path

# ------------
# 3rd Party - From pip

import click

from rich.traceback import install

install(show_locals=False)

# ------------
# Custom Modules

from .command_extract import extract

# -------------


@click.group()
@click.version_option()
@click.pass_context
def main(*args, **kwargs):
    """
    Extract tables from PDF files.

    """

    ctx = args[0]
    ctx.ensure_object(dict)


# Add the child menu options
main.add_command(extract)
# main.add_command(show)
