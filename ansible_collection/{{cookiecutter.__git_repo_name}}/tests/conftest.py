from pathlib import Path
import sys
import pytest

base_path = Path(__file__).parent.parent
sys.path.append(base_path.resolve().as_posix())
