#!/usr/bin/env python3
"""
Enrichment Programs & Fellowships Application Tracker (Adult & 29yo Founder Optimized)

Utility to track application deadlines, status, and milestone deliverables.
"""

PROGRAMS = [
    {
        "name": "Emergent Ventures (Mercatus Center)",
        "category": "Fast Non-Dilutive Grant",
        "deadline": "Rolling (2-3 Wk Decision)",
        "value": "$10,000 - $100,000",
        "status": "IMMEDIATE (Apply Now)"
    },
    {
        "name": "NSF SBIR Phase I",
        "category": "Federal Deep Tech Grant",
        "deadline": "Rolling Pitch",
        "value": "$300,000 Non-Dilutive",
        "status": "Preparing Project Pitch"
    },
    {
        "name": "Y Combinator (YC Winter)",
        "category": "Venture Accelerator",
        "deadline": "October 2026",
        "value": "$500,000 Investment",
        "status": "Preparing Metrics (+12%/day)"
    },
    {
        "name": "776 Fellowship (Alexis Ohanian)",
        "category": "Founder Grant",
        "deadline": "Rolling",
        "value": "$100,000 Non-Dilutive",
        "status": "Targeting Submission"
    },
    {
        "name": "Osher Reentry Scholarship",
        "category": "Adult Undergrad (25+)",
        "deadline": "Upon Re-enrollment",
        "value": "$5,000 - $10,000",
        "status": "Planned for Syracuse Re-entry"
    },
    {
        "name": "Stanford Knight-Hennessy Scholars",
        "category": "Graduate Fellowship",
        "deadline": "October 2027",
        "value": "Full Tuition + Stipend (Stanford MS/PhD)",
        "status": "Targeted for MS/PhD Entry"
    }
]

def print_tracker():
    print("=== ELITE FELLOWSHIPS & GRANTS TRACKER (29yo FOUNDER OPTIMIZED) ===")
    for p in PROGRAMS:
        print(f"\n[+] {p['name']} ({p['category']})")
        print(f"    Value: {p['value']}")
        print(f"    Deadline: {p['deadline']}")
        print(f"    Status: {p['status']}")

if __name__ == "__main__":
    print_tracker()
