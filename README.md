collectd_graphite_fix
=====================

Graphite writer plugin changed it's target when we upgraded to collectd 5.3.
This move the whisper files to the new location so you can preserve history.
Worked for us, no guarantees.

The Issue:
----------

From the collectd mailing list:

```
On Wed, Apr 24, 2013 at 08:15:27PM -0300, Nico wrote:
> In 5.2.0 many variables use to end in ".value' In 5.3.0 this is no
> longer present. This is good !! but i cant find an option in the
> configuration to remove this from 5.2.0 or to add it in 5.3.0

"value" in this case is the name of the "data source". Whether it is
added or not is controlled by the "AlwaysAppendDS" option.

Unfortunately it was broken in 5.2.0. This was tracked in issue 214 [*]
and fixed in version 5.2.1.

Best regards,
—octo
```
