```bash
name: "robot"
fluents {
  name: "robot_at"
  valueType: "bool"
  signature: "Location"
}
fluents {
  name: "battery_charge"
  valueType: "real[0, 100]"
}
objects {
  name: "l1"
  type: "Location"
}
objects {
  name: "l2"
  type: "Location"
}
actions {
  name: "move"
  parameters: "l_from"
  parameters: "l_to"
  parameterTypes: "Location"
  parameterTypes: "Location"
  preconditions {
    type: 18
    args {
      type: 12
      payload {
        type: "int"
        value: "10"
      }
    }
    args {
      type: 7
      payload {
        type: "fluent"
        value: "battery_charge"
      }
    }
    payload {
      type: "none"
      value: "-"
    }
  }
  preconditions {
    type: 2
    args {
      type: 20
      args {
        type: 8
        payload {
          type: "aparam"
          value: "l_from"
        }
      }
      args {
        type: 8
        payload {
          type: "aparam"
          value: "l_to"
        }
      }
      payload {
        type: "none"
        value: "-"
      }
    }
    payload {
      type: "none"
      value: "-"
    }
  }
  preconditions {
    type: 7
    args {
      type: 8
      payload {
        type: "aparam"
        value: "l_from"
      }
    }
    payload {
      type: "fluent"
      value: "robot_at"
    }
  }
  preconditions {
    type: 2
    args {
      type: 7
      args {
        type: 8
        payload {
          type: "aparam"
          value: "l_to"
        }
      }
      payload {
        type: "fluent"
        value: "robot_at"
      }
    }
    payload {
      type: "none"
      value: "-"
    }
  }
  effects {
    x {
      type: 7
      args {
        type: 8
        payload {
          type: "aparam"
          value: "l_from"
        }
      }
      payload {
        type: "fluent"
        value: "robot_at"
      }
    }
    v {
      type: 11
      payload {
        type: "bool"
        value: "False"
      }
    }
  }
  effects {
    x {
      type: 7
      args {
        type: 8
        payload {
          type: "aparam"
          value: "l_to"
        }
      }
      payload {
        type: "fluent"
        value: "robot_at"
      }
    }
    v {
      type: 11
      payload {
        type: "bool"
        value: "True"
      }
    }
  }
  effects {
    x {
      type: 7
      payload {
        type: "fluent"
        value: "battery_charge"
      }
    }
    v {
      type: 15
      args {
        type: 7
        payload {
          type: "fluent"
          value: "battery_charge"
        }
      }
      args {
        type: 12
        payload {
          type: "int"
          value: "10"
        }
      }
      payload {
        type: "none"
        value: "-"
      }
    }
  }
}
initialState {
  x {
    type: 7
    args {
      type: 10
      payload {
        type: "obj"
        value: "l1"
      }
    }
    payload {
      type: "fluent"
      value: "robot_at"
    }
  }
  v {
    type: 11
    payload {
      type: "bool"
      value: "True"
    }
  }
}
initialState {
  x {
    type: 7
    args {
      type: 10
      payload {
        type: "obj"
        value: "l2"
      }
    }
    payload {
      type: "fluent"
      value: "robot_at"
    }
  }
  v {
    type: 11
    payload {
      type: "bool"
      value: "False"
    }
  }
}
initialState {
  x {
    type: 7
    payload {
      type: "fluent"
      value: "battery_charge"
    }
  }
  v {
    type: 12
    payload {
      type: "int"
      value: "100"
    }
  }
}
goals {
  type: 7
  args {
    type: 10
    payload {
      type: "obj"
      value: "l2"
    }
  }
  payload {
    type: "fluent"
    value: "robot_at"
  }
}
```