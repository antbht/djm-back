#!/bin/bash

init() {
    source bin/activate
}

unit_tests() {
    python -m unittest unit_tests/*py
}

dist() {
    python setup.py bdist_wheel
}

deploy() {
    pip install -e .
    djm_back
}


init
unit_tests
dist
deploy