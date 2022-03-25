# Error: Resource Conflict

This error only shows up when a user tries to start a job for the second
time (a specific task like discovery, maintenance, unload/upload
snapshot) that is already scheduled.

Only one job can be executed at the time, so for example, if discovery
is running and you will schedule snapshot unload and then attempt to
unload the same snapshot for the second time, you will get this error.
