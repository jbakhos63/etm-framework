#!/usr/bin/env python3
"""
Euclidean Timing Mechanics (ETM) Framework - Enhanced Version
Comprehensive implementation with detection-triggered conflict resolution
Incorporates findings from Trials 070-074 supporting Model B (Detection-Triggered Symbolic Conflict)
Version: 1.1 - Updated for Detection-Based Pauli Exclusion
"""

import numpy as np
import json
import matplotlib.pyplot as plt
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Any, Union
from enum import Enum
import copy
import uuid

# =============================================================================
# CORE ETM TYPES AND ENUMS
# =============================================================================

class ReturnStatus(Enum):
    PENDING = "pending"
    ALLOWED = "allowed" 
    DENIED = "denied"
    FAILED = "failed"
    COMPLETE = "complete"
    COEXISTING = "coexisting"  # New status for multiple identities at same node

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
    SYMBOLIC_MUTATION = "symbolic_mutation"  # Mutate ancestry/identity
    IDENTITY_RENAME = "identity_rename"  # Change identity tag
    PHASE_SEPARATION = "phase_separation"  # Enforce phase offset
    EXCLUSION = "exclusion"  # Traditional Pauli exclusion

@dataclass
class ETMConfig:
    """Global ETM configuration parameters"""
    # Basic parameters
    tick: int = 0
    max_ticks: int = 100
    
    # Network topology - Updated to 8-connectivity based on optimization results
    connectivity: int = 8  # Optimal from connectivity tests
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
    
    # Conflict resolution - Updated based on Trial results
    epsilon: float = 0.01  # Phase difference threshold for coexistence
    coherence_window: int = 1
    enable_passive_coexistence: bool = True  # Allow coexistence without detection
    default_conflict_resolution: ConflictResolutionMethod = ConflictResolutionMethod.COEXISTENCE
    
    # Detection and interaction parameters
    enable_detection_events: bool = True
    detection_triggers_mutation: bool = True
    mutation_probability: float = 0.8  # Probability of mutation vs exclusion on detection
    
    # Trial control
    trial_name: str = "default"
    output_json: bool = True
    output_plots: bool = True

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

@dataclass  
class NodePattern:
    """Single node's timing pattern within a particle module"""
    relative_position: Tuple[int, int, int]  # Position relative to particle center
    timing_rate: float  # Node's individual timing rate (0 <= r <= 1)
    phase_offset: float = 0.0  # Initial phase offset from particle center
    role: str = "standard"  # e.g., "core", "edge", "propagation_front"

@dataclass
class ParticleModule:
    """Complete particle definition as a pattern of node timing settings"""
    particle_type: ParticleType
    context: ParticleContext
    energy_level: str = "ground"  # e.g., "ground", "1s", "2p", "excited_1"
    
    # Spatial pattern definition
    node_patterns: List[NodePattern] = field(default_factory=list)
    center_offset: Tuple[int, int, int] = (0, 0, 0)  # Offset from geometric center
    
    # Motion properties (for non-photonic particles)
    velocity: Optional[Tuple[float, float, float]] = None  # Spatial velocity vector
    momentum: Optional[Tuple[float, float, float]] = None
    
    # Timing synchronization
    master_phase: float = 0.0  # Overall particle phase
    master_delta_theta: float = 0.1  # Overall particle rhythm rate
    
    # Interaction properties
    absorption_targets: List[ParticleType] = field(default_factory=list)
    emission_products: List['ParticleModule'] = field(default_factory=list)
    transition_rules: Dict[str, str] = field(default_factory=dict)  # energy_level transitions
    
    # Detection properties
    detection_signature: str = ""  # Unique signature for detection events
    triggers_detection: bool = True  # Whether this particle can trigger detection
    
    # Metadata
    creation_tick: int = 0
    ancestry_signature: str = ""
    unique_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    
    def get_affected_positions(self, center_position: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
        """Get all lattice positions this particle affects"""
        positions = []
        for pattern in self.node_patterns:
            abs_pos = (
                center_position[0] + pattern.relative_position[0],
                center_position[1] + pattern.relative_position[1], 
                center_position[2] + pattern.relative_position[2]
            )
            positions.append(abs_pos)
        return positions
    
    def update_master_phase(self):
        """Update the particle's overall phase rhythm"""
        self.master_phase = (self.master_phase + self.master_delta_theta) % 1.0

@dataclass
class Identity:
    """Modular identity according to ETM axioms A1-A7"""
    # Core identity properties (A1, A3)
    module_tag: str
    ancestry: str
    
    # Phase rhythm properties (A1, A2)
    theta: float  # Current phase [0.0, 1.0)
    delta_theta: float  # Phase advance per tick
    
    # State tracking
    tick_memory: int = 0
    position: Optional[Tuple[int, int, int]] = None
    return_status: ReturnStatus = ReturnStatus.PENDING
    
    # Identity tracking and differentiation
    unique_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    original_ancestry: str = ""  # Track original ancestry before mutations
    mutation_history: List[Dict] = field(default_factory=list)
    is_mutated: bool = False
    
    # Coexistence tracking
    coexisting_with: List[str] = field(default_factory=list)  # IDs of coexisting identities
    conflict_resolution_applied: Optional[ConflictResolutionMethod] = None
    
    # Particle module reference (if this identity represents a particle)
    particle_module: Optional[ParticleModule] = None
    
    def update_phase(self):
        """Implement R2: Phase Advancement Rule"""
        self.theta = (self.theta + self.delta_theta) % 1.0
        self.tick_memory += 1
        
        # Update particle module if present
        if self.particle_module:
            self.particle_module.update_master_phase()
    
    def apply_symbolic_mutation(self, mutation_type: str, new_ancestry: str = None, mutation_tag: str = None):
        """Apply symbolic mutation for conflict resolution"""
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
        
        # Record mutation history
        self.mutation_history.append({
            "tick": self.tick_memory,
            "type": mutation_type,
            "original": original_ancestry,
            "new": self.ancestry,
            "tag": mutation_tag
        })
        self.is_mutated = True

@dataclass
class Recruiter:
    """Recruiter rhythm at a spatial node"""
    theta_recruiter: float
    ancestry_recruiter: str
    delta_theta: float = 0.1
    
    # Track identities that have returned to this recruiter
    returned_identities: List[str] = field(default_factory=list)  # Identity IDs
    supports_coexistence: bool = True  # Whether this recruiter allows multiple identities
    
    def update_phase(self):
        """Update recruiter phase rhythm"""
        self.theta_recruiter = (self.theta_recruiter + self.delta_theta) % 1.0
    
    def add_returned_identity(self, identity: Identity):
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

# =============================================================================
# CORE ETM ENGINE - Enhanced with Detection-Triggered Conflict Resolution
# =============================================================================

class ETMEngine:
    """
    Core ETM simulation engine implementing all axioms and rules
    Enhanced with detection-triggered conflict resolution based on Trial results 070-074
    """
    
    def __init__(self, config: ETMConfig):
        self.config = config
        self.tick = 0
        
        # Initialize spatial lattice
        self.lattice_shape = config.lattice_size
        self.center = tuple(s // 2 for s in self.lattice_shape)
        
        # Storage for simulation state
        self.identities: List[Identity] = []
        self.recruiters: Dict[Tuple[int, int, int], Recruiter] = {}
        self.echo_fields: Dict[Tuple[int, int, int], EchoField] = {}
        
        # Detection and conflict resolution tracking
        self.detection_events: List[DetectionEvent] = []
        self.coexistence_registry: Dict[Tuple[int, int, int], List[str]] = {}  # position -> identity IDs
        self.conflict_resolutions: List[Dict] = []
        
        # Results storage
        self.results_history: List[Dict] = []
        
        # Initialize echo fields
        self._initialize_echo_fields()
    
    def _initialize_echo_fields(self):
        """Initialize echo fields for all lattice positions"""
        for x in range(self.lattice_shape[0]):
            for y in range(self.lattice_shape[1]):
                for z in range(self.lattice_shape[2]):
                    self.echo_fields[(x, y, z)] = EchoField()
    
    def get_neighbors(self, x: int, y: int, z: int) -> List[Tuple[int, int, int]]:
        """Get neighbor positions based on 8-connectivity (optimized setting)"""
        neighbors = []
        connectivity = self.config.connectivity
        
        if connectivity >= 6:  # Basic 6-connectivity
            directions = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
            neighbors.extend(directions)
            
        if connectivity >= 8:  # Add xy-plane edges (optimal level)
            neighbors.extend([(-1,-1,0), (-1,1,0), (1,-1,0), (1,1,0)])
            
        if connectivity >= 12:  # Add remaining edges
            neighbors.extend([
                (-1,0,-1), (-1,0,1), (1,0,-1), (1,0,1),
                (0,-1,-1), (0,-1,1), (0,1,-1), (0,1,1)
            ])
        
        # Higher connectivity levels available but 8 is optimal
        
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
        """Register an identity as coexisting at a position"""
        if position not in self.coexistence_registry:
            self.coexistence_registry[position] = []
        
        if identity.unique_id not in self.coexistence_registry[position]:
            self.coexistence_registry[position].append(identity.unique_id)
            
        # Update identity's coexistence tracking
        other_identities = [id for id in self.coexistence_registry[position] if id != identity.unique_id]
        identity.coexisting_with = other_identities
        
        if len(other_identities) > 0:
            identity.return_status = ReturnStatus.COEXISTING
    
    def get_coexisting_identities(self, position: Tuple[int, int, int]) -> List[Identity]:
        """Get all identities coexisting at a position"""
        if position not in self.coexistence_registry:
            return []
        
        coexisting = []
        for identity_id in self.coexistence_registry[position]:
            identity = self.get_identity_by_id(identity_id)
            if identity:
                coexisting.append(identity)
        
        return coexisting
    
    def get_identity_by_id(self, identity_id: str) -> Optional[Identity]:
        """Get identity by unique ID"""
        for identity in self.identities:
            if identity.unique_id == identity_id:
                return identity
        return None
    
    def add_particle_module(self, particle_module: ParticleModule, center_position: Tuple[int, int, int]):
        """Add a complete particle module to the simulation"""
        # Create identity for the particle
        identity = Identity(
            module_tag=particle_module.particle_type.value,
            ancestry=particle_module.ancestry_signature,
            theta=particle_module.master_phase,
            delta_theta=particle_module.master_delta_theta,
            position=center_position,
            particle_module=particle_module,
            original_ancestry=particle_module.ancestry_signature
        )
        
        # Apply node patterns to lattice
        affected_positions = particle_module.get_affected_positions(center_position)
        for i, pattern in enumerate(particle_module.node_patterns):
            if i < len(affected_positions):
                pos = affected_positions[i]
                if self._is_valid_position(pos):
                    # Set node timing rate (this would affect the node's behavior)
                    # For now, we'll represent this through echo field modulation
                    current_echo = self.echo_fields[pos].rho_local
                    timing_influence = pattern.timing_rate * 50.0  # Scale factor
                    self.echo_fields[pos].rho_local = max(current_echo, timing_influence)
                    
                    # Could also create recruiters based on particle patterns
                    if pattern.role == "core":
                        recruiter = Recruiter(
                            theta_recruiter=particle_module.master_phase + pattern.phase_offset,
                            ancestry_recruiter=particle_module.ancestry_signature
                        )
                        self.recruiters[pos] = recruiter
        
        self.identities.append(identity)
        return identity
    
    def _is_valid_position(self, position: Tuple[int, int, int]) -> bool:
        """Check if position is within lattice bounds"""
        return (0 <= position[0] < self.lattice_shape[0] and
                0 <= position[1] < self.lattice_shape[1] and
                0 <= position[2] < self.lattice_shape[2])
    
    def create_detection_event(self, event_type: DetectionEventType, position: Tuple[int, int, int], 
                             triggering_particle: Identity = None) -> DetectionEvent:
        """Create a detection event that can trigger conflict resolution"""
        affected_identities = self.get_coexisting_identities(position)
        
        event = DetectionEvent(
            event_type=event_type,
            position=position,
            tick=self.tick,
            triggering_particle=triggering_particle,
            affected_identities=affected_identities
        )
        
        self.detection_events.append(event)
        return event
    
    def resolve_detection_conflict(self, detection_event: DetectionEvent) -> Dict[str, Any]:
        """Resolve conflict triggered by detection event using symbolic methods"""
        if len(detection_event.affected_identities) < 2:
            return {"resolution": "no_conflict", "details": "less than 2 identities"}
        
        resolution_method = self.config.default_conflict_resolution
        
        # Apply resolution based on method
        resolution_result = {
            "method": resolution_method.value,
            "tick": self.tick,
            "position": detection_event.position,
            "affected_count": len(detection_event.affected_identities),
            "mutations": []
        }
        
        if resolution_method == ConflictResolutionMethod.SYMBOLIC_MUTATION:
            # Apply ancestry mutation to resolve conflict
            for i, identity in enumerate(detection_event.affected_identities[1:], 1):  # Skip first identity
                mutation_tag = f"_{i}"
                identity.apply_symbolic_mutation("ancestry_append", mutation_tag=mutation_tag)
                resolution_result["mutations"].append({
                    "identity_id": identity.unique_id,
                    "mutation": mutation_tag,
                    "new_ancestry": identity.ancestry
                })
        
        elif resolution_method == ConflictResolutionMethod.IDENTITY_RENAME:
            # Rename identity tags to differentiate
            for i, identity in enumerate(detection_event.affected_identities[1:], 1):
                mutation_tag = f"*{i}"
                identity.apply_symbolic_mutation("identity_suffix", mutation_tag=mutation_tag)
                resolution_result["mutations"].append({
                    "identity_id": identity.unique_id,
                    "new_tag": identity.module_tag
                })
        
        elif resolution_method == ConflictResolutionMethod.PHASE_SEPARATION:
            # Apply small phase offsets to separate identities
            for i, identity in enumerate(detection_event.affected_identities[1:], 1):
                phase_offset = i * 0.02  # Small phase separation
                identity.theta = (identity.theta + phase_offset) % 1.0
                resolution_result["mutations"].append({
                    "identity_id": identity.unique_id,
                    "phase_offset": phase_offset,
                    "new_phase": identity.theta
                })
        
        # Record conflict resolution
        for identity in detection_event.affected_identities:
            identity.conflict_resolution_applied = resolution_method
        
        detection_event.resolution_method = resolution_method
        detection_event.mutation_results = resolution_result
        
        self.conflict_resolutions.append(resolution_result)
        return resolution_result
    
    def move_particle(self, identity: Identity):
        """Move a particle according to its velocity vector"""
        if identity.particle_module and identity.particle_module.velocity:
            current_pos = identity.position
            velocity = identity.particle_module.velocity
            
            # Calculate new position (simplified - integer steps for now)
            new_pos = (
                int(current_pos[0] + velocity[0]),
                int(current_pos[1] + velocity[1]), 
                int(current_pos[2] + velocity[2])
            )
            
            if self._is_valid_position(new_pos):
                # Remove particle from old position
                self._remove_particle_from_position(identity, current_pos)
                
                # Add particle to new position
                identity.position = new_pos
                self._apply_particle_to_position(identity, new_pos)
                
                # Check for detection events at new position
                if (identity.particle_module.triggers_detection and 
                    self.config.enable_detection_events):
                    coexisting = self.get_coexisting_identities(new_pos)
                    if len(coexisting) > 1:  # Multiple identities at position
                        self.create_detection_event(
                            DetectionEventType.PARTICLE_COLLISION, 
                            new_pos, 
                            identity
                        )
    
    def _remove_particle_from_position(self, identity: Identity, position: Tuple[int, int, int]):
        """Remove particle effects from a position"""
        # Remove from coexistence registry
        if position in self.coexistence_registry:
            if identity.unique_id in self.coexistence_registry[position]:
                self.coexistence_registry[position].remove(identity.unique_id)
            if not self.coexistence_registry[position]:
                del self.coexistence_registry[position]
        
        if identity.particle_module:
            affected_positions = identity.particle_module.get_affected_positions(position)
            for pos in affected_positions:
                if self._is_valid_position(pos):
                    # Reset echo field (simplified)
                    self.echo_fields[pos].rho_local *= 0.5
                    # Remove recruiters created by this particle
                    if pos in self.recruiters:
                        del self.recruiters[pos]
    
    def _apply_particle_to_position(self, identity: Identity, position: Tuple[int, int, int]):
        """Apply particle effects to a new position"""
        # Register coexistence
        self.register_coexistence(position, identity)
        
        if identity.particle_module:
            affected_positions = identity.particle_module.get_affected_positions(position)
            for i, pattern in enumerate(identity.particle_module.node_patterns):
                if i < len(affected_positions):
                    pos = affected_positions[i]
                    if self._is_valid_position(pos):
                        # Apply timing influence
                        timing_influence = pattern.timing_rate * 50.0
                        self.echo_fields[pos].rho_local += timing_influence
                        
                        # Create recruiters for core patterns
                        if pattern.role == "core":
                            recruiter = Recruiter(
                                theta_recruiter=identity.particle_module.master_phase + pattern.phase_offset,
                                ancestry_recruiter=identity.particle_module.ancestry_signature
                            )
                            self.recruiters[pos] = recruiter
    
    def add_recruiter(self, position: Tuple[int, int, int], recruiter: Recruiter):
        """Add a recruiter at a specific position"""
        self.recruiters[position] = recruiter
    
    def set_echo_field(self, position: Tuple[int, int, int], rho_local: float):
        """Set echo field strength at a position"""
        if position in self.echo_fields:
            self.echo_fields[position].rho_local = rho_local
    
    # =========================================================================
    # ETM RULE IMPLEMENTATIONS - Enhanced for Detection-Triggered Resolution
    # =========================================================================
    
    def calculate_phase_match(self, theta_identity: float, theta_recruiter: float) -> bool:
        """Implement phase matching component of R1"""
        phase_diff = abs(theta_identity - theta_recruiter) % 1.0
        phase_diff = min(phase_diff, 1.0 - phase_diff)
        return phase_diff <= self.config.phase_tolerance
    
    def calculate_ancestry_match(self, ancestry_identity: str, ancestry_recruiter: str) -> bool:
        """Implement ancestry matching with smoothing (R10, R11)"""
        if not self.config.ancestry_required:
            return True
        
        if self.config.smoothing_enabled and self.tick >= self.config.smoothing_tick:
            mismatch = self.count_mismatch_tags(ancestry_identity, ancestry_recruiter)
            effective_mismatch = self.apply_symbolic_smoothing(mismatch)
            return effective_mismatch <= self.config.smoothing_threshold
        else:
            return ancestry_identity == ancestry_recruiter
    
    def count_mismatch_tags(self, ancestry1: Union[str, List], ancestry2: Union[str, List]) -> int:
        """Count mismatched characters between ancestry strings or lists"""
        # Convert to lists if strings
        if isinstance(ancestry1, str):
            ancestry1 = list(ancestry1)
        if isinstance(ancestry2, str):
            ancestry2 = list(ancestry2)
        
        if len(ancestry1) != len(ancestry2):
            return abs(len(ancestry1) - len(ancestry2)) + sum(
                1 for a, b in zip(ancestry1, ancestry2) if a != b
            )
        return sum(1 for a, b in zip(ancestry1, ancestry2) if a != b)
    
    def apply_symbolic_smoothing(self, mismatch: int) -> int:
        """Apply symbolic smoothing logic (R11)"""
        # Based on trial results: reduce significant mismatches
        if mismatch == 4:
            return 2
        elif mismatch == 3:
            return 2
        return mismatch
    
    def calculate_echo_match(self, position: Tuple[int, int, int]) -> Tuple[bool, float]:
        """Implement echo matching with hybrid calculation (A4, A4b)"""
        rho_local = self.echo_fields[position].rho_local
        
        # Calculate neighbor echo for hybrid mode
        neighbors = self.get_neighbors(*position)
        if neighbors:
            rho_neigh = sum(self.echo_fields[pos].rho_local for pos in neighbors) / len(neighbors)
        else:
            rho_neigh = 0.0
        
        # Hybrid echo calculation (A4b)
        rho_hybrid = (self.config.echo_hybrid_local_weight * rho_local + 
                     self.config.echo_hybrid_neighbor_weight * rho_neigh)
        
        echo_match = rho_hybrid >= self.config.rho_min
        return echo_match, rho_hybrid
    
    def evaluate_return_eligibility(self, identity: Identity) -> Tuple[bool, Dict]:
        """Implement R1: Return Eligibility Evaluation"""
        if not identity.position or identity.position not in self.recruiters:
            return False, {"reason": "no_recruiter"}
        
        recruiter = self.recruiters[identity.position]
        
        # Phase match
        phase_match = self.calculate_phase_match(identity.theta, recruiter.theta_recruiter)
        
        # Ancestry match
        ancestry_match = self.calculate_ancestry_match(identity.ancestry, recruiter.ancestry_recruiter)
        
        # Echo match
        echo_match, rho_hybrid = self.calculate_echo_match(identity.position)
        
        # Combined eligibility (A5)
        return_allowed = phase_match and ancestry_match and echo_match
        
        return return_allowed, {
            "phase_match": phase_match,
            "ancestry_match": ancestry_match,
            "echo_match": echo_match,
            "rho_hybrid": rho_hybrid,
            "phase_diff": abs(identity.theta - recruiter.theta_recruiter) % 1.0
        }
    
    def check_conflict_passive(self, identity1: Identity, identity2: Identity) -> bool:
        """Check for conflict in passive state (without detection)"""
        if not self.config.enable_passive_coexistence:
            # Use original conflict logic
            if (identity1.position == identity2.position and 
                identity1.ancestry == identity2.ancestry):
                
                phase_diff = abs(identity1.theta - identity2.theta) % 1.0
                phase_diff = min(phase_diff, 1.0 - phase_diff)
                return phase_diff < self.config.epsilon
        
        # With passive coexistence enabled (based on trial results), no conflict
        return False
    
    def check_detection_required(self, position: Tuple[int, int, int]) -> bool:
        """Check if detection event is required at position"""
        coexisting = self.get_coexisting_identities(position)
        
        # Detection required if multiple identical identities without resolution
        if len(coexisting) > 1:
            # Check for identical identities that haven't been resolved
            unresolved_identical = []
            for identity in coexisting:
                if identity.conflict_resolution_applied is None:
                    # Check if identical to any other unresolved identity
                    for other in unresolved_identical:
                        if (identity.ancestry == other.ancestry and 
                            abs(identity.theta - other.theta) < self.config.epsilon):
                            return True
                    unresolved_identical.append(identity)
        
        return False
    
    def execute_identity_reformation(self, identity: Identity):
        """Implement identity reformation (R3) with coexistence support"""
        if identity.position in self.recruiters:
            recruiter = self.recruiters[identity.position]
            
            # Lock to recruiter rhythm
            identity.theta = recruiter.theta_recruiter
            identity.ancestry = recruiter.ancestry_recruiter
            
            # Check for coexistence
            coexisting = self.get_coexisting_identities(identity.position)
            if len(coexisting) > 1:
                identity.return_status = ReturnStatus.COEXISTING
            else:
                identity.return_status = ReturnStatus.COMPLETE
            
            # Register with recruiter
            recruiter.add_returned_identity(identity)
            
            # Boost echo field
            self.echo_fields[identity.position].add_reinforcement(1.0)
    
    # =========================================================================
    # SIMULATION LOOP - Enhanced with Detection Events
    # =========================================================================
    
    def advance_tick(self):
        """Execute one complete ETM simulation tick"""
        self.tick += 1
        
        # 1. Tick Initialization (Procedural Logic Section 1)
        self.advance_phases()
        self.apply_echo_decay()
        
        # 1.5. Move particles with velocity vectors
        for identity in self.identities:
            if identity.particle_module and identity.particle_module.velocity:
                self.move_particle(identity)
        
        # 2. Identity Evaluation Loop (Procedural Logic Section 2)
        return_results = []
        for identity in self.identities:
            return_allowed, evaluation = self.evaluate_return_eligibility(identity)
            return_results.append({
                "identity": identity,
                "return_allowed": return_allowed,
                "evaluation": evaluation
            })
        
        # 3. Reformation and Reinforcement (Procedural Logic Section 3)
        for result in return_results:
            if result["return_allowed"]:
                # Check for passive conflicts (minimal with new coexistence model)
                conflicts = self.check_all_passive_conflicts(result["identity"])
                if not conflicts:
                    self.execute_identity_reformation(result["identity"])
                else:
                    result["identity"].return_status = ReturnStatus.FAILED
        
        # 4. Detection Event Processing
        if self.config.enable_detection_events:
            self.process_detection_events()
        
        # 5. Process particle interactions (absorption, emission, transitions)
        self.process_particle_interactions()
        
        # 6. Echo Propagation and Inheritance (Procedural Logic Section 5)
        self.apply_echo_inheritance()
        
        # 7. State Advancement and Cleanup (Procedural Logic Section 6)
        self.record_tick_results(return_results)
    
    def process_detection_events(self):
        """Process all detection events for this tick"""
        positions_to_check = list(self.coexistence_registry.keys())
        
        for position in positions_to_check:
            if self.check_detection_required(position):
                # Create and resolve detection event
                detection_event = self.create_detection_event(
                    DetectionEventType.MEASUREMENT_PROBE,
                    position
                )
                
                if self.config.detection_triggers_mutation:
                    resolution_result = self.resolve_detection_conflict(detection_event)
    
    def process_particle_interactions(self):
        """Process particle absorption, emission, and energy level transitions"""
        interactions = []
        
        # Check for particle overlaps and potential interactions
        for i, identity1 in enumerate(self.identities):
            for j, identity2 in enumerate(self.identities[i+1:], i+1):
                if (identity1.particle_module and identity2.particle_module and
                    identity1.position == identity2.position):
                    
                    # Check if particles can interact
                    interaction = self.check_particle_interaction(identity1, identity2)
                    if interaction:
                        interactions.append(interaction)
                        
                        # Create detection event for interaction
                        if self.config.enable_detection_events:
                            self.create_detection_event(
                                DetectionEventType.PHOTON_INTERACTION,
                                identity1.position,
                                identity1
                            )
        
        # Execute interactions
        for interaction in interactions:
            self.execute_interaction(interaction)
    
    def check_particle_interaction(self, identity1: Identity, identity2: Identity) -> Optional[Dict]:
        """Check if two particles can interact (absorption, etc.)"""
        p1 = identity1.particle_module
        p2 = identity2.particle_module
        
        # Example: Photon absorption by electron
        if (p1.particle_type == ParticleType.PHOTON and 
            p2.particle_type == ParticleType.ELECTRON and
            p2.context == ParticleContext.ATOMIC_ORBITAL):
            
            return {
                "type": "absorption",
                "absorber": identity2,
                "absorbed": identity1,
                "result_energy_level": "excited_1"  # This would be calculated
            }
        
        return None
    
    def execute_interaction(self, interaction: Dict):
        """Execute a particle interaction"""
        if interaction["type"] == "absorption":
            absorber = interaction["absorber"]
            absorbed = interaction["absorbed"]
            
            # Remove absorbed particle
            self.identities.remove(absorbed)
            self._remove_particle_from_position(absorbed, absorbed.position)
            
            # Transition absorber to higher energy level
            if absorber.particle_module:
                absorber.particle_module.energy_level = interaction["result_energy_level"]
                absorber.particle_module.context = ParticleContext.TRANSITION_STATE
                # Update timing patterns for new energy level
                self.update_particle_energy_state(absorber)
    
    def update_particle_energy_state(self, identity: Identity):
        """Update particle patterns for new energy state"""
        if identity.particle_module:
            # This would update the node patterns based on new energy level
            # For now, just update the timing rate
            identity.particle_module.master_delta_theta *= 1.2  # Higher energy = faster rhythm
    
    def advance_phases(self):
        """Advance all identity and recruiter phases (R2)"""
        for identity in self.identities:
            identity.update_phase()
        
        for recruiter in self.recruiters.values():
            recruiter.update_phase()
    
    def apply_echo_decay(self):
        """Apply echo decay to all fields (R4)"""
        for echo_field in self.echo_fields.values():
            echo_field.apply_decay(self.config.decay_factor)
    
    def apply_echo_inheritance(self):
        """Apply echo inheritance from neighbors (R5)"""
        if self.config.inheritance_alpha <= 0:
            return
        
        new_echo_values = {}
        
        for position, echo_field in self.echo_fields.items():
            neighbors = self.get_neighbors(*position)
            if neighbors:
                neighbor_echo = sum(self.echo_fields[pos].rho_local for pos in neighbors) / len(neighbors)
                new_echo = echo_field.rho_local + self.config.inheritance_alpha * neighbor_echo
                new_echo_values[position] = new_echo
        
        # Apply new values
        for position, new_value in new_echo_values.items():
            self.echo_fields[position].rho_local = new_value
    
    def check_all_passive_conflicts(self, identity: Identity) -> List[Identity]:
        """Check for passive conflicts with all other identities"""
        conflicts = []
        for other in self.identities:
            if other != identity and self.check_conflict_passive(identity, other):
                conflicts.append(other)
        return conflicts
    
    def record_tick_results(self, return_results: List[Dict]):
        """Record results for this tick"""
        tick_data = {
            "tick": self.tick,
            "identities": [],
            "return_results": [],
            "detection_events": [],
            "coexistence_registry": dict(self.coexistence_registry),
            "conflict_resolutions": self.conflict_resolutions[-10:]  # Last 10 resolutions
        }
        
        for identity in self.identities:
            tick_data["identities"].append({
                "unique_id": identity.unique_id,
                "module_tag": identity.module_tag,
                "ancestry": identity.ancestry,
                "original_ancestry": identity.original_ancestry,
                "theta": identity.theta,
                "position": identity.position,
                "return_status": identity.return_status.value,
                "tick_memory": identity.tick_memory,
                "is_mutated": identity.is_mutated,
                "coexisting_with": identity.coexisting_with,
                "conflict_resolution": identity.conflict_resolution_applied.value if identity.conflict_resolution_applied else None
            })
        
        for result in return_results:
            tick_data["return_results"].append({
                "identity_id": result["identity"].unique_id,
                "return_allowed": result["return_allowed"],
                "evaluation": result["evaluation"]
            })
        
        # Record detection events for this tick
        current_tick_events = [event for event in self.detection_events if event.tick == self.tick]
        for event in current_tick_events:
            tick_data["detection_events"].append({
                "type": event.event_type.value,
                "position": event.position,
                "affected_count": len(event.affected_identities),
                "resolution_method": event.resolution_method.value if event.resolution_method else None,
                "triggering_particle": event.triggering_particle.unique_id if event.triggering_particle else None
            })
        
        self.results_history.append(tick_data)
    
    def run_simulation(self) -> Dict:
        """Run complete ETM simulation"""
        print(f"Starting Enhanced ETM simulation: {self.config.trial_name}")
        print(f"Configuration: {self.config.connectivity}-connectivity, {self.config.max_ticks} ticks")
        print(f"Detection events: {'Enabled' if self.config.enable_detection_events else 'Disabled'}")
        print(f"Passive coexistence: {'Enabled' if self.config.enable_passive_coexistence else 'Disabled'}")
        
        while self.tick < self.config.max_ticks:
            self.advance_tick()
            
            if self.tick % 10 == 0:
                print(f"Tick {self.tick}/{self.config.max_ticks} - Identities: {len(self.identities)}, Detection events: {len([e for e in self.detection_events if e.tick == self.tick])}")
        
        results = {
            "config": self.config.__dict__,
            "final_tick": self.tick,
            "total_identities": len(self.identities),
            "total_recruiters": len(self.recruiters),
            "total_detection_events": len(self.detection_events),
            "total_conflict_resolutions": len(self.conflict_resolutions),
            "coexistence_positions": len(self.coexistence_registry),
            "history": self.results_history
        }
        
        if self.config.output_json:
            self.save_results_json(results)
        
        return results
    
    def save_results_json(self, results: Dict):
        """Save results to JSON file with proper tuple key handling"""
        filename = f"etm_enhanced_trial_{self.config.trial_name}_{self.tick}ticks.json"
        
        # Make results JSON serializable
        serializable_results = copy.deepcopy(results)
        
        # Convert enum values to strings
        if 'config' in serializable_results:
            config = serializable_results['config']
            if 'default_conflict_resolution' in config:
                if hasattr(config['default_conflict_resolution'], 'value'):
                    config['default_conflict_resolution'] = config['default_conflict_resolution'].value
        
        # Convert tuple keys to strings in history
        if 'history' in serializable_results:
            for tick_data in serializable_results['history']:
                if 'coexistence_registry' in tick_data:
                    registry = tick_data['coexistence_registry']
                    if registry:
                        fixed_registry = {}
                        for key, value in registry.items():
                            str_key = ",".join(map(str, key)) if isinstance(key, tuple) else str(key)
                            fixed_registry[str_key] = value
                        tick_data['coexistence_registry'] = fixed_registry
        
        with open(filename, 'w') as f:
            json.dump(serializable_results, f, indent=2, default=str)
        
        print(f"Enhanced results saved to: {filename}")

# =============================================================================
# PARTICLE MODULE LIBRARY - Enhanced with Detection Signatures
# =============================================================================

class ParticleLibrary:
    """Library of pre-defined particle modules with detection capabilities"""
    
    @staticmethod
    def photon_free_space(wavelength_factor: float = 1.0, direction: Tuple[float, float, float] = (1, 0, 0)) -> ParticleModule:
        """Photon propagating through free space - Enhanced with detection triggering"""
        # Photon as a traveling wave pattern
        node_patterns = [
            NodePattern((0, 0, 0), timing_rate=1.0, role="core"),  # Leading edge
            NodePattern((-1, 0, 0), timing_rate=0.8, phase_offset=0.25),  # Wave trail
            NodePattern((-2, 0, 0), timing_rate=0.6, phase_offset=0.5),
            NodePattern((1, 0, 0), timing_rate=0.9, phase_offset=-0.1, role="propagation_front")
        ]
        
        # Normalize direction vector for velocity
        magnitude = (direction[0]**2 + direction[1]**2 + direction[2]**2)**0.5
        if magnitude > 0:
            velocity = (direction[0]/magnitude, direction[1]/magnitude, direction[2]/magnitude)
        else:
            velocity = (1, 0, 0)
        
        return ParticleModule(
            particle_type=ParticleType.PHOTON,
            context=ParticleContext.FREE_SPACE,
            node_patterns=node_patterns,
            velocity=velocity,
            master_delta_theta=0.2 * wavelength_factor,
            ancestry_signature="PHOTON_FREE",
            absorption_targets=[ParticleType.ELECTRON],
            detection_signature="PHOTON_PING",
            triggers_detection=True  # Photons trigger detection events
        )
    
    @staticmethod
    def electron_ground_state() -> ParticleModule:
        """Electron in atomic ground state (1s orbital) - Enhanced for coexistence"""
        # Spherically symmetric pattern for ground state
        node_patterns = [
            NodePattern((0, 0, 0), timing_rate=1.0, role="core"),
            # First shell
            NodePattern((1, 0, 0), timing_rate=0.7),
            NodePattern((-1, 0, 0), timing_rate=0.7),
            NodePattern((0, 1, 0), timing_rate=0.7),
            NodePattern((0, -1, 0), timing_rate=0.7),
            NodePattern((0, 0, 1), timing_rate=0.7),
            NodePattern((0, 0, -1), timing_rate=0.7),
            # Second shell (weaker)
            NodePattern((2, 0, 0), timing_rate=0.3),
            NodePattern((-2, 0, 0), timing_rate=0.3),
            NodePattern((0, 2, 0), timing_rate=0.3),
            NodePattern((0, -2, 0), timing_rate=0.3),
        ]
        
        return ParticleModule(
            particle_type=ParticleType.ELECTRON,
            context=ParticleContext.ATOMIC_ORBITAL,
            energy_level="1s",
            node_patterns=node_patterns,
            master_delta_theta=0.05,
            ancestry_signature="ELECTRON_1S",
            transition_rules={"photon_absorption": "2p"},
            detection_signature="ELECTRON_1S",
            triggers_detection=False  # Electrons don't typically trigger detection
        )
    
    @staticmethod
    def electron_excited_state() -> ParticleModule:
        """Electron in excited state (2p orbital) - Enhanced for transitions"""
        # More complex pattern for excited state
        node_patterns = [
            NodePattern((0, 0, 0), timing_rate=0.8, role="core"),
            # Elongated p-orbital pattern
            NodePattern((3, 0, 0), timing_rate=0.9),
            NodePattern((-3, 0, 0), timing_rate=0.9),
            NodePattern((2, 1, 0), timing_rate=0.6),
            NodePattern((2, -1, 0), timing_rate=0.6),
            NodePattern((-2, 1, 0), timing_rate=0.6),
            NodePattern((-2, -1, 0), timing_rate=0.6),
            # Outer shell
            NodePattern((4, 0, 0), timing_rate=0.4),
            NodePattern((-4, 0, 0), timing_rate=0.4),
        ]
        
        return ParticleModule(
            particle_type=ParticleType.ELECTRON,
            context=ParticleContext.ATOMIC_ORBITAL,
            energy_level="2p",
            node_patterns=node_patterns,
            master_delta_theta=0.08,  # Higher energy = faster rhythm
            ancestry_signature="ELECTRON_2P",
            transition_rules={"spontaneous_emission": "1s"},
            detection_signature="ELECTRON_2P",
            triggers_detection=False
        )
    
    @staticmethod
    def electron_free_space(velocity: Tuple[float, float, float] = (0, 0, 0)) -> ParticleModule:
        """Free electron with momentum - Enhanced for interactions"""
        # Compact pattern for free electron
        node_patterns = [
            NodePattern((0, 0, 0), timing_rate=1.0, role="core"),
            NodePattern((1, 0, 0), timing_rate=0.5),
            NodePattern((-1, 0, 0), timing_rate=0.5),
            NodePattern((0, 1, 0), timing_rate=0.5),
            NodePattern((0, -1, 0), timing_rate=0.5),
        ]
        
        return ParticleModule(
            particle_type=ParticleType.ELECTRON,
            context=ParticleContext.FREE_SPACE,
            energy_level="free",
            node_patterns=node_patterns,
            velocity=velocity,
            master_delta_theta=0.1,
            ancestry_signature="ELECTRON_FREE",
            detection_signature="ELECTRON_FREE",
            triggers_detection=True  # Free electrons can trigger detection
        )

# =============================================================================
# ENHANCED TRIAL BUILDER - With Detection-Triggered Scenarios
# =============================================================================

class ETMTrialBuilder:
    """Builder for creating specific ETM trial configurations with detection events"""
    
    @staticmethod
    def trial_070_enhanced_dual_identity_coexistence() -> Tuple[ETMEngine, ETMConfig]:
        """Enhanced recreation of Trial 070 with detection-triggered resolution"""
        config = ETMConfig(
            trial_name="070_enhanced_dual_identity_coexistence",
            max_ticks=5,
            connectivity=8,  # Using optimal connectivity
            lattice_size=(30, 30, 30),
            smoothing_enabled=True,
            smoothing_tick=3,
            enable_passive_coexistence=True,  # Key setting from trial results
            enable_detection_events=True,
            detection_triggers_mutation=True,
            default_conflict_resolution=ConflictResolutionMethod.SYMBOLIC_MUTATION
        )
        
        engine = ETMEngine(config)
        
        # Set up recruiter field
        center = engine.center
        recruiter = Recruiter(theta_recruiter=0.25, ancestry_recruiter="ABC")
        engine.add_recruiter(center, recruiter)
        
        # Initialize echo field around center
        for dx in range(-6, 7):
            for dy in range(-6, 7):
                for dz in range(-6, 7):
                    x, y, z = center[0]+dx, center[1]+dy, center[2]+dz
                    if (0 <= x < 30 and 0 <= y < 30 and 0 <= z < 30):
                        engine.set_echo_field((x, y, z), 30.0)
        
        # Boost core region
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                for dz in range(-2, 3):
                    x, y, z = center[0]+dx, center[1]+dy, center[2]+dz
                    if (0 <= x < 30 and 0 <= y < 30 and 0 <= z < 30):
                        engine.set_echo_field((x, y, z), 60.0)
        
        # Create two identities that will approach and coexist
        identity_a = Identity(
            module_tag="ROTOR_A",
            ancestry="ABCXY",
            theta=0.24,
            delta_theta=0.1,
            position=(14, 15, 15),
            original_ancestry="ABCXY"
        )
        
        identity_b = Identity(
            module_tag="ROTOR_B", 
            ancestry="ABCZW",
            theta=0.25,
            delta_theta=0.1,
            position=(16, 15, 15),
            original_ancestry="ABCZW"
        )
        
        engine.identities.extend([identity_a, identity_b])
        
        return engine, config
    
    @staticmethod
    def detection_triggered_mutation_trial() -> Tuple[ETMEngine, ETMConfig]:
        """Trial specifically testing detection-triggered symbolic mutation"""
        config = ETMConfig(
            trial_name="detection_triggered_mutation",
            max_ticks=10,
            connectivity=8,
            lattice_size=(40, 40, 40),
            enable_passive_coexistence=True,
            enable_detection_events=True,
            detection_triggers_mutation=True,
            default_conflict_resolution=ConflictResolutionMethod.SYMBOLIC_MUTATION
        )
        
        engine = ETMEngine(config)
        
        # Create two identical electrons at same orbital
        center = engine.center
        
        electron1 = ParticleLibrary.electron_ground_state()
        electron1.ancestry_signature = "ABC"
        identity1 = engine.add_particle_module(electron1, center)
        
        electron2 = ParticleLibrary.electron_ground_state()
        electron2.ancestry_signature = "ABC"  # Identical ancestry
        identity2 = engine.add_particle_module(electron2, center)
        
        # Add photon that will trigger detection at tick 5
        photon = ParticleLibrary.photon_free_space(direction=(1, 0, 0))
        photon_position = (center[0] - 5, center[1], center[2])
        engine.add_particle_module(photon, photon_position)
        
        return engine, config
    
    @staticmethod
    def coexistence_stability_trial() -> Tuple[ETMEngine, ETMConfig]:
        """Trial testing long-term stability of coexisting identities"""
        config = ETMConfig(
            trial_name="coexistence_stability",
            max_ticks=50,
            connectivity=8,
            lattice_size=(60, 60, 60),
            enable_passive_coexistence=True,
            enable_detection_events=False,  # No detection events
            ancestry_required=True,
            smoothing_enabled=True
        )
        
        engine = ETMEngine(config)
        center = engine.center
        
        # Create multiple electrons in same orbital
        for i in range(3):
            electron = ParticleLibrary.electron_ground_state()
            electron.ancestry_signature = "ELECTRON_TEST"
            electron.master_phase = 0.25 + i * 0.001  # Slight phase differences
            engine.add_particle_module(electron, center)
        
        return engine, config
    
    @staticmethod
    def photon_electron_detection_trial() -> Tuple[ETMEngine, ETMConfig]:
        """Trial: Photon detection triggering electron state resolution"""
        config = ETMConfig(
            trial_name="photon_electron_detection",
            max_ticks=30,
            connectivity=8,
            lattice_size=(40, 40, 40),
            enable_passive_coexistence=True,
            enable_detection_events=True,
            detection_triggers_mutation=True,
            default_conflict_resolution=ConflictResolutionMethod.SYMBOLIC_MUTATION
        )
        
        engine = ETMEngine(config)
        
        # Place two electrons in overlapping orbitals
        center = engine.center
        
        electron1 = ParticleLibrary.electron_ground_state()
        electron1.ancestry_signature = "ELECTRON_GROUND"
        identity1 = engine.add_particle_module(electron1, center)
        
        electron2 = ParticleLibrary.electron_ground_state()
        electron2.ancestry_signature = "ELECTRON_GROUND"  # Same ancestry
        identity2 = engine.add_particle_module(electron2, center)
        
        # Create detection photon approaching
        photon = ParticleLibrary.photon_free_space(
            wavelength_factor=1.2,
            direction=(1, 0, 0)
        )
        photon_position = (center[0] - 10, center[1], center[2])
        engine.add_particle_module(photon, photon_position)
        
        return engine, config
    
    @staticmethod
    def connectivity_enhanced_echo_trial() -> Tuple[ETMEngine, ETMConfig]:
        """Trial testing 8-connectivity enhancement of echo field propagation"""
        config = ETMConfig(
            trial_name="connectivity_enhanced_echo",
            max_ticks=50,
            connectivity=8,  # Optimal connectivity
            lattice_size=(21, 21, 21),
            enable_passive_coexistence=True,
            enable_detection_events=True
        )
        
        engine = ETMEngine(config)
        
        # Initialize central echo field (similar to connectivity test)
        center = engine.center
        engine.set_echo_field(center, 100.0)
        
        # Add multiple identities for testing
        for i in range(4):
            identity = Identity(
                module_tag=f"TEST_{i}",
                ancestry="ABCD",
                theta=0.25 + i * 0.05,
                delta_theta=0.1,
                position=center
            )
            engine.identities.append(identity)
            engine.register_coexistence(center, identity)
        
        return engine, config

# =============================================================================
# MAIN EXECUTION - Enhanced with Detection Scenarios
# =============================================================================

def main():
    """Main execution function - Enhanced trials with detection-triggered resolution"""
    
    print("Enhanced ETM Framework - Detection-Triggered Conflict Resolution")
    print("="*70)
    
    # Example 1: Enhanced dual identity coexistence (based on Trial 070)
    print("Running Enhanced Trial 070: Dual Identity Coexistence")
    engine1, config1 = ETMTrialBuilder.trial_070_enhanced_dual_identity_coexistence()
    results1 = engine1.run_simulation()
    
    print(f"\nCompleted: {config1.trial_name}")
    print(f"Final identities: {results1['total_identities']}")
    print(f"Detection events: {results1['total_detection_events']}")
    print(f"Conflict resolutions: {results1['total_conflict_resolutions']}")
    print(f"Coexistence positions: {results1['coexistence_positions']}")
    
    # Example 2: Detection-triggered mutation
    print("\n" + "="*70)
    print("Running Detection-Triggered Mutation Trial")
    engine2, config2 = ETMTrialBuilder.detection_triggered_mutation_trial()
    results2 = engine2.run_simulation()
    
    print(f"\nCompleted: {config2.trial_name}")
    print(f"Final identities: {results2['total_identities']}")
    print(f"Detection events: {results2['total_detection_events']}")
    print(f"Conflict resolutions: {results2['total_conflict_resolutions']}")
    
    # Example 3: Coexistence stability
    print("\n" + "="*70)
    print("Running Coexistence Stability Trial")
    engine3, config3 = ETMTrialBuilder.coexistence_stability_trial()
    results3 = engine3.run_simulation()
    
    print(f"\nCompleted: {config3.trial_name}")
    print(f"Final identities: {results3['total_identities']}")
    print(f"Coexistence positions: {results3['coexistence_positions']}")
    
    print("\n" + "="*70)
    print("Enhanced ETM Framework trials completed successfully!")
    print(f"Key Enhancements:")
    print(f"- Detection-triggered conflict resolution: ✓")
    print(f"- Passive coexistence support: ✓")
    print(f"- 8-connectivity optimization: ✓")
    print(f"- Symbolic mutation system: ✓")
    print(f"- Trial 070-074 findings integrated: ✓")
    
    return results1, results2, results3

if __name__ == "__main__":
    main()