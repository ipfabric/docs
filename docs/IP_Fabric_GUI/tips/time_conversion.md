---
description: In this section, we describe how IP Fabric handles Time Conversion.
---

# Times Stored in IP Fabric

IP Fabric stores times in two different formats;
_Absolute Time_ or _Relative Time_ depending on the type of data.

## Absolute Time

This is also known as an _Epoch_ or _Unix timestamp_ and is stored in milliseconds
that have elapsed since 00:00:00 UTC on 1 January 1970.

- **Inventory --> End of Life Milestones**:
  - _End of Sale_: `endSale`
  - _End of Maintenance_: `endMaintenance`
  - _End of Support_: `endSupport`
- **Management --> Discovery History**:
  - _Last discovery time_: `ts`
- **Management --> Configuration**:
  - _Last Change At_: `lastChangeAt`
  - _Last Check At_: `lastCheckAt`
- **Discovery Snapshot** (`GET /api/{api_version}/snapshots`):
  - _Start Time_: `tsStart`
  - _End Time_: `tsEnd`

!!! example "Converting millisecond timestamp to ISO date with Python"

    ```python
    import datetime

    ts = 1348876800000  # milliseconds

    # datetime does not accept milliseconds so must divide by 1,000:
    dt = datetime.datetime.utcfromtimestamp(ts/1000).replace(tzinfo=datetime.timezone.utc)
    print(dt.isoformat())  # >>> '2012-09-29T00:00:00+00:00'
    ```

## Relative Time

Relative time (stored in seconds) is the amount of time that has elapsed and does not represent an exact timestamp.

- **Inventory --> Devices**:
  - _Uptime_: `uptime` (relative to the boot time of the device at the time the command was run on the device.)
- **Technology --> Routing --> \*** :
  - **Routes**:
    - _Age_: `nhLowestAge`
  - **Routing Protocols**:
    - _Session Time_ or _Uptime_: `currStateTime`

!!! note "Relative time does not change."

    This is relative to the time that the command was run on the device and does not change. Example:

    > Device reported uptime of `120 Days 5 Hours` when `show version` was run.<br>

    Viewing that Snapshot on a day or week later will also show `120 Days 5 Hours`.

!!! example "Converting time interval in seconds to human readable form with Python"

    ```python
    import datetime

    ts = 200700  # seconds

    dt = datetime.timedelta(seconds=ts)
    print(str(dt))  # >>> '2 days, 7:45:00'
    ```

## IP Fabric Time Conversion

Time conversion in IP Fabric is done in the frontend and is also formatted when exporting to CSV.
The data returned via the API will always be returned in milliseconds or seconds.
This can differ from other time conversion websites as an example from [epochconverter.com](https://www.epochconverter.com/):

Time Conversion (in seconds):

| Human-readable Time |                    IP Fabric | [epochconverter.com](https://www.epochconverter.com/) |
| ------------------- | ---------------------------: | ----------------------------------------------------: |
| 1 minute            |                           60 |                                                    60 |
| 1 hour              |                        3,600 |                                                 3,600 |
| 1 day               |                       86,400 |                                                86,400 |
| 1 week              |                      604,800 |                                               604,800 |
| 1 month             | 2,629,800<br/>(30.4375 days) |                            2,629,743<br/>(30.44 days) |
| 1 year              | 31,557,600<br/>(365.25 days) |                          31,556,926<br/>(365.24 days) |
