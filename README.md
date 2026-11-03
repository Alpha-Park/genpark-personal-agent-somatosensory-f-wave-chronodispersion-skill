# Somatosensory F-Wave Chronodispersion Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Electroneuromyography (ENMG) F-wave chronodispersion (Fmax - Fmin in ms), persistence (%), and proximal motor nerve root conduction integrity.

```mermaid
flowchart TD
    SupramaxStim["Supramaximal Distal Motor Nerve Stimulation"] --> OrthoM["Orthodromic Direct Motor Muscle Action Potential (M-Wave)"]
    SupramaxStim --> Antidromic["Antidromic Conduction Ascending Motor Axons to Spinal Cord"]
    Antidromic --> MotoneuronBackfire["Anterior Horn Alpha Motoneuron Recurrent Discharge"]
    MotoneuronBackfire --> LateFWave["Late Recurrent Motor Wave (F-Wave Series)"]
    LateFWave --> ChronoDisp["Chronodispersion Extraction (Fmax - Fmin) & Persistence"]
    ChronoDisp --> ProximalScore["Proximal Motor Nerve Root & Demyelination Score"]
    ProximalScore --> Agent["OpenClaw / Hermes Personal Agent Postural Guarding"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Clinical Neurophysiology Standards**: Implements validated equations for minimal/maximal F-wave latencies, chronodispersion, and central conduction times.
- **Proximal Radiculopathy & Demyelination Screening**: Sensitive detection of proximal nerve root compression or polyneuropathic conduction dispersion.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import SomatosensoryFWaveChronodispersionClient

client = SomatosensoryFWaveChronodispersionClient()
result = client.evaluate_f_wave(
    f_min_latency_ms=26.4,
    f_max_latency_ms=29.8,
    f_persistence_pct=90.0
)
print("Chronodispersion:", result["f_chronodispersion_ms"], "ms")
print("Proximal Motor Score:", result["proximal_motor_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
