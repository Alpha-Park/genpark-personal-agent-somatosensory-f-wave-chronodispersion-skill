"""
MCP Server for Somatosensory F-Wave Chronodispersion Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating F-wave minimal latency, chronodispersion, and persistence.
"""

import sys
import json
from typing import Dict, Any
from client import SomatosensoryFWaveChronodispersionClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_f_wave",
                "description": "Calculates Electroneuromyography (ENMG) F-wave chronodispersion (Fmax - Fmin in ms), persistence (%), and proximal motor conduction score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "f_min_latency_ms": {
                            "type": "number",
                            "description": "Minimal F-wave latency in milliseconds (e.g. 26.5 ms, normative 24-31 ms)."
                        },
                        "f_max_latency_ms": {
                            "type": "number",
                            "description": "Maximal F-wave latency in milliseconds (e.g. 30.2 ms)."
                        },
                        "f_persistence_pct": {
                            "type": "number",
                            "description": "F-wave persistence percentage over >= 20 stimuli (e.g. 85.0%, normative >= 70%)."
                        },
                        "distal_motor_latency_ms": {
                            "type": "number",
                            "description": "Distal motor latency in milliseconds (default: 3.8 ms).",
                            "default": 3.8
                        },
                        "limb_length_cm": {
                            "type": "number",
                            "description": "Tested limb length in centimeters (default: 75.0 cm).",
                            "default": 75.0
                        },
                        "nerve_name": {
                            "type": "string",
                            "description": "Tested motor nerve (default: MEDIAN_NERVE).",
                            "default": "MEDIAN_NERVE"
                        }
                    },
                    "required": ["f_min_latency_ms", "f_max_latency_ms", "f_persistence_pct"]
                }
            }
        ]
    }


def handle_request(client: SomatosensoryFWaveChronodispersionClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_f_wave":
            res = client.evaluate_f_wave(
                f_min_latency_ms=float(args.get("f_min_latency_ms", 27.0)),
                f_max_latency_ms=float(args.get("f_max_latency_ms", 30.5)),
                f_persistence_pct=float(args.get("f_persistence_pct", 85.0)),
                distal_motor_latency_ms=float(args.get("distal_motor_latency_ms", 3.8)),
                limb_length_cm=float(args.get("limb_length_cm", 75.0)),
                nerve_name=str(args.get("nerve_name", "MEDIAN_NERVE"))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = SomatosensoryFWaveChronodispersionClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
