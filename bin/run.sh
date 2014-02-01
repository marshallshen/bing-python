#!/bin/bash
# Start search and relevance feedbacks.
echo "account key is $1"
echo "target precision is $2"
echo "query is $3"

if [ -z "$3" ];then
  echo "use default account key"
fi

echo "Starting search.."

python "$(dirname "$0")/../bing/relevance.py" $1 $2 $3
