This script downloads the old revisions of each proxy and deletes them from apigee.

The script first checks the revision numbers of each environmnet in an organization, then finds the lowest deployed revision from all the environmnet reviions, then it retains 2 lower revisions of that revision. other lower revisions it downloads to loacl system and then delete from apigee.

It asks IP of managemnet server, organization name and sysadmin username and password as input for the action.

As its a python script, required environment and modules should have been setup.
