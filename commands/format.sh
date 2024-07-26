#!bin/bash

djlint ./templates --reformat --format-js --indent-js 2 --format-css --indent-css 2 --indent 2 --use-gitignore --profile "django"
