import os
import sys

def build_topical_map(central_entity, source_context, clusters):
    print(f"=== TOPICAL MAP GENERATOR (KORAY'S FRAMEWORK) ===")
    print(f"Central Entity (CE): {central_entity}")
    print(f"Source Context (SC): {source_context}")
    print(f"Central Search Intent (CSI): {central_entity} for {source_context}\n")
    
    for cluster_name, subtopics in clusters.items():
        print(f"📁 Macro-Context Cluster: {cluster_name}")
        for st in subtopics:
            print(f"   └── 📄 Micro-Context Node: {st}")
            print(f"       ├── EAV: [{central_entity}] -> [{cluster_name}] -> [{st}]")
            print(f"       └── Anchor Strategy: Exact entity-attribute target\n")

if __name__ == "__main__":
    example_clusters = {
        "Diagnostics & Codes": ["OBD-II P0300 Misfire Diagnosis", "Brake Pad Wear Sensor Resistance Limits"],
        "Preventative Maintenance": ["Oil Viscosity Operating Thresholds", "Transmission Fluid Flushing Schedules"]
    }
    build_topical_map("Automotive Engineering", "Practical Mechanical Repair", example_clusters)
