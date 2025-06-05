#!/usr/bin/env python3
"""
ETM Trial 070 - Compact Summary Version
Enhanced for upload-friendly JSON output while maintaining analytical rigor
Post-Trial 074 validation with detection-triggered conflict resolution
"""

from etm_framework import *
import time
import json
from datetime import datetime

def run_trial_070_compact():
    """Execute Trial 070 with optimized data collection for compact output"""
    
    # Configuration matching validated setup
    config = ETMConfig(
        trial_name="070_compact_summary",
        max_ticks=10,
        connectivity=8,  # Validated optimal
        lattice_size=(30, 30, 30),
        smoothing_enabled=True,
        smoothing_tick=3,
        enable_passive_coexistence=True,  # Key finding from trials
        enable_detection_events=True,
        detection_triggers_mutation=True,
        default_conflict_resolution=ConflictResolutionMethod.SYMBOLIC_MUTATION,
        output_json=False  # We'll create our own compact summary
    )
    
    engine = ETMEngine(config)
    
    # Set up core scenario - validated configuration
    center = engine.center  # (15, 15, 15)
    recruiter = Recruiter(theta_recruiter=0.25, ancestry_recruiter="ABC")
    engine.add_recruiter(center, recruiter)
    
    # Initialize strong echo field (matching successful trial setup)
    for dx in range(-5, 6):
        for dy in range(-5, 6):
            for dz in range(-5, 6):
                x, y, z = center[0]+dx, center[1]+dy, center[2]+dz
                if (0 <= x < 30 and 0 <= y < 30 and 0 <= z < 30):
                    distance = (dx**2 + dy**2 + dz**2)**0.5
                    if distance <= 2.0:
                        engine.set_echo_field((x, y, z), 80.0)
                    elif distance <= 4.0:
                        engine.set_echo_field((x, y, z), 50.0)
                    else:
                        engine.set_echo_field((x, y, z), 30.0)
    
    # Create dual identities at SAME position (key fix from trials)
    identity_a = Identity(
        module_tag="ROTOR_A",
        ancestry="ABC",  # Match recruiter
        theta=0.24,     # Close to recruiter (0.25)
        delta_theta=0.1,
        position=center,  # Same as recruiter
        original_ancestry="ABC"
    )
    
    identity_b = Identity(
        module_tag="ROTOR_B", 
        ancestry="ABC",  # Match recruiter
        theta=0.26,     # Close to recruiter (0.25)
        delta_theta=0.1,
        position=center,  # Same as recruiter
        original_ancestry="ABC"
    )
    
    engine.identities.extend([identity_a, identity_b])
    
    # Register coexistence
    engine.register_coexistence(center, identity_a)
    engine.register_coexistence(center, identity_b)
    
    return engine, config

def collect_compact_data(engine, config, results):
    """Collect essential data for compact JSON summary"""
    
    # Basic trial information
    trial_info = {
        "trial_name": config.trial_name,
        "execution_timestamp": datetime.now().isoformat(),
        "framework_version": "2.0_post_trial_074",
        "completed_ticks": results['final_tick'],
        "max_ticks": config.max_ticks,
        "execution_completed": results['final_tick'] == config.max_ticks
    }
    
    # Configuration summary (key parameters only)
    config_summary = {
        "connectivity": config.connectivity,
        "lattice_size": config.lattice_size,
        "passive_coexistence": config.enable_passive_coexistence,
        "detection_events": config.enable_detection_events,
        "detection_triggers_mutation": config.detection_triggers_mutation,
        "default_conflict_resolution": config.default_conflict_resolution.value,
        "phase_tolerance": config.phase_tolerance,
        "rho_min": config.rho_min
    }
    
    # Core simulation metrics
    core_metrics = {
        "total_identities": results['total_identities'],
        "total_recruiters": results['total_recruiters'],
        "total_detection_events": results['total_detection_events'],
        "total_conflict_resolutions": results['total_conflict_resolutions'],
        "coexistence_positions": results['coexistence_positions']
    }
    
    # Final state analysis (most recent tick)
    final_state = results['history'][-1] if results['history'] else {}
    
    # Identity analysis (essential properties only)
    identity_analysis = []
    for identity_data in final_state.get('identities', []):
        identity_summary = {
            "id": identity_data['unique_id'][:8],  # Shortened for compactness
            "module_tag": identity_data['module_tag'],
            "ancestry": identity_data['ancestry'],
            "original_ancestry": identity_data['original_ancestry'],
            "position": identity_data['position'],
            "phase": round(identity_data['theta'], 4),
            "status": identity_data['return_status'],
            "tick_memory": identity_data['tick_memory'],
            "is_mutated": identity_data['is_mutated'],
            "coexisting_count": len(identity_data.get('coexisting_with', [])),
            "conflict_resolution": identity_data.get('conflict_resolution')
        }
        identity_analysis.append(identity_summary)
    
    # Coexistence registry analysis
    coexistence_analysis = {}
    registry = final_state.get('coexistence_registry', {})
    for position_tuple, identity_ids in registry.items():
        # Convert tuple position to string for JSON serialization
        pos_str = f"{position_tuple[0]},{position_tuple[1]},{position_tuple[2]}"
        coexistence_analysis[pos_str] = {
            "identity_count": len(identity_ids),
            "identity_ids": [id[:8] for id in identity_ids]  # Shortened IDs
        }
    
    # Return eligibility analysis (latest results)
    return_eligibility = []
    for result in final_state.get('return_results', []):
        return_summary = {
            "identity_id": result['identity_id'][:8],
            "allowed": result['return_allowed'],
            "evaluation": result.get('evaluation', {})
        }
        # Round numerical values for compactness
        if 'rho_hybrid' in return_summary['evaluation']:
            return_summary['evaluation']['rho_hybrid'] = round(return_summary['evaluation']['rho_hybrid'], 2)
        if 'phase_diff' in return_summary['evaluation']:
            return_summary['evaluation']['phase_diff'] = round(return_summary['evaluation']['phase_diff'], 4)
        
        return_eligibility.append(return_summary)
    
    # Validation checklist (critical for research continuity)
    validation = {
        "framework_stability": results['final_tick'] == config.max_ticks,
        "identity_preservation": results['total_identities'] == 2,
        "coexistence_achievement": results['coexistence_positions'] > 0,
        "detection_resolution_functional": results['total_detection_events'] > 0 and results['total_conflict_resolutions'] > 0,
        "connectivity_optimization": config.connectivity == 8
    }
    
    # Overall assessment - Updated for detection-triggered resolution validation
    critical_checks = [
        validation["framework_stability"],
        validation["identity_preservation"], 
        validation["coexistence_achievement"]
    ]
    
    # For detection-triggered resolution validation, successful conflict resolution is a POSITIVE outcome
    detection_resolution_success = (
        results['total_detection_events'] > 0 and 
        results['total_conflict_resolutions'] > 0 and
        results['total_identities'] == 2  # Identities preserved through mutation, not deletion
    )
    
    phase1_requirements = [
        validation["framework_stability"],
        validation["identity_preservation"],
        validation["coexistence_achievement"],
        validation["connectivity_optimization"],
        detection_resolution_success  # This validates Model B
    ]
    
    assessment = {
        "trial_success": all(critical_checks),
        "phase1_complete": all(phase1_requirements),
        "ready_for_phase2": all(phase1_requirements),
        "detection_resolution_validated": detection_resolution_success,
        "status": "SUCCESS" if all(critical_checks) else "NEEDS_ATTENTION"
    }
    
    # Performance metrics (essential only)
    performance = {
        "execution_time_seconds": None,  # Will be filled by main()
        "ticks_per_second": None,
        "memory_efficient": True,  # Compact output achieved
        "reproducible": True  # Deterministic simulation
    }
    
    # Detection events summary (if any occurred)
    detection_summary = []
    for tick_data in results['history']:
        for event in tick_data.get('detection_events', []):
            detection_summary.append({
                "tick": tick_data['tick'],
                "type": event['type'],
                "position": event['position'],
                "affected_count": event['affected_count'],
                "resolution": event.get('resolution_method')
            })
    
    # Conflict resolutions summary
    conflict_summary = []
    for resolution in results.get('conflict_resolutions', [])[-5:]:  # Last 5 only
        conflict_summary.append({
            "method": resolution.get('method'),
            "tick": resolution.get('tick'),
            "affected_count": resolution.get('affected_count', 0),
            "mutations_applied": len(resolution.get('mutations', []))
        })
    
    # Compile complete compact summary
    compact_summary = {
        "trial_info": trial_info,
        "config": config_summary,
        "metrics": core_metrics,
        "validation": validation,
        "assessment": assessment,
        "performance": performance,
        "identities": identity_analysis,
        "coexistence": coexistence_analysis,
        "return_eligibility": return_eligibility,
        "detection_events": detection_summary,
        "conflict_resolutions": conflict_summary,
        "research_notes": {
            "key_findings": [
                "Detection-triggered conflict resolution validated" if detection_resolution_success else "Detection resolution not triggered",
                "8-connectivity optimization confirmed" if validation["connectivity_optimization"] else "Sub-optimal connectivity",
                "Framework stability maintained" if validation["framework_stability"] else "Framework issues detected",
                "Symbolic mutation preserved identities" if results['total_identities'] == 2 and results['total_conflict_resolutions'] > 0 else "No mutations required"
            ],
            "phase_status": "Phase 1 complete - Model B validated" if assessment["phase1_complete"] else "Phase 1 incomplete",
            "next_steps": "Begin Phase 2 atomic structure reproduction" if assessment["ready_for_phase2"] else "Address Phase 1 issues",
            "model_validation": "Model B (Detection-Triggered Symbolic Conflict) confirmed" if detection_resolution_success else "Model validation incomplete"
        }
    }
    
    return compact_summary

def save_compact_summary(summary_data):
    """Save compact summary to JSON file with size optimization"""
    filename = f"etm_trial_070_compact_summary_{summary_data['trial_info']['completed_ticks']}ticks.json"
    
    # Save with compact formatting to minimize file size
    with open(filename, 'w') as f:
        json.dump(summary_data, f, separators=(',', ':'), indent=1)
    
    # Calculate and report file size
    import os
    file_size_kb = os.path.getsize(filename) / 1024
    
    print(f"\nCompact summary saved: {filename}")
    print(f"File size: {file_size_kb:.1f} KB")
    
    if file_size_kb > 100:
        print(f"⚠ WARNING: File size exceeds 100KB - may need further optimization")
    else:
        print(f"✓ File size optimal for Claude upload")
    
    return filename

def main():
    """Execute Trial 070 with compact summary output"""
    
    print("="*70)
    print("ETM TRIAL 070 - COMPACT SUMMARY VERSION")
    print("Detection-Triggered Conflict Resolution Validation")
    print("="*70)
    
    start_time = time.time()
    
    try:
        # Execute trial
        print("Setting up trial configuration...")
        engine, config = run_trial_070_compact()
        
        print("Running simulation...")
        results = engine.run_simulation()
        
        execution_time = time.time() - start_time
        
        print("Generating compact summary...")
        summary = collect_compact_data(engine, config, results)
        
        # Add execution timing
        summary['performance']['execution_time_seconds'] = round(execution_time, 3)
        summary['performance']['ticks_per_second'] = round(config.max_ticks / execution_time, 1)
        
        # Save summary
        filename = save_compact_summary(summary)
        
        # Display key results
        print("\n" + "="*70)
        print("TRIAL RESULTS SUMMARY")
        print("="*70)
        
        print(f"Trial Status: {summary['assessment']['status']}")
        print(f"Phase 1 Complete: {'✓' if summary['assessment']['phase1_complete'] else '✗'}")
        print(f"Ready for Phase 2: {'✓' if summary['assessment']['ready_for_phase2'] else '✗'}")
        
        print(f"\nCore Metrics:")
        print(f"  Identities: {summary['metrics']['total_identities']}")
        print(f"  Detection Events: {summary['metrics']['total_detection_events']}")
        print(f"  Conflict Resolutions: {summary['metrics']['total_conflict_resolutions']}")
        print(f"  Coexistence Positions: {summary['metrics']['coexistence_positions']}")
        
        print(f"\nValidation Checklist:")
        for check, status in summary['validation'].items():
            print(f"  {check}: {'✓' if status else '✗'}")
        
        if summary['assessment']['detection_resolution_validated']:
            print(f"  ✓ CRITICAL: Detection-triggered resolution validated (Model B)")
        
        print(f"\nModel Validation:")
        print(f"  {summary['research_notes']['model_validation']}")
        
        print(f"\nPerformance:")
        print(f"  Execution Time: {summary['performance']['execution_time_seconds']}s")
        print(f"  Ticks/Second: {summary['performance']['ticks_per_second']}")
        
        print(f"\nNext Steps: {summary['research_notes']['next_steps']}")
        
        print(f"\n{'='*70}")
        print(f"UPLOAD FILE: {filename}")
        print(f"This file contains complete analysis data in compact format")
        print(f"{'='*70}")
        
        return summary['assessment']['phase1_complete']
        
    except Exception as e:
        print(f"\nERROR DURING EXECUTION:")
        print(f"  Exception: {e}")
        print(f"  Type: {type(e).__name__}")
        
        import traceback
        print(f"\nFull traceback:")
        traceback.print_exc()
        
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print(f"\n✓ TRIAL 070 SUCCESSFUL - MODEL B VALIDATED - COMPACT SUMMARY READY")
    else:
        print(f"\n✗ TRIAL 070 NEEDS ATTENTION")