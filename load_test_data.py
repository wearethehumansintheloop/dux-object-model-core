#!/usr/bin/env python3
"""
Load Test Data into Research Platform
Loads synthetic DUX objects from the Object Model into the Research Platform's Neo4j database.
"""

import json
import os
import sys
from pathlib import Path
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env")

# Neo4j configuration
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# Path to test data
TEST_DATA_PATH = Path("test_data/synthetic/v9_5_validation_sample.json")

def load_test_data():
    """Load test data from JSON file into Neo4j."""
    
    # Check if test data file exists
    if not TEST_DATA_PATH.exists():
        print(f"❌ Test data file not found: {TEST_DATA_PATH}")
        return False
    
    # Load test data
    try:
        with open(TEST_DATA_PATH, 'r') as f:
            test_objects = json.load(f)
        print(f"✅ Loaded {len(test_objects)} test objects from {TEST_DATA_PATH}")
    except Exception as e:
        print(f"❌ Error loading test data: {e}")
        return False
    
    # Connect to Neo4j
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        print(f"✅ Connected to Neo4j at {NEO4J_URI}")
    except Exception as e:
        print(f"❌ Error connecting to Neo4j: {e}")
        return False
    
    # Load objects into Neo4j
    with driver.session() as session:
        for obj in test_objects:
            try:
                obj_type = obj.get("object_type")
                obj_id = obj.get("id")
                
                if not obj_type or not obj_id:
                    print(f"⚠️  Skipping object without type or id: {obj}")
                    continue
                
                # Create node based on object type
                if obj_type == "Problem":
                    session.run("""
                        MERGE (p:Problem {id: $id})
                        SET p += $props
                    """, id=obj_id, props={k: v for k, v in obj.items() if k not in ["id", "object_type"]})
                    print(f"✅ Loaded Problem: {obj_id}")
                
                elif obj_type == "Behavior":
                    session.run("""
                        MERGE (b:Behavior {id: $id})
                        SET b += $props
                    """, id=obj_id, props={k: v for k, v in obj.items() if k not in ["id", "object_type"]})
                    print(f"✅ Loaded Behavior: {obj_id}")
                
                elif obj_type == "Result":
                    session.run("""
                        MERGE (r:Result {id: $id})
                        SET r += $props
                    """, id=obj_id, props={k: v for k, v in obj.items() if k not in ["id", "object_type"]})
                    print(f"✅ Loaded Result: {obj_id}")
                
                elif obj_type == "Flow":
                    session.run("""
                        MERGE (f:Flow {id: $id})
                        SET f += $props
                    """, id=obj_id, props={k: v for k, v in obj.items() if k not in ["id", "object_type"]})
                    print(f"✅ Loaded Flow: {obj_id}")
                
                elif obj_type == "UserOutcome":
                    session.run("""
                        MERGE (u:UserOutcome {id: $id})
                        SET u += $props
                    """, id=obj_id, props={k: v for k, v in obj.items() if k not in ["id", "object_type"]})
                    print(f"✅ Loaded UserOutcome: {obj_id}")
                
                else:
                    print(f"⚠️  Unknown object type: {obj_type}")
                
            except Exception as e:
                print(f"❌ Error loading object {obj.get('id', 'unknown')}: {e}")
    
    # Create Insight relationships
    print("\n🔗 Creating Insight relationships...")
    try:
        # Create sample insight chains by linking Problems, Behaviors, and Results
        session.run("""
            MATCH (p:Problem), (b:Behavior), (r:Result)
            WHERE p.id CONTAINS 'problem' AND b.id CONTAINS 'behavior' AND r.id CONTAINS 'result'
            WITH p, b, r LIMIT 3
            MERGE (i:Insight {id: 'insight_' + p.id + '_' + b.id + '_' + r.id})
            SET i.name = 'Sample Insight Chain',
                i.story = 'This is a sample insight chain connecting ' + p.id + ' to ' + b.id + ' to ' + r.id,
                i.evidence_maturity = '03_early_signal',
                i.updated_at = datetime()
            MERGE (i)-[:HAS_PROBLEM]->(p)
            MERGE (i)-[:HAS_BEHAVIOR]->(b)
            MERGE (i)-[:HAS_RESULT]->(r)
        """)
        print("✅ Created sample insight chains")
    except Exception as e:
        print(f"❌ Error creating insight relationships: {e}")
    
    driver.close()
    print("\n🎉 Test data loading complete!")
    return True

def verify_data_loaded():
    """Verify that data was loaded successfully."""
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        with driver.session() as session:
            # Count nodes by type
            result = session.run("""
                MATCH (n)
                RETURN labels(n)[0] as type, count(n) as count
                ORDER BY type
            """)
            
            print("\n📊 Data verification:")
            for record in result:
                print(f"  {record['type']}: {record['count']} nodes")
            
            # Check for insight chains
            insight_count = session.run("MATCH (i:Insight) RETURN count(i) as count").single()['count']
            print(f"  Insight chains: {insight_count}")
            
        driver.close()
        return True
    except Exception as e:
        print(f"❌ Error verifying data: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Loading test data into Research Platform...")
    
    if load_test_data():
        verify_data_loaded()
        print("\n✅ Test data is ready! You can now:")
        print("  1. Start the Research Platform: docker-compose up api")
        print("  2. Visit the White-Label UI: http://localhost:3000/showcase-live")
        print("  3. Test the connection and view live data")
    else:
        print("\n❌ Failed to load test data")
        sys.exit(1) 