#!/bin/bash

service nginx start
gunicorn eshop.wsgi