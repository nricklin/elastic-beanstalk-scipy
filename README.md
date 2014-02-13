elastic-beanstalk-scipy
=======================

Getting scipy to work on elastic beanstalk with Python 2.7.

This package will compile scipy from source (which in turn requries getting a fortran compiler onto the beanstalk instance).  It takes a long time, and is not suitable for actual deployment.  BUT, you can do this once, then tarball up the `/opt/python/run/venv` virutal environment and use that for faster deployment.

Run:

```
eb init
```
Building scipy will take forever on a micro instance due to cpu throttling, so change the instance type to
a small:

Edit the `.elasticbeanstalk/optionsettings` file and change `InstanceType=t1.micro` to `InstanceType=m1.small`.

Then propagate those settings to elastic beanstalk:

```
eb update
```

Then create the environment and deploy the application:
```
eb start
``` 

