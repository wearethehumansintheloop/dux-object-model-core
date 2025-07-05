#!/usr/bin/env python3
"""
DUX Object Model Master Governance Script

This script runs all object validation scripts and provides a comprehensive
summary of the DUX Object Model governance status across all object types.

Naming Convention: validate_[object_type]_objects.py
Sorting: Alphabetical by object type for consistent execution order
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

# List of all validation scripts in execution order
# Sorted alphabetically by object type for consistent governance flow
VALIDATION_SCRIPTS = [
    "validate_behavior_objects.py",      # 1. Behavior (observable actions)
    "validate_flow_objects.py",          # 2. Flow (user journeys)
    "validate_insight_objects.py",       # 3. Insight (synthesized findings)
    "validate_problem_objects.py",       # 4. Problem (JTBD statements)
    "validate_provenance_objects.py",    # 5. Provenance (evidence sources)
    "validate_result_objects.py",        # 6. Result (desired outcomes)
    "validate_useroutcome_objects.py"    # 7. UserOutcome (user goals)
]

def run_validation_script(script_name: str) -> bool:
    """Run a single validation script and return success status."""
    print(f"\n{'='*80}")
    print(f"🔍 Running: {script_name}")
    print(f"{'='*80}")
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(result.stdout)
            return True
        else:
            print(f"❌ Error running {script_name}:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout running {script_name}")
        return False
    except Exception as e:
        print(f"❌ Exception running {script_name}: {e}")
        return False

def main():
    """Run all governance validations."""
    print("🎯 DUX Object Model Master Governance System")
    print("=" * 80)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"Total validation scripts: {len(VALIDATION_SCRIPTS)}")
    print(f"Execution order: Alphabetical by object type")
    
    # Check if all scripts exist
    missing_scripts = []
    for script in VALIDATION_SCRIPTS:
        if not Path(script).exists():
            missing_scripts.append(script)
    
    if missing_scripts:
        print(f"\n❌ Missing validation scripts: {missing_scripts}")
        return
    
    # Run all validations in order
    successful_runs = 0
    failed_runs = 0
    execution_results = []
    
    for i, script in enumerate(VALIDATION_SCRIPTS, 1):
        print(f"\n📋 Step {i}/{len(VALIDATION_SCRIPTS)}: {script}")
        
        if run_validation_script(script):
            successful_runs += 1
            execution_results.append(f"✅ {script}")
        else:
            failed_runs += 1
            execution_results.append(f"❌ {script}")
    
    # Final summary
    print(f"\n{'='*80}")
    print("🎯 GOVERNANCE SUMMARY")
    print(f"{'='*80}")
    print(f"✅ Successful validations: {successful_runs}")
    print(f"❌ Failed validations: {failed_runs}")
    print(f"📊 Total scripts: {len(VALIDATION_SCRIPTS)}")
    
    print(f"\n📋 Execution Results:")
    for result in execution_results:
        print(f"  {result}")
    
    if successful_runs == len(VALIDATION_SCRIPTS):
        print(f"\n🎉 All governance validations completed successfully!")
        print(f"🎯 DUX Object Model is fully validated and ready for use!")
    else:
        print(f"\n⚠️  {failed_runs} validation(s) failed - check error logs")
        print(f"🔧 Fix issues and re-run governance for complete validation")
    
    print(f"\n📁 Check watch_folders/hitl_failed/ for quarantined files")
    print(f"📁 Check individual error logs for detailed validation issues")
    print(f"🔄 Re-run: python run_all_governance.py")

if __name__ == "__main__":
    main() 