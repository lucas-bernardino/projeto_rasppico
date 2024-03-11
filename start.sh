#!/bin/bash

ngrok start --all --log=stdout >/dev/null &

sleep 2

cd rust-script && cargo run

cd .. && docker-compose up --build
