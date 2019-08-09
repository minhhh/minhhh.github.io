Title: Setup nodejs development environment with conda and nodeenv
Date: 2019-08-09 00:00
Author: Ha.Minh
Category: Programming
Tags: nodejs, conda, nodeenv

When you want to develop your nodejs project on different node versions, you have some tools to help you install multiple node versions such as `nave`, `nvm`, `n`. However, this is still not as nice as `virtualenv` in Python, where you have completely isolated environments so one project does not affect the others.

Fortunately, there is a tool called [nodeenv](https://github.com/ekalinin/nodeenv) that can help you create isolated node.js environment the same way as `virtualenv`. Using `nodeenv` is already good enough, but if you don't want to store the virtualenv folder in the same project folder, then you would need some other tool to manage virtualenv folders globally. There are 2 options: `conda` and `pipenv`. `pipenv` does not integrate very well with shell scripts because you have to start a separate pipenv shell. `conda` is perfect because it can manage all kinds of packages, not just Python or nodejs and it's very compatible with shell scripts.

In conclusion, using `conda` and `nodeenv` is a much better choice than just `nave` or `nvm`.
