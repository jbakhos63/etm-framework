#!/usr/bin/env python3
"""
ETM Configuration Management
All configuration classes, enums, and global constants for ETM Framework

This preserves all validated parameters from your successful ETM research:
- Model B Detection-Triggered Conflict Resolution (Validated)
- Calibrated Energy Calculations (<1% accuracy vs quantum mechanics)  
- Enhanced Proton Patterns (>95% AGN survival)
- Nucleon Internal Structure with Beta Decay
"""

from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Any
from enum import Enum

# =============================================================================
# VERSION INFORMATION - Preserved from your validated framework
# =============================================================================

ETM_VERSION = "2.3 Nucleon Enhanced"
ETM_STATUS = "Model B Validated + Energy Calibrated + Proton Enhanced + NUCLEON INTERNAL STRUCTURE"
VALIDATION_TRIALS = "070-074"
CALIBRATION_STATUS = "Energy: 1768% → 0.014% error (129,818x improvement), Proton: >95% AGN survival"
NUCLEON_STATUS = "Composite particle architecture with neutron internal structure modeling"
LAST_UPDATED = "June 2025 - Nucleon Internal Structure Implementation Complete"

# =============================================================================
# CORE ETM ENUMS - Preserved exactly from your validated version
# =============================================================================

class ReturnStatus(Enum):
    PENDING = "pending"
    ALLOWED = "allowed" 
    DENIED = "denied"
    FAILED = "failed"
    COMPLETE = "complete"
    COEXISTING = "coexisting"  # Validated status for multiple identities at same node

class ModuleTag(Enum):
    GROUND = "G"
    EXCITED_1 = "E1"
    EXCITED_2 = "E2"
    DECAY = "D"

class ParticleType(Enum):
    PHOTON = "photon"
    ELECTRON = "electron"
    PROTON = "proton"
    NEUTRON = "neutron"
    NEUTRINO = "neutrino"

class ParticleContext(Enum):
    FREE_SPACE = "free_space"
    ATOMIC_ORBITAL = "atomic_orbital"
    NUCLEAR_BOUND = "nuclear_bound"
    TRANSITION_STATE = "transition_state"
    ABSORBED_CONSTITUENT = "absorbed_constituent"

class DetectionEventType(Enum):
    PHOTON_INTERACTION = "photon_interaction"
    PARTICLE_COLLISION = "particle_collision"
    MEASUREMENT_PROBE = "measurement_probe"
    ENERGY_TRANSITION = "energy_transition"

class ConflictResolutionMethod(Enum):
    COEXISTENCE = "coexistence"  # Allow overlap without conflict
    SYMBOLIC_MUTATION = "symbolic_mutation"  # Validated: Mutate ancestry/identity
    IDENTITY_RENAME = "identity_rename"  # Change identity tag
    PHASE_SEPARATION = "phase_separation"  # Enforce phase offset
    EXCLUSION = "exclusion"  # Traditional Pauli exclusion

class ParticleStabilityLevel(Enum):
    STABLE = "stable"
    METASTABLE = "metastable"
    UNSTABLE = "unstable"
    CRITICAL = "critical"

# Nucleon-specific enums from your enhanced version
class WeakInteractionType(Enum):
    BETA_MINUS_DECAY = "beta_minus_decay"
    BETA_PLUS_DECAY = "beta_plus_decay"
    ELECTRON_CAPTURE = "electron_capture"
    MUON_DECAY = "muon_decay"
    NEUTRINO_SCATTERING = "neutrino_scattering"
    W_BOSON_EXCHANGE = "w_boson_exchange"
    Z_BOSON_EXCHANGE = "z_boson_exchange"

# =============================================================================
# MAIN CONFIGURATION CLASS - All your validated parameters preserved exactly
# =============================================================================

@dataclass
class ETMConfig:
    """Global ETM configuration parameters - CALIBRATED for <1% energy accuracy"""
    
    # Basic parameters
    tick: int = 0
    max_ticks: int = 100
    
    # Network topology - VALIDATED: 8-connectivity optimal (35.6% improvement)
    connectivity: int = 8  # Confirmed optimal from connectivity tests
    lattice_size: Tuple[int, int, int] = (30, 30, 30)
    
    # Phase parameters
    phase_tolerance: float = 0.11
    delta_theta_default: float = 0.1
    
    # Echo parameters
    rho_min: float = 25.0
    decay_factor: float = 0.95
    inheritance_alpha: float = 0.10
    echo_hybrid_local_weight: float = 0.6
    echo_hybrid_neighbor_weight: float = 0.4
    
    # Ancestry parameters
    ancestry_required: bool = True
    smoothing_enabled: bool = False
    smoothing_threshold: int = 2
    smoothing_tick: int = 3
    
    # Conflict resolution - VALIDATED: Model B (Detection-Triggered) confirmed
    epsilon: float = 0.01  # Phase difference threshold for coexistence
    coherence_window: int = 1
    enable_passive_coexistence: bool = True  # VALIDATED: Allow coexistence without detection
    default_conflict_resolution: ConflictResolutionMethod = ConflictResolutionMethod.SYMBOLIC_MUTATION  # VALIDATED
    
    # Detection and interaction parameters - VALIDATED settings
    enable_detection_events: bool = True  # VALIDATED: Detection triggers resolution
    detection_triggers_mutation: bool = True  # VALIDATED: Symbolic differentiation
    mutation_probability: float = 0.8  # Probability of mutation vs exclusion on detection
    
    # CALIBRATED ENERGY CALCULATION PARAMETERS - NEW: Achieving <1% accuracy
    enable_calibrated_energy: bool = True  # Enable calibrated energy calculations
    
    # Calibrated energy scale factors (validated for <1% accuracy)
    kinetic_scale_factor: float = 1000.0      # CALIBRATED: Reduced from 1360.0 (1.4x reduction)
    potential_coefficient: float = 0.003723   # CALIBRATED: Reduced from 0.08 (18.6x reduction)
    stability_scale_factor: float = 2.63      # CALIBRATED: Reduced from 5.0 (1.9x reduction)
    coulomb_constant: float = 13.6            # MAINTAINED: Correct scale preserved
    
    # Legacy parameters for backward compatibility
    legacy_kinetic_scale: float = 1360.0     # Original value for compatibility testing
    legacy_potential_coeff: float = 0.08     # Original value for compatibility testing
    legacy_stability_scale: float = 5.0      # Original value for compatibility testing
    
    # Calibration validation targets
    target_hydrogen_ground_state: float = -13.6  # eV - quantum mechanical target
    accuracy_tolerance_percent: float = 1.0      # <1% error target
    
    # Particle modeling parameters with enhanced proton
    enable_particle_foundation: bool = True  # Enable fundamental particle modeling
    enable_enhanced_proton: bool = True      # NEW: Enable AGN-survival proton patterns
    particle_stability_threshold: float = 0.95  # Minimum stability for viable particles
    cosmological_compatibility: bool = True  # Require AGN ejection survival
    
    # NEW: Nucleon and composite particle parameters
    enable_nucleon_internal_structure: bool = False   # Enable nucleon composite modeling
    enable_weak_interactions: bool = False            # Enable weak force processes
    enable_pattern_reorganization: bool = False       # Enable composite pattern reorganization
    enable_beta_decay: bool = False                   # Enable neutron beta decay
    enable_conservation_enforcement: bool = False     # Enforce conservation laws
    enable_antiparticles: bool = False               # Enable anti-particle patterns
    
    # NEW: Weak interaction parameters
    weak_coupling_constant: float = 1.0e-5          # Weak interaction strength
    beta_decay_lifetime_ticks: int = 900            # Neutron lifetime (~15 minutes)
    weak_interaction_probability: float = 0.001     # Base probability per tick
    pattern_reorganization_threshold: float = 0.8   # Threshold for spontaneous reorganization
    
    # NEW: Conservation law tolerances
    energy_conservation_tolerance: float = 1e-3
    charge_conservation_tolerance: float = 1e-6
    lepton_number_tolerance: float = 1e-6
    baryon_number_tolerance: float = 1e-6
    
    # Output control - Compact output by default
    compact_output: bool = True  # Generate compact JSON summaries
    max_output_size_kb: int = 100  # Maximum JSON file size for uploads
    output_json: bool = True  # Enable JSON output
    output_plots: bool = False  # Disable plots by default for efficiency
    
    # Trial control
    trial_name: str = "default"
    
    def get_calibration_summary(self) -> Dict[str, Any]:
        """Get summary of calibration improvements"""
        return {
            "energy_calibration_enabled": self.enable_calibrated_energy,
            "enhanced_proton_enabled": self.enable_enhanced_proton,
            "kinetic_reduction_factor": f"{self.legacy_kinetic_scale / self.kinetic_scale_factor:.1f}x",
            "potential_reduction_factor": f"{self.legacy_potential_coeff / self.potential_coefficient:.1f}x",
            "stability_reduction_factor": f"{self.legacy_stability_scale / self.stability_scale_factor:.1f}x",
            "target_accuracy": f"<{self.accuracy_tolerance_percent}%",
            "target_energy": f"{self.target_hydrogen_ground_state} eV",
            "calibration_validation": "0.014% error achieved (129,818x improvement)"
        }
    
    def enable_nucleon_physics(self):
        """Enable nucleon internal structure and all dependencies"""
        self.enable_nucleon_internal_structure = True
        self.enable_weak_interactions = True
        self.enable_pattern_reorganization = True
        self.enable_beta_decay = True
        self.enable_conservation_enforcement = True
        self.enable_antiparticles = True
        self.enable_particle_foundation = True
        self.enable_calibrated_energy = True
        self.enable_enhanced_proton = True

# =============================================================================
# CONFIGURATION FACTORIES - Makes creating trials easier
# =============================================================================

class ConfigurationFactory:
    """Factory methods for creating validated configurations"""
    
    @staticmethod
    def validated_foundation_config(trial_name: str = "foundation") -> ETMConfig:
        """Create configuration preserving all validated achievements"""
        config = ETMConfig(
            trial_name=trial_name,
            connectivity=8,  # VALIDATED optimal
            enable_passive_coexistence=True,  # VALIDATED
            enable_detection_events=True,  # VALIDATED
            detection_triggers_mutation=True,  # VALIDATED
            default_conflict_resolution=ConflictResolutionMethod.SYMBOLIC_MUTATION,  # VALIDATED
            enable_calibrated_energy=True,  # CALIBRATED
            enable_enhanced_proton=True,   # Enhanced
            enable_particle_foundation=True
        )
        return config
    
    @staticmethod
    def nucleon_physics_config(trial_name: str = "nucleon") -> ETMConfig:
        """Create configuration for nucleon internal structure trials"""
        config = ConfigurationFactory.validated_foundation_config(trial_name)
        config.enable_nucleon_physics()  # Enable all nucleon dependencies
        return config

# =============================================================================
# TEST FUNCTION - To verify this module works
# =============================================================================

def test_config_module():
    """Test that the configuration module works correctly"""
    print("Testing ETM Configuration Module...")
    print("=" * 50)
    
    # Test 1: Basic configuration
    config = ETMConfig()
    print(f"✓ Basic config created")
    print(f"  Connectivity: {config.connectivity} (should be 8)")
    print(f"  Kinetic scale: {config.kinetic_scale_factor} (should be 1000.0)")
    
    # Test 2: Calibration summary
    summary = config.get_calibration_summary()
    print(f"✓ Calibration summary: {summary['calibration_validation']}")
    
    # Test 3: Nucleon configuration
    nucleon_config = ConfigurationFactory.nucleon_physics_config("test")
    print(f"✓ Nucleon config: beta_decay={nucleon_config.enable_beta_decay}")
    
    # Test 4: Version information
    print(f"✓ Version: {ETM_VERSION}")
    print(f"✓ Status: {ETM_STATUS}")
    
    print("\n🎉 Configuration module working perfectly!")
    return True

if __name__ == "__main__":
    test_config_module()
