<!--
 Copyright 2022 Franklin Selva. All rights reserved.
 Use of this source code is governed by a BSD-style
 license that can be found in the LICENSE file.
-->

> **NOTE: This repo will not be used for development anymore and any more information or progress can be tracked in this [PR]**(https://github.com/plaans/aries/pull/29)

# PROTOBUF - UPF

This is a temporary repository for working with UPF serialization.

Available problems right now (in python),

- `robot -> is currently default`
- robot_no_negative_preconditions
- robot_decrease
- robot_loader
- robot_loader_mod
- robot_loader_adv
- robot_locations_connected
- robot_locations_visited
- charge_discharge
- matchcellar
- timed_connected_locations

## Current UPF Problem template

The problem is presented as [data/problem.md](data/problem.md)
The parsed UPF problem data is available in [data/UPF.md](data/UPF.md)

## First run

To start the initial setup, you can start in a `pyenv`,

```
sh first_setup.sh
```

## Usage

To start the python client, you can start in a `pyenv`,

```
python python/main.py
```

And the server can be started by,

```
cargo run --bin upf-server
```
