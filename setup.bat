@echo on
pip install paramiko
start /B python bootfile_syncer.py
ssh kipr@10.68.3.75
