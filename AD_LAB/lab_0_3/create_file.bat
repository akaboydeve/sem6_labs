@echo off
for /l %%i in (1,1,25) do (
    echo # This is p%%i.py > p%%i.py
)
echo Files created successfully.