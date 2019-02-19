TITLE: DirectoryPermissionChecker
ECHO Enter directory:
SET /P UserInputPath=<dirPath.txt

ECHO ON
ECHO UserInputPath
accesschk "%USERNAME%" %UserInputPath%
PAUSE