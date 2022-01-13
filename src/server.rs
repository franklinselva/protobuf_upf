/*
 *   Copyright (c) 2022
 *   All rights reserved.
 */
use async_trait::async_trait;
use tonic::{transport::Server, Request, Response, Status};
use upf::upf_server::{Upf, UpfServer};
use upf::{
    Action, ActionInstance, Answer, Assignment, Expression, Fluent, Object, Payload, Problem,
    SequentialPlan,
};

pub mod upf {
    tonic::include_proto!("upf");
}

#[derive(Default)]
pub struct UpfService {}

#[async_trait]
impl Upf for UpfService {
    async fn plan(&self, request: Request<Problem>) -> Result<Response<Answer>, Status> {
        println! ("Planning...");
        let _problem = Problem::from(request.into_inner());
        let answer = Answer::default();
        let response = Response::new(answer);
        Ok(response)
    }
}

#[derive(Default, Debug, Clone)]
pub struct Deserialize {
    pub fluent: Fluent,
    pub object: Object,
    pub expression: Expression,
    pub assignment: Assignment,
    pub payload: Payload,
    pub action: Action,
    pub problem: Problem,
    pub action_instance: ActionInstance,
    pub sequential_plan: SequentialPlan,
    pub answer: Answer,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Set address to localhost
    let addr = "127.0.0.1:2222".parse()?;
    let upf_service = UpfService::default();

    Server::builder()
        .add_service(UpfServer::new(upf_service))
        .serve(addr)
        .await?;

    Ok(())
}
