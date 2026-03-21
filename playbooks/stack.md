# Stack

Upgrading back-end infrastructure.
Goals:
  * Cost optimization. Monthly bill for 4 CPX21 instances is €40.96.


## OS

Prompt: Upgrading back-end infrastructure on Hetzner for cost optimization. What is the most recommended operating system?

Gemini (best): 
  - OS: Debian: + lowest resource usage, maximum efficiency and stability; - shorter support lifecycle
  - Compute instances: CAX. CAX21: 4 vCPUs / 8 GB RAM.

ChatGPT (fluffy):
  - OS: Ubuntu
  - Compute instances: CPX

## Monitoring stack

Prompt: What is the best monitoring stack for CAX21 / Debian, to see CPU/memory/Node/Postgres usage?

ChatGPT:
  - Prometheus + Grafana + Exporters → Netdata → Beszel 

Gemini:
  - Prometheus + Grafana + Exporters → Netdata

Prompt: What is the easiest monitoring stack to install and operate? I don't need deep debugging, just an ability to monitor endpoints and send an alert if an endpoint is down.

ChatGPT:
  - Uptime Kuma

Gemini:
  - Uptima Kuma

OS stats: Beszel : easiest to operate, lightest on resources.
Endpoints: Uptime Robot. Kuma for DB if required.

## DB

Image to run on Debian: https://hub.docker.com/_/postgres 

## Build pipelines
