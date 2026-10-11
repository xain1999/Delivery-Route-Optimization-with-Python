"""Download the Chicago Regional road network used in Chapter 4.

    python tools/fetch_chicago_network.py        # about 4 MB, a few seconds

The network was built by the Chicago Area Transportation Study (CATS) for
regional traffic planning and is distributed, with an equilibrium traffic
assignment, by the Transportation Networks for Research project:
https://github.com/bstabler/TransportationNetworks (folder chicago-regional).
The project states that the data sets are donated and meant for research;
read its terms before using them in a product.  For your own city, build
the street network from OpenStreetMap instead (tools/fetch_chicago_roads.py).

Writes data/cats/ChicagoRegional_{net,node,flow}.tntp.
"""
from __future__ import annotations

import sys
import urllib.request
from pathlib import Path

BASE = ("https://raw.githubusercontent.com/bstabler/TransportationNetworks/"
        "master/chicago-regional/")
FILES = ["ChicagoRegional_net.tntp", "ChicagoRegional_node.tntp",
         "ChicagoRegional_flow.tntp"]
OUT = Path(__file__).resolve().parent.parent / "data" / "cats"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        path = OUT / name
        if path.exists() and path.stat().st_size > 0:
            print(f"{name}: already here")
            continue
        print(f"{name}: downloading...", flush=True)
        with urllib.request.urlopen(BASE + name, timeout=120) as resp:
            path.write_bytes(resp.read())
        print(f"{name}: {path.stat().st_size / 1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
