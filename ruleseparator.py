#!/usr/bin/env python3

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="input file.json")
args = parser.parse_args()

if args.file:

    with open(args.file) as data_file:
        data = json.load(data_file)

    for rule in data["resources"]:

        rule_name = rule["properties"]["displayName"]
        resources = []
        resources.append(rule)

        schema = {
            "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
            "contentVersion": "1.0.0.0",
            "parameters": {"workspace": {"type": "String"}},
            "resources": resources,
        }

        with open(rule_name + ".json", "w") as f:
            json.dump(schema, f)

else:
    parser.print_help()
    parser.exit()
