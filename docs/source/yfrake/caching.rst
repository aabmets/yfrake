Caching
=======

YFrake includes a fast in-memory **TLRU** cache for the client and the server objects to speed up consecutive identical requests to the same endpoints over a period of time.
The default time-to-live *(TTL)* values have been found to be optimal through testing.

Caching can be disabled either individually for each endpoint by setting their TTL value to zero or in groups
by enabling the group override setting and leaving the relevant group TTL value to zero.

This cache does not persist over program restarts. If the user desires to use something more permanent,
it is suggested to use a library like `diskcache`_.

.. _diskcache: https://grantjenks.com/docs/diskcache/