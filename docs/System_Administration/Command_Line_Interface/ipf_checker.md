---
description: This section provides a guide how to use `ipf-checker` tool to check IP Fabric system health.
---

# ipf-checker

!!! info "Before Upgrading to `v7.5`"

    The upcoming `v7.5` release introduces a new PostgreSQL-based database, which brings updated hardware requirements.
    To ensure stability and optimal performance after the upgrade, we strongly recommend **using directly attached SSD or NVMe storage**.

    To evaluate your current system's readiness, please run the hardware assessment tool manually using the following command:

    ```
    sudo ipf-checker -d -s
    ```

    Please share the results with our Customer Support team. As performance baselines are still being established, we will need to review each result individually.

    You can provide the results by:

    1. **Generating a Techsupport file** with System logs only after running the command, or

    2. **Copying the terminal output** into a text file.

    Please ensure you create a ticket in our [Customer Support Portal](https://support.ipfabric.io) and attach the results file for our analysis.

!!! example "Disk benchmark example"

    ![Example disk benchmark output](../../images/miscellaneous/System_Administration-Command_Line_Interface_ipf_checker_disk_benchmark.webp){ align=left }

The `ipf-checker` is a Python script, which reports whether the hardware requirements,
environment checks and dependencies are all met by the IP Fabric appliance to ensure smooth operation.

It can display the results in a clean, readable table. It also logs every result to a log file for further inspection.

!!! note "Log file location"

    The log file is located at `/var/log/ipf/ipf-checker/ipf-checker.log`.
    
    It gets attached to the **Techsupport** file, for inspection by our Customer Support team.

## Use

Execute shell command `ipf-checker` and use options if needed.

```shell
ipf-checker [-h] [-q] [-c] [-d [TIMEOUT_MINUTES]] [-b [username] [password] | -t [x-api-token] | -a [access-token] | -s]

Resource validation tool for the IP Fabric appliance that displays a table in the terminal and shows the results of various environment checks in real time.

options:
  -h, --help            show this help message and exit
  -q, --quiet           Quiet option for ipf-checker with no output in console.
  -c, --no-color        No color or style output in console.
  -d [TIMEOUT_MINUTES], --disk-benchmark [TIMEOUT_MINUTES]
                        Perform a read and write disk benchmark on the machine. An optional argument can be passed to specify the timeout in minutes.
  -b [username] [password], --basic [username] [password]
                        Passing basic credentials for calling IP Fabric endpoints.
  -t [x-api-token], --x-api-token [x-api-token]
                        Passing X-API-TOKEN for calling IP Fabric endpoints.
  -a [access-token], --access-token [access-token]
                        Passing basic credentials for calling IP Fabric endpoints.
  -s, --skip-auth       Skipping tests that need authentication.
```

!!! example "Results table example"

    The script will generate a table with the results of the checks performed.

    ![Example ipf-chekcer output](../../images/miscellaneous/System_Administration-Command_Line_Interface_ipf_checker_full_table_pt1.webp){ align=left }

    ![Example ipf-chekcer output](../../images/miscellaneous/System_Administration-Command_Line_Interface_ipf_checker_full_table_pt2.webp){ align=left }

## Environment variables

In your home directory, you can create the `.ipf-checker/env` file, which can
contain any of the following environment variables:

```bash
IPF_CHECKER_LOG_LEVEL= # default is INFO
IPF_CHECKER_TOKEN=
IPF_CHECKER_DISK_BENCHMARK_TIMEOUT= # default is 45
```

If the token is set in an environment variable, it will be used automatically when executing the script. Shell authentication arguments override the token.

## Generating API Token

An API token is required when executing the script with authenticated tests enabled. You can generate the token in the IP Fabric UI.

There is an `ipf-checker` role you can choose for the token, ensuring the tool has access only to the necessary endpoints and nothing more.

!!! info "Token generation"

    The API token can be generated in the IP Fabric UI by going to **Settings** -> **Integrations** -> **API Tokens** 
    and clicking on the **Generate Token** button. Copy the token and use it with the `-t` option or 
    set it in the `.ipf-checker/env` file as `IPF_CHECKER_TOKEN`.

    ![Example token geneartion](../../images/miscellaneous/System_Administration-Command_Line_Interface_ipf_checker_token.webp)
