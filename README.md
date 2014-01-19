# Sqwiggle Notifier for Wercker

Send a message to a Sqwiggle room.

### Options

* `token` (required) Your Sqwiggle token.
* `room-id` (required) The id of the Sqwiggle room.
* `passed-message` (optional) The message which will be shown on a passed build or deploy.
* `failed-message` (optional) The message which will be shown on a failed build or deploy.
* `passed-notify` (optional, default: `false`) If this is `true` the passed build/deploy message will make Sqwiggle notify the user.
* `failed-notify` (optional, default: `true`) If this is `true` the passed build/deploy message will make Sqwiggle notify the user.
* `on` (optional, default: `always`) When should this step send a message. Possible values: `always` and `failed`.

### Example

Add SQWIGGLE_TOKEN as deploy target or application environment variable.

```yaml
build:
  after-steps:
    - sqwiggle-notify:
        token: $SQWIGGLE_TOKEN
        room-id: id
```
