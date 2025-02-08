# Service Management Multiagent System (SMMS)

This repository contains an service management algorithm for cloud and edge computing service placement and migration, designed for running and testing in the simulated environment of [EdgeSimPy](https://github.com/EdgeSimPy/EdgeSimPy).

The approach leverages multi-agent cooperation to enhance decision-making as to dynamically allocates and migrate services, aiming to optimize defined metrics (e.g. latency, privacy, resource utilization, etc). The initial aim of this work is to place services in Edge Servers near its users, given their location in a 2x2 grid.

## How to install and run

- Requirements:

  - `make`: `brew install make`
  - `pyenv`: `brew install pyenv` (be sure to read its installation instructions, needs to be added to your shell profile)
  - `python 3.13.1`: `pyenv install 3.13.1`

- Install the project's Python dependencies:

  - `make install`

- Run the project:
  - `make run`
