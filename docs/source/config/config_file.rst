Config File
===========

.. contents:: Contents

.. raw:: html

   <br />
   <hr>

Description
~~~~~~~~~~~

TTL time values are **integer seconds**.
All settings in the config file affect the client and the server behaviour both, except those in the **SERVER** section, which affect only the behaviour of the server.

.. raw:: html

   <br />
   <hr>


Sections
~~~~~~~~

CLIENT
------

| **limit:** *integer - default:* **64**
| The amount of active concurrent requests to Yahoo servers.
|
| **timeout:** *integer - default:* **2**
| The amount of time in seconds to wait for each response.

.. raw:: html

   <br />
   <hr>


SERVER
------

| **host:** *string - default:* **localhost**
| The host name on which the YFrake server listens on.
|
| **port:** *integer - default:* **8888**
| The port number on which the YFrake server listens on.
|
| **backlog:** *integer - default:* **128**
| The number of unaccepted connections that the system will allow before refusing new connections.

.. raw:: html

   <br />
   <hr>


CACHE_SIZE
----------

| **max_entries:** *integer - default:* **1024**
| The max number of entries in the cache before the cache begins to evict LRU entries.
|
| **max_entry_size:** *integer - default:* **1**
| The max memory usage for a single cache entry in megabytes.
| A request is not cached if the response is larger than this value.
|
| **max_memory:** *integer - default:* **64**
| The max memory usage of entries in megabytes before the cache begins to evict LRU entries.

.. raw:: html

   <br />
   <hr>


CACHE_TTL_GROUPS
----------------

| **override:** *string - default:* **false**
| If **false**, the individual TTL value of each endpoint is used.
| If **true**, the group TTL value of the endpoints is used.
|
| **short_ttl:** *integer - default:* **0**
| Defines the group TTL value for the *CACHE_TTL_SHORT* section.
|
| **long_ttl:** *integer - default:* **0**
| Defines the group TTL value for the *CACHE_TTL_LONG* section.

.. raw:: html

   <br />
   <hr>


CACHE_TTL_SHORT
---------------

| **historical_prices:** *integer - default:* **60**
| **detailed_summary:** *integer - default:* **60**
| **financials:** *integer - default:* **60**
| **insights:** *integer - default:* **60**
| **key_statistics:** *integer - default:* **60**
| **market_summary:** *integer - default:* **60**
| **news:** *integer - default:* **60**
| **options:** *integer - default:* **60**
| **price_overview:** *integer - default:* **60**
| **quotes_overview:** *integer - default:* **60**
| **trending_symbols:** *integer - default:* **60**

.. raw:: html

   <br />
   <hr>


CACHE_TTL_LONG
--------------

| **balance_statements:** *integer - default:* **3600**
| **calendar_events:** *integer - default:* **3600**
| **cashflow_statements:** *integer - default:* **3600**
| **company_overview:** *integer - default:* **3600**
| **currencies:** *integer - default:* **3600**
| **earnings:** *integer - default:* **3600**
| **earnings_history:** *integer - default:* **3600**
| **earnings_trend:** *integer - default:* **3600**
| **esg_chart:** *integer - default:* **3600**
| **esg_scores:** *integer - default:* **3600**
| **fund_ownership:** *integer - default:* **3600**
| **income_statements:** *integer - default:* **3600**
| **insider_holders:** *integer - default:* **3600**
| **insider_transactions:** *integer - default:* **3600**
| **institution_ownership:** *integer - default:* **3600**
| **major_holders:** *integer - default:* **3600**
| **purchase_activity:** *integer - default:* **3600**
| **quote_type:** *integer - default:* **3600**
| **ratings_history:** *integer - default:* **3600**
| **recommendation_trend:** *integer - default:* **3600**
| **recommendations:** *integer - default:* **3600**
| **sec_filings:** *integer - default:* **3600**
| **shares_outstanding:** *integer - default:* **3600**
| **validate_symbols:** *integer - default:* **3600**