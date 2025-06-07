"""
ETM Framework - Euclidean Timing Mechanics
A modular physics simulation framework
"""

__version__ = "2.3 Nucleon Enhanced"

# Simple imports that work
def get_config():
    from .config import ETMConfig
    return ETMConfig

def get_engine():
    from .core import ETMEngine
    return ETMEngine

def get_identity():
    from .core import Identity
    return Identity

# For direct access if needed
try:
    from .config import ETMConfig, ConfigurationFactory
    from .core import ETMEngine, Identity, Recruiter, EchoField
except ImportError:
    # If there are import issues, they can still be imported individually
    pass