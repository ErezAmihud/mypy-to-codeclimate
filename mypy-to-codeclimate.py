#!/usr/bin/env python3

import re
import json
import hashlib
import argparse

line_number_regex = ":(\d+):"
extended_line_number_regex = ":(\d+):(\d+):(\d+):(\d+):"
file_name_regex = "^(.+?):"
issue_description_error_regex = "error(.*)"
issue_description_note_regex = "note(.*)"
# need to add this regex in
issue_description_warning_regex = "warning(.*)"

def get_positions(issue)->dict:
    possible_extended_line_number = re.search(extended_line_number_regex, issue)
    if possible_extended_line_number is not None:
        return {"begin":{"line":possible_extended_line_number.group(1), "column": possible_extended_line_number.group(2)},
                "end":{"line":possible_extended_line_number.group(3), "column": possible_extended_line_number.group(4)}
                }

        
    possible_line_number = re.search(line_number_regex, issue)
    line_number = 1
    if possible_line_number is not None:
        line_number = possible_line_number.group(1)

    return {"begin": {"line":line_number, "column":0}, "end":{"line":line_number, "column": 0}}


def analyze(mypy_output:str) -> str:
    split_issues_on_newline = mypy_output.strip().split('\n')
    del split_issues_on_newline[-1]
    for issue in split_issues_on_newline:
        positions = get_positions(issue)

        possible_file_name = re.search(file_name_regex, issue)
        if possible_file_name:
            file_name=possible_file_name.group(1)
        else:
            continue

        issue_description = re.search(issue_description_error_regex, issue)
        if issue_description is not None:
            issue_description = issue_description.group(1)
        elif issue_description is None:
            issue_description = re.search(issue_description_note_regex, issue).group(1)
        else:
            issue_description = re.search(issue_description_warning_regex, issue).group(1)

        codeclimate_json = {
                'type': 'issue',
                'check_name': 'Static Type Check',
                'categories': ['Style'],
                'fingerprint': "",
                'description' : issue_description,
                "location": {
                    "path":file_name,
                    "positions": positions,
                    },
                "severity": "major"
                }
        codeclimate_json["fingerprint"] = hashlib.md5(json.dumps(codeclimate_json).encode()).digest().hex()
        yield codeclimate_json

def run(input_file: str, output_file: str):
    json.dump(list(analyze(open(input_file, "r").read())), open(output_file, "w"), indent=4)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="output file created from mypy output")
    parser.add_argument("output_file", help="The file to write the codeclimate result to")
    args = parser.parse_args()
    run(args.input_file, args.output_file)
if __name__ == "__main__":
    main()
