---
description: 'This page explains the error "SSH client not received any data for last xx ms!" seen in the Connectivity Report.'
---

# Connectivity Report -- `SSH client not received any data for last xx ms!`

If you encounter this error message during discovery, it indicates that the SSH client has not received any data from the network device for a certain period. This could be due to various factors, including:

- Slow response from network devices caused by high CPU or memory usage, configuration issues, or network errors.

- Congested network causing packet loss, latency, or jitter between the SSH client and the network device.

- Discovery services being overloaded with other tasks, preventing the SSH client from sending or receiving data.

## How To Improve Performance of Discovery Services

There are several ways to enhance the performance of discovery services and reduce the occurrence of this error message. Some suggestions include:

- Creating more workers to manage additional concurrent SSH sessions and distribute the workload among them (available since `6.0`).

- Limiting the number of devices processed by each worker to prevent overloading and potential timeouts or errors (available since `6.3.1`).

- Contacting the Support or Solution Architecture team to explore configuration or architectural changes that can optimize the performance and scalability of the discovery services.

We are actively identifying tasks that are not optimized, which may cause the discovery services to stall and hinder the processing of SSH data. Your feedback and cooperation in reporting any issues encountered with our discovery services are highly appreciated.

If you are experiencing a significant number of these error messages, please reach out to us through our support portal. We will investigate the issue promptly and provide a resolution as soon as possible.
