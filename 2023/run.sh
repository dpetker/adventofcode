#!/bin/bash -e

# run.sh - build and run a given day's solution

day="$1"

if [ -z "$day" ]; then
  echo "Usage $0 <day>"
  exit 1
fi

file_to_run="src/day$day.kt"

if [ ! -f "$file_to_run" ]; then
  echo "Error: could not find file: $file_to_run"
  exit 1
fi

jar_file="build/day$day.jar"

kotlinc $file_to_run -include-runtime -d $jar_file

java -jar $jar_file
