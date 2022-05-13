from collections import Counter
from dataclasses import dataclass
from typing import List

@dataclass
class Contents:
    files: List[str]
    folders: List[str]
    
    def _repr_pretty_(self, p, cycle):
        if cycle:
            p.text('...')
        else:
            p.text(f'Files: ({len(self.files)}) ')
            p.text(f'{dict(Counter([f.suffix for f in self.files]))} ' if len(self.files) > 0  else '')
            p.breakable('| ')
            p.text(f'Folders: ({len(self.folders)})')

def list_contents(path):
    items = list(path.iterdir())

    fi = [item for item in items if item.is_file()]
    fo = [item for item in items if item.is_dir()]
    
    return Contents(files=fi, folders=fo)