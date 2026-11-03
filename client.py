"""
Somatosensory F-Wave Chronodispersion & Proximal Motor Conduction Engine.
Provides deterministic, zero-dependency modeling of minimal/maximal F-wave latencies,
F-wave chronodispersion (Fmax - Fmin in ms), persistence (%), and proximal radicular axonal integrity.
"""

from typing import Dict, Any, List, Optional


class SomatosensoryFWaveChronodispersionClient:
    """
    Deterministic client for calculating F-Wave Chronodispersion and Proximal Conduction.
    Assesses anterior horn alpha motoneuron antidromic recurrent firing,
    conduction velocity heterogeneity across large motor axons, and proximal nerve root demyelination.
    """

    def __init__(self):
        pass

    def evaluate_f_wave(
        self,
        f_min_latency_ms: float,
        f_max_latency_ms: float,
        f_persistence_pct: float,
        distal_motor_latency_ms: float = 3.8,
        limb_length_cm: float = 75.0,
        nerve_name: str = "MEDIAN_NERVE"
    ) -> Dict[str, Any]:
        """
        Calculates F-wave chronodispersion: F_disp = F_max - F_min.
        Normative values (Median / Ulnar nerve, limb length approx 70-80 cm):
        - F_min latency: 24.0 - 31.0 ms
        - F_disp (chronodispersion): 2.5 - 5.5 ms
        - Persistence: >= 70.0%
        """
        if f_min_latency_ms <= 0 or f_max_latency_ms <= 0:
            return {"error": "F-wave latencies must be strictly positive"}
        if f_max_latency_ms < f_min_latency_ms:
            return {"error": "Maximal F-wave latency cannot be less than minimal latency"}
        if f_persistence_pct < 0 or f_persistence_pct > 100:
            return {"error": "F-wave persistence must be between 0% and 100%"}

        # 1. F-Wave Chronodispersion (ms)
        f_disp_ms = round(f_max_latency_ms - f_min_latency_ms, 2)

        # 2. Estimated Central / Proximal Conduction Time (F - M - 1) / 2
        f_central_time_ms = round((f_min_latency_ms - distal_motor_latency_ms - 1.0) / 2.0, 2)

        # 3. Proximal Motor Root & Axonal Health Score (0 - 100)
        score = 80.0
        if 2.5 <= f_disp_ms <= 5.2:
            score += 10.0
        elif f_disp_ms > 7.5:
            score -= 28.0  # Markedly desynchronized motor conduction
        elif f_disp_ms > 6.0:
            score -= 15.0
        elif f_disp_ms < 1.0:
            score -= 5.0  # Restricted sample / poor axon recruitment

        if f_persistence_pct >= 80.0:
            score += 10.0
        elif f_persistence_pct >= 65.0:
            score += 5.0
        elif f_persistence_pct < 40.0:
            score -= 25.0  # Profound motor conduction block
        elif f_persistence_pct < 60.0:
            score -= 12.0

        if 24.0 <= f_min_latency_ms <= 31.5:
            score += 5.0
        elif f_min_latency_ms > 34.0:
            score -= 15.0

        f_score = round(min(100.0, max(5.0, score)), 1)

        if f_score >= 85.0 and f_disp_ms <= 5.5 and f_persistence_pct >= 70.0:
            tier = "OPTIMAL_PROXIMAL_MOTOR_CONDUCTION"
            interp = f"Synchronous F-wave transmission (Fmin {f_min_latency_ms} ms, Chronodispersion {f_disp_ms} ms, Persistence {f_persistence_pct}%); intact anterior horn and proximal root conduction."
            guidance = "Superior neuromuscular motor unit synchrony. No evidence of proximal demyelination or radicular conduction slowing."
        elif f_disp_ms > 6.5 or f_persistence_pct < 50.0:
            tier = "ELEVATED_CHRONODISPERSION_DEMODULATION"
            interp = f"Prolonged F-wave chronodispersion ({f_disp_ms} ms > 5.5 ms) or low persistence ({f_persistence_pct}%); indicative of motor axon conduction velocity dispersion, demyelination, or proximal radiculopathy."
            guidance = "Proximal motor conduction heterogeneity detected. Screen for cervical/lumbar radicular impingement or inflammatory neuropathy."
        else:
            tier = "MILD_PROXIMAL_LATENCY_DELAY"
            interp = f"Mild F-wave latency extension (Fmin {f_min_latency_ms} ms, Central time {f_central_time_ms} ms); acceptable chronodispersion ({f_disp_ms} ms)."
            guidance = "Monitor upper limb ergonomics; maintain thoracic-cervical spinal mobility to prevent neural compression."

        return {
            "nerve_name": nerve_name,
            "f_min_latency_ms": f_min_latency_ms,
            "f_max_latency_ms": f_max_latency_ms,
            "f_chronodispersion_ms": f_disp_ms,
            "f_persistence_pct": f_persistence_pct,
            "distal_motor_latency_ms": distal_motor_latency_ms,
            "proximal_conduction_time_ms": f_central_time_ms,
            "proximal_motor_score": f_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
