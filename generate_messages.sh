#!/usr/bin/env bash

protoc -I=boxbot/message/proto --python_out=boxbot/message/ boxbot/message/proto/*.proto