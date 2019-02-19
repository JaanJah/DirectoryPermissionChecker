@ECHO OFF
TITLE: DirectoryPermissionChecker
SET /P UserInputPath=<dirPath.txt
accesschk "%USERNAME%" %UserInputPath%
PAUSE