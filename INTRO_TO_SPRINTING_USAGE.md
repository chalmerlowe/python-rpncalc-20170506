# RPN Calculator Engine for Python Workshops

This project is meant to be used as a sample open-source project for the [Intro to Sprinting](https://github.com/chalmerlowe/intro_to_sprinting) course by [chalmerlowe](https://github.com/chalmerlowe). The point of the project is to have a simple-to-understand workspace so that the focus can be on the *process* of contributing rather than the details of the project being committed to.

Once the workshop is done, you might want to keep a copy of the repo, but it is recommended you make an entirely new copy from the base repo for each workshop.


## Using the Project for a Workshop

Because a workshop requires making commits, the repository is designed to be duplicated (not forked) for a particular instance of the workshop.

Note that students will be making pull requests to this, and their initial PRs should be for simple functionality; if you keep using the same project eventually the "easy" tasks cease to exist.

### Initial Setup

1. Clone the project locally
1. Create a new project in GitHub for your workshop instance (fx python-rpncalc-2017-03-17)
1. Push the local clone to your new project

### Optional: set up (Travis-CI)[https://travis-ci.org]

1. Create an account if necessary
1. Click the "+" button to create a new link between Travis-CI and your repo
1. Click the toggle for your copy of the rpncalc repo to enable automatic integration
1. Go back to your project in GitHub and click "Settings"
1. Click on "Integrations and Services" - you should see Travis-CI in the list
1. Click on "Travis-CI"
1. Click on "Test Service"
1. Go back to Travis-CI and you should see the project building and testing on several versions of Python

## During the Workshop

Students will be making pull requests to your repo. Make sure you are familiar with approving pull requests beforehand. If you are using Travis-CI, it is recommended you only accept pull requests that pass all integration testing and that you check for new test functions for any code changes that are contributed.
