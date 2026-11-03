---
name: genpark-personal-agent-somatosensory-f-wave-chronodispersion-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Electroneuromyography (ENMG) F-wave chronodispersion (Fmax - Fmin in ms), persistence (%), and proximal motor nerve root conduction integrity.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Somatosensory F-Wave Chronodispersion Skill

A sovereign personal agent capability for evaluating antidromic motor nerve activation, anterior horn alpha motoneuron recurrent firing, F-wave minimal latency ($F_{min}$), F-wave chronodispersion ($F_{disp} = F_{max} - F_{min}$), and proximal radicular conduction.

## Core Capabilities
- **F-Wave Chronodispersion Analysis**: Quantifies conduction velocity range ($F_{disp} = F_{max} - F_{min}\text{ in ms}$, normative: $2.5 - 5.5\text{ ms}$) across motor axon pools.
- **Proximal Conduction Time**: Estimates central spinal travel latency ($\frac{F - M - 1}{2}$).
- **F-Wave Persistence Calculation**: Tracks trial repeatability ($\ge 70\%$) to detect early motor axon conduction block.
- **Ergonomic Radicular Guarding**: Screens for thoracic outlet and cervical/lumbar nerve root impingement during long sedentary sitting.

## Fast Invocation
```python
from client import SomatosensoryFWaveChronodispersionClient

client = SomatosensoryFWaveChronodispersionClient()
res = client.evaluate_f_wave(
    f_min_latency_ms=26.4,
    f_max_latency_ms=29.8,
    f_persistence_pct=90.0
)
print("F-Wave Chronodispersion:", res["f_chronodispersion_ms"], "ms")
print("Proximal Motor Score:", res["proximal_motor_score"], "/ 100")
```
