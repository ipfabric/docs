---
description: Current API may return an arbitrary count of 100000000 for large collections (tables). 
---

# Iterating Over Large Collections

Current API may return an arbitrary `count` of `100000000` for large collections (tables). This doesn't mean that the collection doesn't contain more records. We have an open change request to augment this behavior and return `null` in such cases (as returned value cannot be trusted).

We recommend implementing "blind iteration" even before mentioned change is implemented as it will allow to fetch all records with the current as well as future API implementation.

!!! example "Blind iteration pseudo-code"

    ```ruby
    limit = 500
    start = 0
    returned_count = limit

    while returned_count == limit do
      batch, returned_count = fetch_data(start, limit)
      start += returned_count
     
      # process returned batch
    end
    ```

Blind iteration was already introduced into [IP Fabric Python SDK v5.0.1](https://gitlab.com/ip-fabric/integrations/python-ipfabric/-/releases/v5.0.1).
