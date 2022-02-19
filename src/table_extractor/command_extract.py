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
# @click.argument(
#     "output",
#     type=click.Path(
#         exists=True,
#         file_okay=False,
#         dir_okay=True,
#         readable=True,
#         path_type=Path,
#     ),
# )
# @click.option(
#     "--verbose",
#     is_flag=True,
#     help="Display verbose data during the solve process.",
# )
# @click.option(
#     "--list-solvers",
#     is_flag=True,
#     help="Display the available solvers.",
#     callback=show_solvers,
#     expose_value=False,
#     is_eager=True,
# )
# @click.option(
#     "--solver",
#     default=["ECOS"],
#     help="Use a particular solver. Default `ECOS`. Use `--list-solvers` for available choices.",
#     type=str,
#     multiple=True,  # allow them to specify multiple solvers to use
# )
# @click.option(
#     "--iterations",
#     default=100,
#     help="The maximum number of iterations to perform.",
#     type=int,
# )
def extract(*args, **kwargs):
    """
    Given a PDF file, extract all of the tables.

    # Usage

    $ te ./data/pdf

    """
    ctx = args[0]

    pdf = kwargs['pdf']

    console.print(pdf)

    # config = toml.loads(kwargs["configuration"].read_text())
    # output = kwargs["output"]

    # # console.print(config)
    # # {'title': 'Uniform Distribution (N=20, r=75)', 'particle_count': 20, 'particle_sizes': [[1, 75]]}

    # build_start_time = datetime.now()

    # # Keep the same arrangement from run-to-run - comment it out to get random behavior
    # # np.random.seed(10)

    # n = config["particle_count"]

    # r = []

    # for ps in config["particle_sizes"]:
    #     ratio, radius = ps
    #     r.extend([radius] * int(n * ratio))

    # if len(r) != n:
    #     console.print(
    #         f"[red]The number of radii != particles ({len(r)} != {n}). "
    #         "Setting n = len(r)![/red]"
    #     )
    #     n = len(r)

    # r = np.array(r)

    # # ---------------
    # c = cvx.Variable((n, 3))

    # constr = []

    # for i in range(n - 1):
    #     constr.append(
    #         cvx.norm(cvx.reshape(c[i, :], (1, 3)) - c[i + 1 : n, :], 2, axis=1)
    #         >= r[i] + r[i + 1 : n]
    #     )

    # prob = cvx.Problem(cvx.Minimize(cvx.max(cvx.max(cvx.abs(c), axis=1) + r)), constr)

    # # https://www.cvxpy.org/tutorial/advanced/index.html <- solver listing and their options

    # for solver in kwargs["solver"]:

    #     prob.solve(
    #         method="dccp",
    #         solver=solver,
    #         verbose=kwargs["verbose"],
    #         max_iters=kwargs["iterations"],
    #         abstol=5e-5,  # abstol=1e-8,
    #         reltol=5e-5,  # reltol=1e-8,
    #         feastol=1e-4,  # feastol=1e-8,
    #         # abstol_inacc=5e-5,
    #         # reltol_inacc=5e-5,
    #         # feastol_inacc=1e-4,
    #         # ep=1e-4,
    #         # max_slack=1e-4,
    #         # ccp_times=5,
    #     )

    #     # ------------
    #     l = cvx.max(cvx.max(cvx.abs(c), axis=1) + r).value * 2
    #     console.print(f"Cube Edge = {l:.4f}")

    #     cv = cvx.power(l, 3).value
    #     console.print(f"Cube Volume = {cv:.4f}")

    #     sv = (4 / 3) * np.pi * cvx.sum(cvx.power(r, 3)).value
    #     console.print(f"Sphere Volume = {sv:.4f}")
    #     console.print()

    #     ratio = sv / cv
    #     console.print(f"Packing Ratio = {ratio:.4f} ({ratio:.4%})")
    #     console.print()

    #     build_end_time = datetime.now()
    #     console.print(f"Started:   {build_start_time}")
    #     console.print(f"Finished:  {build_end_time}")
    #     console.print(f"Elapsed:   {build_end_time - build_start_time}")

    #     # --------
    #     # Save Data for Plotting

    #     data = build_output(
    #         config["title"],
    #         build_start_time,
    #         build_end_time,
    #         [
    #             CalculatedCircle3D(
    #                 c[i, 0].value, c[i, 1].value, c[i, 2].value, float(r[i])
    #             )
    #             for i in range(n)
    #         ],
    #         packing_ratio=ratio,
    #         cube_volume=float(cv),
    #         sphere_volume=sv,
    #         bbox_length=l,
    #         max_iterations=kwargs["iterations"],
    #     )

    #     json_output = output.joinpath(
    #         f"{kwargs['configuration'].stem}.{solver.lower()}.json"
    #     )

    #     json_output.write_text(json.dumps(data, sort_keys=True, indent=4))
    #     console.print()
    #     console.print(f"Results written to: {output}")
    #     console.print()
