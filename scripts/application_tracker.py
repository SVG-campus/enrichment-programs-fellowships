#!/usr/bin/env python3
"""
Enrichment Programs & Fellowships Application Tracker

Utility to track application deadlines, status, and milestone deliverables.
"""

PROGRAMS = [
    {
        "name": "Thiel Fellowship",
        "category": "Entrepreneurial",
        "deadline": "Rolling",
        "value": "$100,000 Non-dilutive Grant",
        "status": "Targeting Submission (Q4 2026)"
    },
    {
        "name": "Y Combinator (YC Winter)",
        "category": "Accelerator",
        "deadline": "October 2026",
        "value": "$500,000 Investment",
        "status": "Preparing Metrics"
    },
    {
        "name": "Syracuse Renée Crown Honors",
        "category": "Undergraduate Honors",
        "deadline": "Upon Re-enrollment",
        "value": "Priority Registration & $5,000 Research Grant",
        "status": "Planned for Spring 2027"
    },
    {
        "name": "Stanford Knight-Hennessy Scholars",
        "category": "Graduate Fellowship",
        "deadline": "October 2027",
        "value": "Full Tuition + Stipend (Stanford MS/PhD)",
        "status": "Targeted for MS/PhD Entry"
    },
    {
        "name": "Hertz Foundation Fellowship",
        "category": "Doctoral Fellowship",
        "deadline": "October 2027",
        "value": "$250,000 Direct PhD Funding",
        "status": "Targeted for PhD Entry"
    }
]

def print_tracker():
    print("=== ELITE FELLOWSHIPS & ENRICHMENT PROGRAM TRACKER ===")
    for p in PROGRAMS:
        print(f"\n[+] {p['name']} ({p['category']})")
        print(f"    Value: {p['value']}")
        print(f"    Deadline: {p['deadline']}")
        print(f"    Status: {p['status']}")

if __name__ == "__main__":
    print_tracker()
