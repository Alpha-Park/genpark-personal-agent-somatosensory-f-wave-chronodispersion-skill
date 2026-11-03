"""
Example Usage: Somatosensory F-Wave Chronodispersion & Proximal Motor Conduction.
Demonstrates zero-dependency calculation of F-wave chronodispersion, proximal conduction time, and motor root scoring.
"""

from client import SomatosensoryFWaveChronodispersionClient


def main():
    client = SomatosensoryFWaveChronodispersionClient()
    print("=== Somatosensory F-Wave Chronodispersion Demo ===")

    # Test Case 1: Healthy synchronous proximal motor nerve conduction (Median nerve)
    res1 = client.evaluate_f_wave(
        f_min_latency_ms=26.4,
        f_max_latency_ms=29.8,
        f_persistence_pct=90.0,
        distal_motor_latency_ms=3.6,
        limb_length_cm=76.0,
        nerve_name="MEDIAN_NERVE"
    )
    print("\nTest Case 1: Normal Proximal Motor Conduction (Median Nerve)")
    print(f"  F-Wave Range: {res1['f_min_latency_ms']} - {res1['f_max_latency_ms']} ms")
    print(f"  Chronodispersion: {res1['f_chronodispersion_ms']} ms | Persistence: {res1['f_persistence_pct']}%")
    print(f"  Proximal Conduction Time: {res1['proximal_conduction_time_ms']} ms")
    print(f"  Proximal Motor Score: {res1['proximal_motor_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Elevated chronodispersion (proximal radiculopathy / demyelination pattern)
    res2 = client.evaluate_f_wave(
        f_min_latency_ms=29.5,
        f_max_latency_ms=38.2,
        f_persistence_pct=52.0,
        distal_motor_latency_ms=4.1,
        nerve_name="ULNAR_NERVE"
    )
    print("\nTest Case 2: Elevated Chronodispersion Pattern (Radicular Dispersion)")
    print(f"  F-Wave Chronodispersion: {res2['f_chronodispersion_ms']} ms | Persistence: {res2['f_persistence_pct']}%")
    print(f"  Proximal Motor Score: {res2['proximal_motor_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
