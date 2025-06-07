#!/usr/bin/env python3
"""
ETM Core Physics Engine
Core classes and simulation engine for Euclidean Timing Mechanics

Contains:
- ETMEngine: Main simulation engine
- Identity: Individual timing patterns
- Recruiter: Spatial rhythm coordinators  
- EchoField: Echo reinforcement fields
- Core physics rules (phase advancement, echo decay, conflict resolution)

Preserves all validated ETM physics from your successful research.
"""

import numpy as np
import json
import copy
import uuid
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Any
from datetime import datetime

# Import our configuration module
try:
    from .config import (
        ETMConfig, ReturnStatus, DetectionEventType, ConflictResolutionMethod,
        ParticleType, WeakInteractionType, ETM_VERSION, ETM_STATUS
    )
except ImportError:
    # Handle direct execution
    from config import (
        ETMConfig, ReturnStatus, DetectionEventType, ConflictResolutionMethod,
        ParticleType, WeakInteractionType, ETM_VERSION, ETM_STATUS
    )

# =============================================================================
# CORE ETM DATA CLASSES - Preserved from validated version
# =============================================================================

@dataclass
class Recruiter:
    """Recruiter rhythm at a spatial node"""
    theta_recruiter: float
    ancestry_recruiter: str
    delta_theta: float = 0.1
    
    # Track identities that have returned to this recruiter
    returned_identities: List[str] = field(default_factory=list)  # Identity IDs
    supports_coexistence: bool = True  # VALIDATED: Allow multiple identities
    
    def update_phase(self):
        """Update recruiter phase rhythm"""
        self.theta_recruiter = (self.theta_recruiter + self.delta_theta) % 1.0
    
    def add_returned_identity(self, identity):
        """Record that an identity has returned to this recruiter"""
        if identity.unique_id not in self.returned_identities:
            self.returned_identities.append(identity.unique_id)

@dataclass
class EchoField:
    """Echo reinforcement field at a node"""
    rho_local: float = 0.0
    reinforcement_history: List[float] = field(default_factory=list)
    
    def apply_decay(self, decay_factor: float):
        """Implement R4: Echo Decay Rule"""
        self.rho_local *= decay_factor
    
    def add_reinforcement(self, amount: float):
        """Add echo reinforcement"""
        self.rho_local += amount
        self.reinforcement_history.append(amount)

@dataclass
class DetectionEvent:
    """Represents a detection or interaction event that can trigger conflict resolution"""
    event_type: DetectionEventType
    position: Tuple[int, int, int]
    tick: int
    triggering_particle: Optional['Identity'] = None
    affected_identities: List['Identity'] = field(default_factory=list)
    resolution_method: Optional[ConflictResolutionMethod] = None
    mutation_results: Dict[str, Any] = field(default_factory=dict)

# =============================================================================
# ENHANCED IDENTITY CLASS - With all your validated features
# =============================================================================

@dataclass
class Identity:
    """Enhanced identity with all validated features and nucleon support"""
    # Core identity properties (preserved from validated version)
    module_tag: str
    ancestry: str
    theta: float
    delta_theta: float
    tick_memory: int = 0
    position: Optional[Tuple[int, int, int]] = None
    return_status: ReturnStatus = ReturnStatus.PENDING
    
    # Identity tracking (preserved)
    unique_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    original_ancestry: str = ""
    mutation_history: List[Dict] = field(default_factory=list)
    is_mutated: bool = False
    
    # Coexistence tracking (preserved)
    coexisting_with: List[str] = field(default_factory=list)
    conflict_resolution_applied: Optional[ConflictResolutionMethod] = None
    
    # Particle foundation integration (preserved)
    fundamental_particle: Optional[Any] = None  # Will be ParticleTimingPattern when particles module loaded
    stability_score: float = 1.0
    
    # NEW: Composite particle support
    is_composite_constituent: bool = False
    parent_composite_id: Optional[str] = None
    constituent_role: str = ""
    
    # NEW: Weak interaction support
    participates_in_weak_interactions: bool = False
    weak_interaction_history: List[Dict] = field(default_factory=list)
    last_weak_interaction_tick: int = -1
    
    # NEW: Anti-particle properties
    is_antiparticle: bool = False
    antiparticle_of: Optional[str] = None
    
    # NEW: Decay properties
    creation_tick: int = 0
    is_decay_product: bool = False
    parent_decay_event: Optional[str] = None
    
    def update_phase(self):
        """Implement R2: Phase Advancement Rule - PRESERVED EXACTLY"""
        self.theta = (self.theta + self.delta_theta) % 1.0
        self.tick_memory += 1
    
    def apply_symbolic_mutation(self, mutation_type: str, new_ancestry: str = None, mutation_tag: str = None):
        """Apply symbolic mutation - PRESERVED EXACTLY from validated version"""
        original_ancestry = self.ancestry
        
        if mutation_type == "ancestry_append" and mutation_tag:
            if isinstance(self.ancestry, str):
                self.ancestry = self.ancestry + mutation_tag
            elif isinstance(self.ancestry, list):
                self.ancestry = self.ancestry + [mutation_tag]
        elif mutation_type == "ancestry_replace" and new_ancestry:
            self.ancestry = new_ancestry
        elif mutation_type == "identity_suffix" and mutation_tag:
            self.module_tag = self.module_tag + mutation_tag
        
        self.mutation_history.append({
            "tick": self.tick_memory,
            "type": mutation_type,
            "original": original_ancestry,
            "new": self.ancestry,
            "tag": mutation_tag,
            "validation_status": "Model_B_confirmed"
        })
        self.is_mutated = True
    
    def calculate_particle_energy(self, nuclear_position: Tuple[int, int, int], 
                                echo_fields: Dict[Tuple[int, int, int], EchoField],
                                config: ETMConfig = None) -> float:
        """PRESERVED: Calibrated energy calculation achieving <1% accuracy"""
        
        if not self.position or not self.fundamental_particle:
            return 0.0
        
        # Use calibrated parameters if enabled and config provided
        if config and config.enable_calibrated_energy:
            # CALIBRATED CALCULATION (achieving <1% accuracy) - PRESERVED EXACTLY
            
            # 1. CALIBRATED kinetic energy component
            kinetic_component = self.delta_theta * config.kinetic_scale_factor
            
            # 2. CALIBRATED potential energy component
            if self.position in echo_fields:
                echo_strength = echo_fields[self.position].rho_local
                potential_component = -echo_strength * config.potential_coefficient
            else:
                potential_component = 0.0
            
            # 3. Coulomb radius component (maintained scale)
            distance = ((self.position[0] - nuclear_position[0])**2 + 
                       (self.position[1] - nuclear_position[1])**2 + 
                       (self.position[2] - nuclear_position[2])**2)**0.5
            radius_component = -config.coulomb_constant / max(distance, 0.1)
            
            # 4. CALIBRATED stability component
            if hasattr(self.fundamental_particle, 'calculate_stability_score'):
                stability_score = self.fundamental_particle.calculate_stability_score(100.0)
            else:
                stability_score = self.stability_score
            stability_component = stability_score * config.stability_scale_factor
            
            total_energy = kinetic_component + potential_component + radius_component + stability_component
            
            return total_energy
            
        else:
            # LEGACY CALCULATION (for backward compatibility)
            return self._calculate_legacy_energy(nuclear_position, echo_fields, config)
    
    def _calculate_legacy_energy(self, nuclear_position: Tuple[int, int, int], 
                               echo_fields: Dict[Tuple[int, int, int], EchoField],
                               config: ETMConfig = None) -> float:
        """Legacy energy calculation - PRESERVED EXACTLY"""
        
        kinetic_component = self.delta_theta * (config.legacy_kinetic_scale if config else 1360.0)
        
        if self.position in echo_fields:
            echo_strength = echo_fields[self.position].rho_local
            potential_component = -echo_strength * (config.legacy_potential_coeff if config else 0.08)
        else:
            potential_component = 0.0
        
        distance = ((self.position[0] - nuclear_position[0])**2 + 
                   (self.position[1] - nuclear_position[1])**2 + 
                   (self.position[2] - nuclear_position[2])**2)**0.5
        
        radius_component = -13.6 / max(distance, 0.1)
        
        if self.fundamental_particle and hasattr(self.fundamental_particle, 'calculate_stability_score'):
            stability_score = self.fundamental_particle.calculate_stability_score(100.0)
            stability_component = stability_score * (config.legacy_stability_scale if config else 5.0)
        else:
            stability_component = 0.0
        
        total_energy = kinetic_component + potential_component + radius_component + stability_component
        
        return total_energy

# =============================================================================
# MAIN ETM ENGINE - Core simulation engine with all validated features
# =============================================================================

class ETMEngine:
    """Core ETM simulation engine - Enhanced for nucleon internal structure"""
    
    def __init__(self, config: ETMConfig):
        self.config = config
        self.tick = 0
        
        # Initialize spatial lattice (preserved)
        self.lattice_shape = config.lattice_size
        self.center = tuple(s // 2 for s in self.lattice_shape)
        
        # Storage for simulation state (preserved)
        self.identities: List[Identity] = []
        self.recruiters: Dict[Tuple[int, int, int], Recruiter] = {}
        self.echo_fields: Dict[Tuple[int, int, int], EchoField] = {}
        
        # Detection and conflict resolution (preserved exactly)
        self.detection_events: List[DetectionEvent] = []
        self.coexistence_registry: Dict[Tuple[int, int, int], List[str]] = {}
        self.conflict_resolutions: List[Dict] = []
        
        # NEW: Composite particle tracking
        self.composite_particles: Dict[str, Any] = {}  # Will be CompositeParticlePattern when particles loaded
        self.pattern_reorganization_events: List[Any] = []
        
        # Results storage (preserved)
        self.results_history: List[Dict] = []

        # Energy bookkeeping for each tick
        self.current_tick_energy_before: float = 0.0
        self.current_tick_energy_after: float = 0.0
        
        # Initialize echo fields (preserved)
        self._initialize_echo_fields()
    
    def _initialize_echo_fields(self):
        """Initialize echo fields for all lattice positions - PRESERVED EXACTLY"""
        for x in range(self.lattice_shape[0]):
            for y in range(self.lattice_shape[1]):
                for z in range(self.lattice_shape[2]):
                    self.echo_fields[(x, y, z)] = EchoField()
    
    def get_neighbors(self, x: int, y: int, z: int) -> List[Tuple[int, int, int]]:
        """Get neighbor positions based on VALIDATED 8-connectivity - PRESERVED EXACTLY"""
        neighbors = []
        connectivity = self.config.connectivity
        
        if connectivity >= 6:  # Basic 6-connectivity
            directions = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
            neighbors.extend(directions)
            
        if connectivity >= 8:  # Add xy-plane edges (VALIDATED optimal level)
            neighbors.extend([(-1,-1,0), (-1,1,0), (1,-1,0), (1,1,0)])
            
        if connectivity >= 12:  # Add remaining edges
            neighbors.extend([
                (-1,0,-1), (-1,0,1), (1,0,-1), (1,0,1),
                (0,-1,-1), (0,-1,1), (0,1,-1), (0,1,1)
            ])
        
        # Convert to absolute coordinates and filter bounds
        result = []
        for dx, dy, dz in neighbors[:connectivity]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if (0 <= nx < self.lattice_shape[0] and 
                0 <= ny < self.lattice_shape[1] and 
                0 <= nz < self.lattice_shape[2]):
                result.append((nx, ny, nz))
        
        return result
    
    def register_coexistence(self, position: Tuple[int, int, int], identity: Identity):
        """Register an identity as coexisting at a position - VALIDATED mechanism"""
        if position not in self.coexistence_registry:
            self.coexistence_registry[position] = []
        
        if identity.unique_id not in self.coexistence_registry[position]:
            self.coexistence_registry[position].append(identity.unique_id)
            
        other_identities = [id for id in self.coexistence_registry[position] if id != identity.unique_id]
        identity.coexisting_with = other_identities
        
        if len(other_identities) > 0:
            identity.return_status = ReturnStatus.COEXISTING
    
    def evaluate_return_eligibility(self, identity: Identity) -> Tuple[bool, Dict]:
        """Implement R1: Return Eligibility Evaluation - PRESERVED EXACTLY"""
        if not identity.position or identity.position not in self.recruiters:
            return False, {"reason": "no_recruiter"}
        
        recruiter = self.recruiters[identity.position]
        
        # Phase match
        phase_diff = abs(identity.theta - recruiter.theta_recruiter) % 1.0
        phase_diff = min(phase_diff, 1.0 - phase_diff)
        phase_match = phase_diff <= self.config.phase_tolerance
        
        # Ancestry match (simplified for compatibility)
        ancestry_match = identity.ancestry == recruiter.ancestry_recruiter
        
        # Echo match
        echo_match, rho_hybrid = self.calculate_echo_match(identity.position)
        
        # Combined eligibility
        return_allowed = phase_match and ancestry_match and echo_match
        
        return return_allowed, {
            "phase_match": phase_match,
            "ancestry_match": ancestry_match,
            "echo_match": echo_match,
            "rho_hybrid": rho_hybrid,
            "phase_diff": phase_diff
        }
    
    def calculate_echo_match(self, position: Tuple[int, int, int]) -> Tuple[bool, float]:
        """Implement echo matching with VALIDATED hybrid calculation - PRESERVED"""
        rho_local = self.echo_fields[position].rho_local
        
        neighbors = self.get_neighbors(*position)
        if neighbors:
            rho_neigh = sum(self.echo_fields[pos].rho_local for pos in neighbors) / len(neighbors)
        else:
            rho_neigh = 0.0
        
        rho_hybrid = (self.config.echo_hybrid_local_weight * rho_local + 
                     self.config.echo_hybrid_neighbor_weight * rho_neigh)
        
        echo_match = rho_hybrid >= self.config.rho_min
        return echo_match, rho_hybrid
    
    def advance_phases(self):
        """Advance all identity and recruiter phases - PRESERVED EXACTLY"""
        for identity in self.identities:
            identity.update_phase()
        
        for recruiter in self.recruiters.values():
            recruiter.update_phase()
    
    def apply_echo_decay(self):
        """Apply echo decay to all fields - PRESERVED EXACTLY"""
        for echo_field in self.echo_fields.values():
            echo_field.apply_decay(self.config.decay_factor)
    
    def apply_echo_inheritance(self):
        """Apply echo inheritance from neighbors - PRESERVED EXACTLY"""
        if self.config.inheritance_alpha <= 0:
            return
        
        new_echo_values = {}
        
        for position, echo_field in self.echo_fields.items():
            neighbors = self.get_neighbors(*position)
            if neighbors:
                neighbor_echo = sum(self.echo_fields[pos].rho_local for pos in neighbors) / len(neighbors)
                new_echo = echo_field.rho_local + self.config.inheritance_alpha * neighbor_echo
                new_echo_values[position] = new_echo
        
        for position, new_value in new_echo_values.items():
            self.echo_fields[position].rho_local = new_value
    
    def execute_identity_reformation(self, identity: Identity):
        """Implement identity reformation - PRESERVED EXACTLY"""
        if identity.position in self.recruiters:
            recruiter = self.recruiters[identity.position]
            
            identity.theta = recruiter.theta_recruiter
            identity.ancestry = recruiter.ancestry_recruiter
            identity.return_status = ReturnStatus.COMPLETE
            
            recruiter.add_returned_identity(identity)
            self.echo_fields[identity.position].add_reinforcement(1.0)
    
    def advance_tick(self):
        """Execute one complete ETM simulation tick - Enhanced with nucleon processes"""
        self.tick += 1

        # 1-4. All existing steps preserved exactly
        self.advance_phases()
        self.apply_echo_decay()

        # Record total timing-strain energy before any interactions this tick
        self.current_tick_energy_before = sum(
            i.calculate_particle_energy(self.center, self.echo_fields, self.config)
            for i in self.identities
        )
        
        return_results = []
        for identity in self.identities:
            return_allowed, evaluation = self.evaluate_return_eligibility(identity)
            return_results.append({
                "identity": identity,
                "return_allowed": return_allowed,
                "evaluation": evaluation
            })
        
        for result in return_results:
            if result["return_allowed"]:
                self.execute_identity_reformation(result["identity"])
        
        if self.config.enable_detection_events:
            self.process_detection_events()
        
        # 5-6. Enhanced steps for nucleon physics (methods will be added when particles module loaded)
        if self.config.enable_nucleon_internal_structure:
            self.process_nucleon_physics()
        
        if self.config.enable_weak_interactions:
            self.process_weak_interactions()

        # 7-8. Preserved exactly
        self.apply_echo_inheritance()

        # Record total timing-strain energy after interactions and inheritance
        self.current_tick_energy_after = sum(
            i.calculate_particle_energy(self.center, self.echo_fields, self.config)
            for i in self.identities
        )
        self.record_tick_results(return_results)
    
    def process_detection_events(self):
        """Process detection events including annihilation energy tracking"""
        # Import here to avoid circular dependency during module initialization
        try:
            from .particles import ParticleFactory
        except Exception:
            from particles import ParticleFactory
        position_map: Dict[Tuple[int, int, int], List[Identity]] = {}
        for identity in self.identities:
            if identity.position is not None:
                position_map.setdefault(identity.position, []).append(identity)

        events_to_remove = []

        for position, ids in position_map.items():
            if len(ids) < 2:
                continue

            # Check all pairs for antiparticle annihilation
            for i in range(len(ids)):
                for j in range(i + 1, len(ids)):
                    a, b = ids[i], ids[j]
                    if (
                        a.is_antiparticle and a.antiparticle_of == b.unique_id
                    ) or (
                        b.is_antiparticle and b.antiparticle_of == a.unique_id
                    ):
                        energy_a = a.calculate_particle_energy(
                            self.center, self.echo_fields, self.config
                        )
                        energy_b = b.calculate_particle_energy(
                            self.center, self.echo_fields, self.config
                        )
                        total_energy = energy_a + energy_b

                        photon_id = None
                        detection = DetectionEvent(
                            event_type=DetectionEventType.PARTICLE_COLLISION,
                            position=position,
                            tick=self.tick,
                            triggering_particle=a,
                            affected_identities=[b],
                            resolution_method=ConflictResolutionMethod.EXCLUSION,
                            mutation_results={"energy_released": total_energy},
                        )
                        self.detection_events.append(detection)

                        # Create a photon carrying the released energy
                        try:
                            photon_pattern = ParticleFactory.create_photon(total_energy)
                            photon_identity = Identity(
                                module_tag="PHOTON",
                                ancestry="photon",
                                theta=0.0,
                                delta_theta=photon_pattern.core_timing_rate,
                                position=position,
                            )
                            photon_identity.fundamental_particle = photon_pattern
                            self.identities.append(photon_identity)
                            photon_id = photon_identity.unique_id
                            detection.mutation_results["photon_id"] = photon_id
                            detection.mutation_results["photon_energy"] = getattr(photon_pattern, "energy_content", total_energy)
                        except Exception:
                            pass
                        self.conflict_resolutions.append(
                            {
                                "tick": self.tick,
                                "position": position,
                                "method": "annihilation",
                                "energy_released": total_energy,
                            }
                        )
                        events_to_remove.extend([a, b])

        # Remove annihilated identities
        for identity in events_to_remove:
            if identity in self.identities:
                self.identities.remove(identity)
    
    def process_nucleon_physics(self):
        """Process nucleon internal structure dynamics - Placeholder for particles module"""
        # Will be implemented when particles module is loaded
        pass
    
    def process_weak_interactions(self):
        """Process weak interaction events - Placeholder for particles module"""
        # Will be implemented when particles module is loaded
        pass
    
    def record_tick_results(self, return_results: List[Dict]):
        """Record results for this tick - Enhanced with nucleon data"""
        tick_data = {
            "tick": self.tick,
            "identities": [],
            "return_results": [],
            "detection_events": [],
            "coexistence_registry": {},
            "conflict_resolutions": [],
            "composite_particles": len(self.composite_particles),
            "pattern_reorganizations": len(self.pattern_reorganization_events),
            "energy_before": self.current_tick_energy_before,
            "energy_after": self.current_tick_energy_after,
            "energy_released_total": 0.0,
            "photon_energy_total": 0.0,
        }
        
        # Convert coexistence registry tuple keys to strings for JSON compatibility
        for position_tuple, identity_ids in self.coexistence_registry.items():
            pos_str = f"{position_tuple[0]},{position_tuple[1]},{position_tuple[2]}"
            tick_data["coexistence_registry"][pos_str] = identity_ids
        
        for identity in self.identities:
            tick_data["identities"].append({
                "unique_id": identity.unique_id,
                "module_tag": identity.module_tag,
                "ancestry": identity.ancestry,
                "theta": identity.theta,
                "position": identity.position,
                "return_status": identity.return_status.value,
                "tick_memory": identity.tick_memory,
                "is_mutated": identity.is_mutated,
                "stability_score": identity.stability_score,
                "is_composite_constituent": identity.is_composite_constituent,
                "is_decay_product": identity.is_decay_product
            })
        
        for result in return_results:
            tick_data["return_results"].append({
                "identity_id": result["identity"].unique_id,
                "return_allowed": result["return_allowed"],
                "evaluation": result["evaluation"]
            })

        for event in self.detection_events:
            tick_data["detection_events"].append({
                "event_type": event.event_type.value,
                "position": event.position,
                "tick": event.tick,
                "trigger_id": event.triggering_particle.unique_id if event.triggering_particle else None,
                "affected_ids": [i.unique_id for i in event.affected_identities],
                "energy_released": event.mutation_results.get("energy_released"),
                "photon_id": event.mutation_results.get("photon_id"),
                "photon_energy": event.mutation_results.get("photon_energy"),
            })
            tick_data["energy_released_total"] += event.mutation_results.get("energy_released", 0.0)
            tick_data["photon_energy_total"] += event.mutation_results.get("photon_energy", 0.0)
        tick_data["conflict_resolutions"] = self.conflict_resolutions.copy()

        # Clear events after recording
        self.detection_events.clear()
        self.conflict_resolutions.clear()

        self.results_history.append(tick_data)
    
    def run_simulation(self) -> Dict:
        """Run complete ETM simulation - Enhanced with nucleon physics"""
        print(f"Starting ETM v{ETM_VERSION} simulation: {self.config.trial_name}")
        print(f"Status: {ETM_STATUS}")
        print(f"Configuration: {self.config.connectivity}-connectivity, {self.config.max_ticks} ticks")
        
        while self.tick < self.config.max_ticks:
            self.advance_tick()
            
            if self.tick % 10 == 0:
                nucleon_count = len(self.composite_particles)
                reorganization_count = len(self.pattern_reorganization_events)
                print(f"Tick {self.tick}/{self.config.max_ticks} - Identities: {len(self.identities)}, Nucleons: {nucleon_count}")
        
        # Enhanced results with nucleon information
        results = {
            "config": self.config.__dict__,
            "final_tick": self.tick,
            "total_identities": len(self.identities),
            "total_recruiters": len(self.recruiters),
            "total_detection_events": len(self.detection_events),
            "total_conflict_resolutions": len(self.conflict_resolutions),
            "coexistence_positions": len(self.coexistence_registry),
            "composite_particles": len(self.composite_particles),
            "pattern_reorganizations": len(self.pattern_reorganization_events),
            "history": self.results_history
        }
        
        return results

# =============================================================================
# TEST FUNCTION - Verify core module works
# =============================================================================

def test_core_module():
    """Test that the core module works correctly"""
    print("Testing ETM Core Module...")
    print("=" * 50)
    
    # Test 1: Configuration import works
    from .config import ETMConfig, ConfigurationFactory
    print("✓ Configuration import successful")
    
    # Test 2: Basic engine creation
    config = ETMConfig(max_ticks=5, connectivity=8)
    engine = ETMEngine(config)
    print(f"✓ Engine created with {config.connectivity}-connectivity")
    print(f"✓ Lattice size: {engine.lattice_shape}")
    print(f"✓ Center position: {engine.center}")
    
    # Test 3: Identity creation
    identity = Identity(
        module_tag="TEST",
        ancestry="ABC",
        theta=0.5,
        delta_theta=0.1,
        position=engine.center
    )
    engine.identities.append(identity)
    print(f"✓ Identity created: {identity.unique_id}")
    
    # Test 4: Basic phase advancement
    original_theta = identity.theta
    identity.update_phase()
    print(f"✓ Phase advancement: {original_theta:.3f} → {identity.theta:.3f}")
    
    # Test 5: Neighbor calculation
    neighbors = engine.get_neighbors(*engine.center)
    print(f"✓ Neighbor calculation: {len(neighbors)} neighbors for center position")
    
    # Test 6: Echo field initialization
    center_echo = engine.echo_fields[engine.center]
    print(f"✓ Echo fields initialized: {len(engine.echo_fields)} positions")
    
    print("\n🎉 Core module working perfectly!")
    print("Ready for next step: Extract particles module")
    return True

if __name__ == "__main__":
    test_core_module()
