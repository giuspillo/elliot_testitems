from elliot.run import run_experiment
import argparse
import os

parser = argparse.ArgumentParser(description="Run sample main.")
parser.add_argument('--config', type=str, default='testitems_setting')
args = parser.parse_args()

os.system("find . -name '.DS_Store' -type f -delete")
run_experiment(f"config_files/{args.config}.yml")