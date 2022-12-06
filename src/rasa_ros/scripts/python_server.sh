#!/bin/bash
BOT_DIR=$( cd -- "$(dirname "${0}")" >/dev/null 2>&1 ; pwd -P )

cd "${BOT_DIR}/../Cogrob_rasa_midterm"
conda deactivate
python3 callback_server.py
