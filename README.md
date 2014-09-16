# Frasco-Tasks

Adds the possibility to run actions in the background using [rq](http://python-rq.org/).
Requires [Frasco-Redis](https://github.com/frascoweb/frasco-redis).

Feature name: *tasks*

## Queuing actions to be run in the background

The *enqueue* action allows you to enqueue actions to be run later by a worker.
These actions will be run out of a request context and thus cannot depend on it.

Options:

  - *action*: the action name (default option)

All other options will be forwarded to the enqueued action.

## Running a worker

The feature provides a *worker* command which allows to start a worker. Multiple
workers can be started if the work is heavy.

    $ frasco worker