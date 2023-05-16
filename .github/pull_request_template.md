# Submitting Pull Requests

## General

 - [ ] Make sure you use [semantic commit messages](https://dev.to/hornet_daemon/git-commit-patterns-5dm7).
       Examples: `"fix(google): Fixed foobar bug"`, `"feat(accounts): Added foobar feature"`.
 - [ ] All Python code must formatted using Black, and clean from pep8 and isort issues.
 - [ ] If your changes are significant, please update `ChangeLog.rst`.

 ## Channels Specifics

In case you add a new channel:

- [ ] Make sure unit tests are available.
- [ ] Add documentation to `docs/channels.rst`.
-  [ ] Add an entry to the list of supported channels over at `docs/overview.rst`.