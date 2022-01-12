/*
 *   Copyright (c) 2022
 *   All rights reserved.
 */
fn main() -> Result<(), Box<dyn std::error::Error>> {
    tonic_build::compile_protos("src/upf.proto")?;
    Ok(())
}
