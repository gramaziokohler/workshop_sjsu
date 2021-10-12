@ECHO OFF

CALL conda activate sjsu >nul 2>&1
IF %ERRORLEVEL% neq 0 GOTO conda_not_initilized

GOTO update_sjsu

:conda_not_initilized
CALL %userprofile%\Anaconda3\condabin\conda activate sjsu >nul 2>&1
IF %ERRORLEVEL% neq 0 GOTO conda_not_found

GOTO update_sjsu

:conda_not_found
ECHO CONDA not found! Cannot update.
PAUSE
EXIT /B %errorlevel%

:update_sjsu
ECHO Updating COMPAS framework...
python -m pip install --no-deps --force-reinstall https://github.com/compas-dev/compas/archive/gltf_update.zip#egg=compas
PAUSE
