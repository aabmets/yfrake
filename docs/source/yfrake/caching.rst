Caching
=======

YFrake includes a **TLRU** cache for the client and the server objects to speed up consecutive identical requests to the same endpoints over a period of time.
The default time-to-live *(TTL)* values have been found to be optimal through testing.

Caching can be disabled either individually for each endpoint by setting their TTL value to zero or in groups by enabling the override setting and leaving the relevant group TTL value to zero.
