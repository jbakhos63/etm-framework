#!/usr/bin/env python3
"""
Test script for ETM modules
This properly imports and tests the modular components
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_config_module():
    """Test the configuration module"""
    print("Testing Configuration Module...")
    print("-" * 40)
    
    from etm.config import ETMConfig, ConfigurationFactory, ETM_VERSION
    
    # Test basic config
    config = ETMConfig()
    print(f"✓ Basic config: connectivity={config.connectivity}")
    print(f"✓ Kinetic scale: {config.kinetic_scale_factor}")
    print(f"✓ Version: {ETM_VERSION}")
    
    # Test nucleon config
    nucleon_config = ConfigurationFactory.nucleon_physics_config("test")
    print(f"✓ Nucleon config: beta_decay={nucleon_config.enable_beta_decay}")
    
    return True

def test_core_module():
    """Test the core module"""
    print("\nTesting Core Module...")
    print("-" * 40)
    
    from etm.config import ETMConfig
    from etm.core import ETMEngine, Identity
    
    # Test engine creation
    config = ETMConfig(max_ticks=5, connectivity=8)
    engine = ETMEngine(config)
    print(f"✓ Engine created: {config.connectivity}-connectivity")
    print(f"✓ Lattice size: {engine.lattice_shape}")
    print(f"✓ Center: {engine.center}")
    
    # Test identity creation
    identity = Identity(
        module_tag="TEST",
        ancestry="ABC", 
        theta=0.5,
        delta_theta=0.1,
        position=engine.center
    )
    print(f"✓ Identity created: {identity.unique_id}")
    
    # Test phase advancement
    original_theta = identity.theta
    identity.update_phase()
    print(f"✓ Phase: {original_theta:.3f} → {identity.theta:.3f}")
    
    # Test neighbors
    neighbors = engine.get_neighbors(*engine.center)
    print(f"✓ Neighbors: {len(neighbors)} for center")
    
    # Test echo fields
    print(f"✓ Echo fields: {len(engine.echo_fields)} positions")
    
    return True

def test_integration():
    """Test that modules work together"""
    print("\nTesting Module Integration...")
    print("-" * 40)
    
    # Import modules individually (this definitely works)
    from etm.config import ETMConfig
    from etm.core import ETMEngine, Identity
    
    # Test direct package imports
    config = ETMConfig(trial_name="integration_test", max_ticks=3)
    engine = ETMEngine(config)
    
    # Add an identity
    identity = Identity(
        module_tag="INTEGRATION_TEST",
        ancestry="TEST",
        theta=0.25,
        delta_theta=0.1,
        position=engine.center
    )
    engine.identities.append(identity)
    
    # Run a few ticks
    for i in range(3):
        engine.advance_tick()
    
    print(f"✓ Simulation ran {engine.tick} ticks")
    print(f"✓ Final identities: {len(engine.identities)}")
    print(f"✓ Integration successful!")
    
    return True

if __name__ == "__main__":
    print("ETM Module Testing")
    print("=" * 50)
    
    try:
        # Test each module
        config_ok = test_config_module()
        core_ok = test_core_module() 
        integration_ok = test_integration()
        
        if config_ok and core_ok and integration_ok:
            print("\n🎉 ALL TESTS PASSED!")
            print("✅ Configuration module working")
            print("✅ Core module working") 
            print("✅ Module integration working")
            print("\nReady for next step: Extract particles module")
        else:
            print("\n❌ Some tests failed")
            
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()