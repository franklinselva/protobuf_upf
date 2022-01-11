```bash
problem name = robot

types = [Location]

fluents = [
  bool robot_at[Location]
  real[0, 100] battery_charge
]

actions = [
  action move(Location l_from, Location l_to) {
    preconditions = [
      (10 <= battery_charge)
      (not (l_from == l_to))
      robot_at(l_from)
      (not robot_at(l_to))
    ]
    effects = [
      robot_at(l_from) := false
      robot_at(l_to) := true
      battery_charge := (battery_charge - 10)
    ]
  }
]

objects = [
  Location: [l1, l2]
]

initial values = [
  robot_at(l1) := true
  robot_at(l2) := false
  battery_charge := 100
]

goals = [
  robot_at(l2)
]

```