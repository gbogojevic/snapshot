# snapshot
AWS EC2 instances snapshot

## About

Demo - uses boto3 to manage AWS EC2 instance snapshots

## Configure

it uses the config file create by the AWS cli

'aws configure --profile name'

## Running

'pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>'

*command* is instances, columes or snapshots
*subcommand* - depends on command
*project* is optional