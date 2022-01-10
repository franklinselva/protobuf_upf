/*
 *   Copyright (c) 2022
 *   All rights reserved.
 */
use upf::upf::{Fluent, Object, Expression, Assignment, Payload, Action, Problem, ActionInstance, Answer};

//Create a serializer object to convert pddl object from protobuf
pub struct Deserialize {
    pub fluent: Fluent;
    pub object: Object;
    pub expression: Expression;
    pub assignment: Assignment;
    pub payload: Payload;
    pub action: Action;
    pub problem: Problem;
    pub action_instance: ActionInstance;
    pub answer: Answer;
}

impl Deserialize {
    pub fn new() -> Deserialize {
        Deserialize {
            fluent: Fluent::new(),
            object: Object::new(),
            expression: Expression::new(),
            assignment: Assignment::new(),
            payload: Payload::new(),
            action: Action::new(),
            problem: Problem::new(),
            action_instance: ActionInstance::new(),
            answer: Answer::new(),
        }
    }
}

impl Default for Deserialize {
    fn default() -> Deserialize {
        Deserialize::new()
    }
}