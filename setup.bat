@echo off

rem  set __COMPAT_LAYER=RunAsInvoker  
 REGEDIT.EXE  /S  "%~dp0backend\regestry.reg"
"%~dp0backend\ViviSetup.exe"


