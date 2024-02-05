---
description: SSH client not received any data for last xx ms! errors in Connectivity Report explanation
---

# Connectivity Report -- `SSH client not received any data for last xx ms!`

If you encounter this error message while running discovery, it means that the SSH client has not received any data from the network device for a certain period. This can be caused by various factors, such as:

- Slow response from network devices due to high CPU or memory usage, configuration issues, or network errors.

- Congested network that causes packet loss, latency, or jitter between the SSH client and the network device.

- Discovery services being overloaded with other tasks and prevent the SSH client from sending or receiving data.

## How to Improve the Performance of Discovery Services

There are some ways to improve the performance of discovery services and reduce the occurrence of this error message. Some of them are:

- Create more workers to handle more concurrent SSH sessions and distribute the workload among them (available since 6.0).

- Limit the number of devices processed by each worker to avoid overloading them and causing timeouts or errors (available since 6.3.1).

Contact the Support or Solution Architect team for changes in the discovery services configuration or architecture that can optimize the performance and scalability.

We are actively searching for not optimized tasks that can cause the discovery services to be stuck and prevent them from processing SSH data. We appreciate your feedback and cooperation in reporting any issues you encounter with our discovery services.

If you have an extensive number of these error messages, please contact us through our support portal. We will investigate the issue and provide you with a solution as soon as possible.
