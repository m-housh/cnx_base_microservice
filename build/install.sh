#!/bin/sh

API_NAME="api"
API_VERSION="0.0.1"

while [ "$1" != "" ]; do
    case $1 in
        -n | --name ) API_NAME="$2"; shift;;
        -v | --version ) API_VERSION="$2"; shift;;
        *) ;;
    esac
    shift
done

export API_NAME
export API_VERSION

pip install /app
