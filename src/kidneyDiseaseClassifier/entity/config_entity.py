from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataINgestionConfig:
    root_dir: Path
    source_URL: str
    local_source_file: Path
    unzip_dir: Path