# ETM Framework - AI Developer Guide
## Complete Instructions for Working with the Modular ETM Framework

### 🎯 **Purpose**
This guide enables any AI to understand, use, and extend the modular ETM (Euclidean Timing Mechanics) framework without prior context.

---

## 📁 **Framework Structure**

```
etm-framework/
├── etm/                    # Main package
│   ├── __init__.py        # Package initialization
│   ├── config.py          # Configuration classes and validated parameters
│   ├── core.py            # Core ETM physics engine
│   └── particles.py       # Particle timing patterns and physics
├── test_modules.py        # Complete module testing suite
├── check_photon_physics.py # Photon physics assessment
└── current_monolith/      # Original framework (backup)
    └── etm_framework.py
```

---

## 🔧 **Module APIs and Usage Patterns**

### **1. Configuration Module (`etm/config.py`)**

**Purpose:** All configuration classes, enums, and validated parameters

**Key Classes:**
```python
from etm.config import ETMConfig, ConfigurationFactory, ParticleType

# Basic configuration
config = ETMConfig()  # Uses all validated defaults

# Validated configurations
config = ConfigurationFactory.validated_foundation_config("trial_name")
config = ConfigurationFactory.nucleon_physics_config("nucleon_trial")

# Key validated parameters (NEVER CHANGE):
config.connectivity = 8                    # Validated optimal
config.kinetic_scale_factor = 1000.0      # Calibrated
config.potential_coefficient = 0.003723   # Calibrated  
config.coulomb_constant = 13.6            # Maintained
```

**Critical Parameters (Validated - Do Not Modify):**
- `connectivity = 8` (35.6% improvement validated)
- `kinetic_scale_factor = 1000.0` (calibrated for <1% energy accuracy)
- `enable_passive_coexistence = True` (Model B validation)
- `default_conflict_resolution = SYMBOLIC_MUTATION` (Model B)

### **2. Core Module (`etm/core.py`)**

**Purpose:** Core ETM physics engine and fundamental classes

**Key Classes:**
```python
from etm.core import ETMEngine, Identity, Recruiter, EchoField

# Create engine
config = ETMConfig(trial_name="test", max_ticks=100)
engine = ETMEngine(config)

# Create identity
identity = Identity(
    module_tag="TEST_PARTICLE",
    ancestry="TEST",
    theta=0.5,              # Phase
    delta_theta=0.1,        # Phase rate
    position=engine.center  # Spatial position
)

# Run simulation
engine.identities.append(identity)
results = engine.run_simulation()
```

**Core Physics Methods:**
- `engine.advance_tick()` - Execute one simulation step
- `identity.update_phase()` - Advance particle phase
- `engine.get_neighbors(x, y, z)` - Get 8-connected neighbors
- `identity.calculate_particle_energy()` - Calibrated energy calculation

### **3. Particles Module (`etm/particles.py`)**

**Purpose:** All particle timing patterns and composite particle architecture

**Key Classes:**
```python
from etm.particles import ParticleFactory, ParticleStabilityTester

# Create validated particles
proton = ParticleFactory.create_enhanced_proton()    # 90.9% AGN survival
electron = ParticleFactory.create_electron()         # Orbital-compatible
neutrino = ParticleFactory.create_neutrino()        # Interaction mediator
neutron = ParticleFactory.create_neutron()          # 3-constituent composite
photon = ParticleFactory.create_photon(13.6)        # Specified energy

# Test particle stability
tester = ParticleStabilityTester()
result = tester.test_particle_stability(proton, "agn_ejection")
```

**Particle Achievements:**
- **Enhanced Proton:** >90% AGN survival for cosmological element recycling
- **Nucleon Internal Structure:** Neutron as composite [proton + electron + neutrino]  
- **Beta Decay:** n → p + e⁻ + ν̄ₑ mechanism implemented
- **Photon Physics:** Complete electromagnetic timing patterns with orbital interactions

---

## 📝 **Standard Script Patterns**

### **Pattern 1: Basic Testing Script**
```python
#!/usr/bin/env python3
"""
Template for ETM module testing
"""

def test_basic_functionality():
    """Test core ETM functionality"""
    from etm.config import ETMConfig
    from etm.core import ETMEngine, Identity
    from etm.particles import ParticleFactory
    
    # 1. Create configuration
    config = ETMConfig(trial_name="test", max_ticks=10)
    
    # 2. Create engine  
    engine = ETMEngine(config)
    
    # 3. Create particles
    proton = ParticleFactory.create_enhanced_proton()
    electron = ParticleFactory.create_electron()
    
    # 4. Test key metrics
    agn_survival = proton.calculate_agn_survival_probability()
    print(f"Enhanced proton AGN survival: {agn_survival:.3f}")
    
    # 5. Validate against targets
    assert config.connectivity == 8, "8-connectivity must be preserved"
    assert agn_survival >= 0.90, "AGN survival must be ≥90%"
    
    return True

if __name__ == "__main__":
    test_basic_functionality()
    print("✅ All tests passed")
```

### **Pattern 2: Simulation Script**
```python
#!/usr/bin/env python3
"""
Template for ETM simulations
"""

def run_etm_simulation(config_name="default", ticks=100):
    """Run ETM simulation with specified parameters"""
    from etm.config import ConfigurationFactory
    from etm.core import ETMEngine, Identity
    
    # 1. Get validated configuration
    config = ConfigurationFactory.validated_foundation_config(config_name)
    config.max_ticks = ticks
    
    # 2. Create engine
    engine = ETMEngine(config)
    
    # 3. Set up scenario (example: hydrogen atom)
    center = engine.center
    
    # Add recruiter
    from etm.core import Recruiter
    recruiter = Recruiter(theta_recruiter=0.25, ancestry_recruiter="H1s")
    engine.recruiters[center] = recruiter
    
    # Add electron identity  
    electron_identity = Identity(
        module_tag="ELECTRON_1s",
        ancestry="H1s", 
        theta=0.24,
        delta_theta=0.1,
        position=center
    )
    engine.identities.append(electron_identity)
    
    # 4. Run simulation
    results = engine.run_simulation()
    
    # 5. Return key metrics
    return {
        "total_identities": results["total_identities"],
        "final_tick": results["final_tick"],
        "success": results["final_tick"] == config.max_ticks
    }

if __name__ == "__main__":
    results = run_etm_simulation("hydrogen_test", 50)
    print(f"Simulation: {results}")
```

### **Pattern 3: Comprehensive Assessment**
```python
#!/usr/bin/env python3
"""
Template for comprehensive ETM assessment
"""

def assess_etm_framework():
    """Comprehensive assessment of ETM framework capabilities"""
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "framework_version": "2.3 Nucleon Enhanced",
        "modules_tested": [],
        "achievements_validated": {},
        "performance_metrics": {}
    }
    
    # Test 1: Configuration
    try:
        from etm.config import ETMConfig, ETM_VERSION
        config = ETMConfig()
        results["modules_tested"].append("config")
        results["achievements_validated"]["connectivity_optimization"] = config.connectivity == 8
        results["achievements_validated"]["calibrated_energy"] = config.enable_calibrated_energy
    except Exception as e:
        results["config_error"] = str(e)
    
    # Test 2: Core physics
    try:
        from etm.core import ETMEngine
        engine = ETMEngine(config)
        results["modules_tested"].append("core")
        results["performance_metrics"]["lattice_size"] = engine.lattice_shape
        results["performance_metrics"]["echo_fields"] = len(engine.echo_fields)
    except Exception as e:
        results["core_error"] = str(e)
    
    # Test 3: Particle physics
    try:
        from etm.particles import ParticleFactory, ParticleStabilityTester
        
        # Test enhanced proton
        proton = ParticleFactory.create_enhanced_proton()
        agn_survival = proton.calculate_agn_survival_probability()
        
        # Test nucleon structure
        neutron = ParticleFactory.create_neutron()
        
        # Test photon physics
        photon = ParticleFactory.create_photon(13.6)
        
        results["modules_tested"].append("particles")
        results["achievements_validated"]["enhanced_proton_agn"] = agn_survival >= 0.90
        results["achievements_validated"]["nucleon_structure"] = len(neutron.constituent_patterns) >= 3
        results["achievements_validated"]["photon_physics"] = photon.energy_content > 0
        
        results["performance_metrics"]["agn_survival_rate"] = agn_survival
        results["performance_metrics"]["neutron_constituents"] = len(neutron.constituent_patterns)
        
    except Exception as e:
        results["particles_error"] = str(e)
    
    return results

if __name__ == "__main__":
    import json
    from datetime import datetime
    
    assessment = assess_etm_framework()
    
    # Print summary
    print("ETM Framework Assessment")
    print("=" * 50)
    print(f"Modules tested: {assessment['modules_tested']}")
    print(f"Achievements validated: {sum(assessment['achievements_validated'].values())}/{len(assessment['achievements_validated'])}")
    
    # Save detailed results
    with open("etm_assessment.json", "w") as f:
        json.dump(assessment, f, indent=2)
    
    print("Detailed results saved to etm_assessment.json")
```

---

## 📊 **Result Interpretation Guidelines**

### **Success Indicators:**
- **AGN Survival ≥ 90%:** Enhanced protons working correctly
- **3+ Neutron Constituents:** Nucleon internal structure functional  
- **Connectivity = 8:** Core ETM optimization preserved
- **Energy Calculations Active:** Calibrated system working
- **All Tests Pass:** Framework integrity maintained

### **Critical Metrics:**
```python
# Expected values for healthy framework
EXPECTED_VALUES = {
    "connectivity": 8,                    # Must be exactly 8
    "agn_survival_minimum": 0.90,        # 90%+ for enhanced protons
    "neutron_constituents": 3,           # Proton + electron + neutrino
    "energy_calibration": True,          # Must be enabled
    "kinetic_scale_factor": 1000.0,      # Calibrated value
    "potential_coefficient": 0.003723,   # Calibrated value
}
```

### **Common Issues and Solutions:**
```python
# Issue: Import errors
# Solution: Ensure all modules in etm/ directory with __init__.py

# Issue: AGN survival < 90%
# Solution: Check enhanced proton pattern integrity

# Issue: Neutron constituents != 3  
# Solution: Verify composite particle initialization

# Issue: Energy calculation errors
# Solution: Verify calibrated parameters preserved
```

---

## 🔄 **JSON Output Patterns**

### **Compact Summary Format:**
```python
def generate_compact_summary(results):
    """Generate compact JSON summary for Claude upload"""
    
    summary = {
        "etm_framework_status": {
            "version": "2.3 Nucleon Enhanced",
            "timestamp": datetime.now().isoformat(),
            "modules_operational": [],
            "validated_achievements": {},
            "performance_metrics": {},
            "next_actions": []
        }
    }
    
    # Add results...
    return summary

# Save with size limit
def save_compact_json(data, max_kb=100):
    """Save JSON with size optimization"""
    filename = f"etm_compact_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(filename, 'w') as f:
        json.dump(data, f, separators=(',', ':'), indent=1)
    
    size_kb = os.path.getsize(filename) / 1024
    
    if size_kb > max_kb:
        print(f"⚠ Warning: {filename} is {size_kb:.1f}KB (target: <{max_kb}KB)")
    else:
        print(f"✓ Saved: {filename} ({size_kb:.1f}KB)")
    
    return filename
```

---

## 🎯 **Framework Validation Checklist**

### **Before Any Development:**
1. ✅ **Verify connectivity = 8** (core optimization)
2. ✅ **Confirm calibrated energy enabled** (accuracy achievement)  
3. ✅ **Check AGN survival ≥ 90%** (enhanced proton validation)
4. ✅ **Validate 3 neutron constituents** (nucleon structure)
5. ✅ **Test photon-electron interactions** (restored physics)

### **After Any Changes:**
1. ✅ **Run module tests** (`python test_modules.py`)
2. ✅ **Check photon physics** (`python check_photon_physics.py`)
3. ✅ **Verify no regressions** in validated parameters
4. ✅ **Test new functionality** thoroughly
5. ✅ **Generate assessment report** before commit

---

## 🚀 **Quick Start for New AI**

```python
# 1. Test framework health
from etm.config import ETMConfig
from etm.core import ETMEngine  
from etm.particles import ParticleFactory

# 2. Verify core achievements
config = ETMConfig()
assert config.connectivity == 8, "Core optimization missing"

proton = ParticleFactory.create_enhanced_proton()
assert proton.calculate_agn_survival_probability() >= 0.90, "Enhanced proton degraded"

# 3. Ready for development!
print("✅ ETM Framework validated and ready")
```

This guide enables any AI to immediately understand and work with the ETM framework while preserving all validated achievements.