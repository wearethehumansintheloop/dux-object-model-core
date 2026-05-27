"""
Interactive Vector Explorer for TF-IDF Validation
Shows exactly which word sits at each coordinate position
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import json
from typing import Dict, List, Tuple


class InteractiveVectorExplorer:
    """
    Explore the relationship between words and vector coordinates
    """
    
    def __init__(self, vectorizer: TfidfVectorizer):
        self.vectorizer = vectorizer
        self.vocabulary = vectorizer.vocabulary_
        self.feature_names = vectorizer.get_feature_names_out()
        self.inverse_vocabulary = {idx: word for word, idx in self.vocabulary.items()}
        
    def get_coordinate_mapping(self) -> Dict[int, str]:
        """
        Get the complete mapping of coordinate positions to words
        """
        mapping = {}
        for coordinate in range(len(self.feature_names)):
            mapping[coordinate] = self.feature_names[coordinate]
        return mapping
    
    def word_to_coordinate(self, word: str) -> int:
        """
        Find which coordinate a specific word occupies
        """
        word_lower = word.lower()
        if word_lower in self.vocabulary:
            return self.vocabulary[word_lower]
        else:
            return None
    
    def coordinate_to_word(self, coordinate: int) -> str:
        """
        Find which word occupies a specific coordinate
        """
        if 0 <= coordinate < len(self.feature_names):
            return self.feature_names[coordinate]
        return None
    
    def analyze_text_vector(self, text: str) -> Dict:
        """
        Analyze a text and show which coordinates are activated
        """
        # Transform text to vector
        vector = self.vectorizer.transform([text]).toarray()[0]
        
        # Find active coordinates (non-zero values)
        active_coordinates = []
        for coord in range(len(vector)):
            if vector[coord] > 0:
                active_coordinates.append({
                    'coordinate': coord,
                    'word': self.feature_names[coord],
                    'weight': float(vector[coord])
                })
        
        # Sort by weight
        active_coordinates.sort(key=lambda x: x['weight'], reverse=True)
        
        return {
            'text': text,
            'total_coordinates': len(vector),
            'active_coordinates': len(active_coordinates),
            'coordinate_details': active_coordinates,
            'vector': vector.tolist()
        }
    
    def create_visual_map(self, text: str) -> str:
        """
        Create a visual ASCII representation of the vector
        """
        analysis = self.analyze_text_vector(text)
        vector = analysis['vector']
        
        # Create visual representation
        visual = []
        visual.append("="*80)
        visual.append(f"VECTOR MAP FOR: {text[:60]}...")
        visual.append("="*80)
        visual.append("")
        
        # Show coordinate grid (10x10 for 100 dimensions)
        visual.append("COORDINATE GRID (0-99):")
        visual.append("-" * 60)
        
        # Determine actual vector size
        vector_size = len(vector)
        grid_rows = min(10, (vector_size + 9) // 10)
        
        for row in range(grid_rows):
            row_str = ""
            for col in range(10):
                coord = row * 10 + col
                if coord >= vector_size:
                    row_str += "  "
                    continue
                value = vector[coord]
                if value > 0:
                    # Active coordinate - show intensity
                    if value > 0.5:
                        row_str += "█ "
                    elif value > 0.3:
                        row_str += "▓ "
                    elif value > 0.1:
                        row_str += "▒ "
                    else:
                        row_str += "░ "
                else:
                    row_str += "· "
            
            # Add row labels
            start_coord = row * 10
            end_coord = start_coord + 9
            visual.append(f"[{start_coord:2d}-{end_coord:2d}] {row_str}")
        
        visual.append("")
        visual.append("Legend: █=high ▓=medium ▒=low ░=very low ·=zero")
        visual.append("")
        
        # List active coordinates with words
        visual.append("ACTIVE COORDINATES:")
        visual.append("-" * 60)
        
        for detail in analysis['coordinate_details'][:20]:  # Top 20
            coord = detail['coordinate']
            word = detail['word']
            weight = detail['weight']
            visual.append(f"  Coord [{coord:3d}] = '{word:20s}' (weight: {weight:.4f})")
        
        return "\n".join(visual)
    
    def export_coordinate_dictionary(self) -> Dict:
        """
        Export the complete coordinate-to-word dictionary
        """
        dictionary = {
            'total_dimensions': len(self.feature_names),
            'coordinate_mapping': {}
        }
        
        for coord in range(len(self.feature_names)):
            dictionary['coordinate_mapping'][coord] = {
                'word': self.feature_names[coord],
                'coordinate': coord
            }
        
        return dictionary


def create_interactive_demo():
    """
    Create an interactive demonstration
    """
    # Sample corpus for building vocabulary
    corpus = [
        "Machine learning algorithms include neural networks and decision trees",
        "Deep learning uses multiple layers of neurons for complex patterns",
        "Supervised learning requires labeled training data for classification",
        "Unsupervised learning discovers hidden patterns in unlabeled data",
        "Reinforcement learning optimizes actions through reward signals"
    ]
    
    # Create vectorizer
    vectorizer = TfidfVectorizer(
        max_features=100,
        ngram_range=(1, 2),
        stop_words='english',
        lowercase=True
    )
    
    # Fit vectorizer
    vectorizer.fit(corpus)
    
    # Create explorer
    explorer = InteractiveVectorExplorer(vectorizer)
    
    return explorer, vectorizer


def demonstrate_word_coordinate_lookup(explorer: InteractiveVectorExplorer):
    """
    Demonstrate looking up words and coordinates
    """
    print("\n" + "="*80)
    print("WORD ↔ COORDINATE LOOKUP DEMONSTRATION")
    print("="*80)
    
    # Test words to look up
    test_words = ["learning", "neural", "data", "patterns", "algorithms"]
    
    print("\n1. WORD → COORDINATE LOOKUP:")
    print("-" * 40)
    for word in test_words:
        coord = explorer.word_to_coordinate(word)
        if coord is not None:
            print(f"  '{word}' → Coordinate {coord}")
        else:
            print(f"  '{word}' → Not in vocabulary")
    
    print("\n2. COORDINATE → WORD LOOKUP:")
    print("-" * 40)
    test_coords = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    for coord in test_coords:
        word = explorer.coordinate_to_word(coord)
        if word:
            print(f"  Coordinate {coord:2d} → '{word}'")
    
    print("\n3. COMPLETE COORDINATE DICTIONARY (First 20):")
    print("-" * 40)
    mapping = explorer.get_coordinate_mapping()
    for coord in range(20):
        print(f"  [{coord:2d}] = '{mapping[coord]}'")


def create_interactive_html_explorer(explorer: InteractiveVectorExplorer):
    """
    Create an enhanced HTML explorer with clickable coordinates
    """
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive TF-IDF Vector Explorer</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        h1 {
            color: white;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        .card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .card h2 {
            color: #333;
            margin-bottom: 15px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }
        
        .input-section {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        input[type="text"] {
            flex: 1;
            padding: 12px;
            border: 2px solid #e5e7eb;
            border-radius: 8px;
            font-size: 1em;
        }
        
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        button:hover {
            background: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        .vector-grid {
            display: grid;
            grid-template-columns: repeat(10, 1fr);
            gap: 4px;
            margin: 20px 0;
        }
        
        .coord-cell {
            aspect-ratio: 1;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
        }
        
        .coord-cell:hover {
            transform: scale(1.2);
            z-index: 10;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        
        .coord-cell.inactive {
            background: #f3f4f6;
            color: #9ca3af;
        }
        
        .coord-cell.active {
            color: white;
        }
        
        .coord-cell.active.high {
            background: #dc2626;
        }
        
        .coord-cell.active.medium {
            background: #f59e0b;
        }
        
        .coord-cell.active.low {
            background: #3b82f6;
        }
        
        .coord-cell.active.verylow {
            background: #8b5cf6;
        }
        
        .tooltip {
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            background: #1f2937;
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 0.85em;
            white-space: nowrap;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s;
            margin-bottom: 8px;
            z-index: 100;
        }
        
        .coord-cell:hover .tooltip {
            opacity: 1;
        }
        
        .tooltip::after {
            content: '';
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            border: 6px solid transparent;
            border-top-color: #1f2937;
        }
        
        .word-lookup {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 20px 0;
        }
        
        .lookup-box {
            padding: 15px;
            background: #f9fafb;
            border-radius: 8px;
            border: 2px solid #e5e7eb;
        }
        
        .lookup-result {
            margin-top: 10px;
            padding: 10px;
            background: white;
            border-radius: 6px;
            min-height: 40px;
            display: flex;
            align-items: center;
            font-weight: 500;
        }
        
        .active-words {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 15px;
        }
        
        .word-tag {
            background: #667eea;
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.9em;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .word-tag .coord {
            background: rgba(255,255,255,0.3);
            padding: 2px 6px;
            border-radius: 10px;
            font-size: 0.85em;
        }
        
        .dictionary-scroll {
            max-height: 400px;
            overflow-y: auto;
            padding: 10px;
            background: #f9fafb;
            border-radius: 8px;
        }
        
        .dict-entry {
            display: flex;
            justify-content: space-between;
            padding: 8px;
            border-bottom: 1px solid #e5e7eb;
        }
        
        .dict-entry:hover {
            background: white;
        }
        
        .coord-num {
            color: #667eea;
            font-weight: 600;
            font-family: monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Interactive TF-IDF Vector Explorer</h1>
        
        <div class="card">
            <h2>Analyze Text</h2>
            <div class="input-section">
                <input type="text" id="textInput" placeholder="Enter text to analyze (e.g., 'neural networks use deep learning algorithms')">
                <button onclick="analyzeText()">Analyze Vector</button>
            </div>
            
            <div id="analysisResult"></div>
        </div>
        
        <div class="card">
            <h2>100-Dimensional Vector Grid</h2>
            <p style="color: #6b7280; margin-bottom: 15px;">
                Click any cell to see which word occupies that coordinate position
            </p>
            <div id="vectorGrid" class="vector-grid"></div>
            <div id="activeWords" class="active-words"></div>
        </div>
        
        <div class="card">
            <h2>Word ↔ Coordinate Lookup</h2>
            <div class="word-lookup">
                <div class="lookup-box">
                    <h3 style="margin-bottom: 10px;">Find Word's Coordinate</h3>
                    <input type="text" id="wordInput" placeholder="Enter word (e.g., 'learning')">
                    <button onclick="lookupWord()" style="margin-top: 10px;">Find Coordinate</button>
                    <div id="wordResult" class="lookup-result"></div>
                </div>
                
                <div class="lookup-box">
                    <h3 style="margin-bottom: 10px;">Find Coordinate's Word</h3>
                    <input type="number" id="coordInput" placeholder="Enter coordinate (0-99)" min="0" max="99">
                    <button onclick="lookupCoordinate()" style="margin-top: 10px;">Find Word</button>
                    <div id="coordResult" class="lookup-result"></div>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h2>Complete Coordinate Dictionary</h2>
            <div id="dictionary" class="dictionary-scroll"></div>
        </div>
    </div>
    
    <script>
        // This will be populated by the Python script
        const coordinateMapping = COORDINATE_MAPPING_PLACEHOLDER;
        
        // Initialize the grid
        function initializeGrid() {
            const grid = document.getElementById('vectorGrid');
            grid.innerHTML = '';
            
            for (let i = 0; i < 100; i++) {
                const cell = document.createElement('div');
                cell.className = 'coord-cell inactive';
                cell.dataset.coord = i;
                cell.textContent = i;
                
                const tooltip = document.createElement('div');
                tooltip.className = 'tooltip';
                tooltip.textContent = coordinateMapping[i] || 'Empty';
                cell.appendChild(tooltip);
                
                cell.addEventListener('click', () => {
                    showCoordinateInfo(i);
                });
                
                grid.appendChild(cell);
            }
        }
        
        function analyzeText() {
            const text = document.getElementById('textInput').value;
            if (!text) return;
            
            // This would normally call the Python backend
            // For demo, we'll simulate with random activation
            const activeCoords = simulateTextAnalysis(text);
            updateGrid(activeCoords);
            showActiveWords(activeCoords);
        }
        
        function simulateTextAnalysis(text) {
            const words = text.toLowerCase().split(/\\s+/);
            const activeCoords = [];
            
            // Find which words from input match our vocabulary
            words.forEach(word => {
                for (let coord in coordinateMapping) {
                    if (coordinateMapping[coord].includes(word)) {
                        activeCoords.push({
                            coord: parseInt(coord),
                            word: coordinateMapping[coord],
                            weight: Math.random() * 0.8 + 0.2
                        });
                    }
                }
            });
            
            return activeCoords;
        }
        
        function updateGrid(activeCoords) {
            // Reset all cells
            document.querySelectorAll('.coord-cell').forEach(cell => {
                cell.className = 'coord-cell inactive';
            });
            
            // Activate relevant cells
            activeCoords.forEach(item => {
                const cell = document.querySelector(`[data-coord="${item.coord}"]`);
                if (cell) {
                    let intensity = 'verylow';
                    if (item.weight > 0.7) intensity = 'high';
                    else if (item.weight > 0.5) intensity = 'medium';
                    else if (item.weight > 0.3) intensity = 'low';
                    
                    cell.className = `coord-cell active ${intensity}`;
                }
            });
        }
        
        function showActiveWords(activeCoords) {
            const container = document.getElementById('activeWords');
            container.innerHTML = '<h3 style="margin-bottom: 10px;">Active Terms:</h3>';
            
            activeCoords.sort((a, b) => b.weight - a.weight);
            
            activeCoords.slice(0, 10).forEach(item => {
                const tag = document.createElement('div');
                tag.className = 'word-tag';
                tag.innerHTML = `
                    ${item.word}
                    <span class="coord">#${item.coord}</span>
                `;
                container.appendChild(tag);
            });
        }
        
        function lookupWord() {
            const word = document.getElementById('wordInput').value.toLowerCase();
            const resultDiv = document.getElementById('wordResult');
            
            for (let coord in coordinateMapping) {
                if (coordinateMapping[coord] === word) {
                    resultDiv.innerHTML = `✅ "${word}" → Coordinate <span class="coord-num">${coord}</span>`;
                    highlightCoordinate(parseInt(coord));
                    return;
                }
            }
            
            resultDiv.innerHTML = `❌ "${word}" not in vocabulary`;
        }
        
        function lookupCoordinate() {
            const coord = parseInt(document.getElementById('coordInput').value);
            const resultDiv = document.getElementById('coordResult');
            
            if (coord >= 0 && coord < 100 && coordinateMapping[coord]) {
                resultDiv.innerHTML = `✅ Coordinate <span class="coord-num">${coord}</span> → "${coordinateMapping[coord]}"`;
                highlightCoordinate(coord);
            } else {
                resultDiv.innerHTML = `❌ Invalid coordinate`;
            }
        }
        
        function highlightCoordinate(coord) {
            // Remove previous highlights
            document.querySelectorAll('.coord-cell').forEach(cell => {
                cell.style.border = '';
            });
            
            // Highlight the specific coordinate
            const cell = document.querySelector(`[data-coord="${coord}"]`);
            if (cell) {
                cell.style.border = '3px solid #dc2626';
                cell.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }
        
        function showCoordinateInfo(coord) {
            const word = coordinateMapping[coord] || 'Empty';
            alert(`Coordinate ${coord} = "${word}"`);
        }
        
        function initializeDictionary() {
            const dict = document.getElementById('dictionary');
            dict.innerHTML = '';
            
            for (let coord = 0; coord < 100; coord++) {
                const entry = document.createElement('div');
                entry.className = 'dict-entry';
                entry.innerHTML = `
                    <span class="coord-num">[${String(coord).padStart(2, '0')}]</span>
                    <span>${coordinateMapping[coord] || 'Empty'}</span>
                `;
                entry.addEventListener('click', () => highlightCoordinate(coord));
                dict.appendChild(entry);
            }
        }
        
        // Initialize on load
        initializeGrid();
        initializeDictionary();
    </script>
</body>
</html>
    """
    
    # Get coordinate mapping
    mapping = explorer.get_coordinate_mapping()
    
    # Replace placeholder with actual mapping
    mapping_json = json.dumps(mapping)
    html_content = html_content.replace('COORDINATE_MAPPING_PLACEHOLDER', mapping_json)
    
    # Save HTML file
    with open('interactive_vector_explorer.html', 'w') as f:
        f.write(html_content)
    
    print("\nInteractive HTML explorer saved to: interactive_vector_explorer.html")


def main():
    """
    Run the interactive vector explorer demonstration
    """
    print("="*80)
    print("INTERACTIVE TF-IDF VECTOR EXPLORER")
    print("="*80)
    
    # Create explorer
    explorer, vectorizer = create_interactive_demo()
    
    # Demonstrate word-coordinate lookup
    demonstrate_word_coordinate_lookup(explorer)
    
    # Analyze sample text
    sample_text = "Neural networks use deep learning algorithms"
    print("\n" + "="*80)
    print("TEXT ANALYSIS DEMONSTRATION")
    print("="*80)
    
    # Show visual map
    visual_map = explorer.create_visual_map(sample_text)
    print(visual_map)
    
    # Export coordinate dictionary
    dictionary = explorer.export_coordinate_dictionary()
    with open('coordinate_dictionary.json', 'w') as f:
        json.dump(dictionary, f, indent=2)
    print("\nCoordinate dictionary exported to: coordinate_dictionary.json")
    
    # Create interactive HTML
    create_interactive_html_explorer(explorer)
    
    return explorer, vectorizer


if __name__ == "__main__":
    explorer, vectorizer = main()
