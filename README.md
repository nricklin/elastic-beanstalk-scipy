elastic-beanstalk-scipy
=======================

Getting scipy to work on elastic beanstalk with Python 2.7

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

