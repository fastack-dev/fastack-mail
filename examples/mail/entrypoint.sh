#!/bin/bash

sleep 5

uvicorn app.main:app --workers 2 --host "0.0.0.0" --port 6700
