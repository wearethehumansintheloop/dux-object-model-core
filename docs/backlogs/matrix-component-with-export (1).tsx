import React, { useRef } from 'react';

interface Matrix2x2Props {
  title: string;
  xAxisLabel: string;
  yAxisLabel: string;
  quadrants: {
    topLeft: { header: string; points: string[] };
    topRight: { header: string; points: string[] };
    bottomLeft: { header: string; points: string[] };
    bottomRight: { header: string; points: string[] };
  };
  insight?: string;
  citations?: string[];
}

export default function Matrix2x2({
  title = 'Matrix Analysis',
  xAxisLabel = 'X Axis',
  yAxisLabel = 'Y Axis',
  quadrants = {
    topLeft: { header: 'Top Left', points: [] },
    topRight: { header: 'Top Right', points: [] },
    bottomLeft: { header: 'Bottom Left', points: [] },
    bottomRight: { header: 'Bottom Right', points: [] }
  },
  insight,
  citations = []
}: Matrix2x2Props) {
  const slideRef = useRef<HTMLDivElement>(null);

  // Ensure quadrants have all required properties
  const safeQuadrants = {
    topLeft: quadrants.topLeft || { header: 'Top Left', points: [] },
    topRight: quadrants.topRight || { header: 'Top Right', points: [] },
    bottomLeft: quadrants.bottomLeft || { header: 'Bottom Left', points: [] },
    bottomRight: quadrants.bottomRight || { header: 'Bottom Right', points: [] }
  };

  // Export function that returns PowerPoint-ready data
  const exportForPowerPoint = () => {
    const exportData = {
      slideType: 'matrix2x2',
      dimensions: {
        width: 1920,
        height: 1080,
        grid: {
          columns: 16,
          rows: 9,
          gutterWidth: 32,
          marginWidth: 32
        }
      },
      elements: [
        {
          type: 'text',
          content: title,
          style: {
            fontSize: 32,
            bold: true,
            color: '#000000'
          },
          position: {
            gridColumn: { start: 1, end: 14 },
            gridRow: { start: 1, end: 2 },
            alignment: 'left'
          }
        },
        {
          type: 'shape',
          shapeType: 'rectangle',
          style: {
            fill: '#FFFFFF',
            border: { width: 2, color: '#000000' }
          },
          position: {
            gridColumn: { start: 2, end: 8 },
            gridRow: { start: 3, end: 6 }
          },
          content: {
            header: safeQuadrants.topLeft.header,
            bullets: safeQuadrants.topLeft.points
          }
        },
        {
          type: 'shape',
          shapeType: 'rectangle',
          style: {
            fill: '#F5F5F5',
            border: { width: 2, color: '#000000' }
          },
          position: {
            gridColumn: { start: 8, end: 14 },
            gridRow: { start: 3, end: 6 }
          },
          content: {
            header: safeQuadrants.topRight.header,
            bullets: safeQuadrants.topRight.points
          }
        },
        {
          type: 'shape',
          shapeType: 'rectangle',
          style: {
            fill: '#E0E0E0',
            border: { width: 2, color: '#000000' }
          },
          position: {
            gridColumn: { start: 2, end: 8 },
            gridRow: { start: 6, end: 9 }
          },
          content: {
            header: safeQuadrants.bottomLeft.header,
            bullets: safeQuadrants.bottomLeft.points
          }
        },
        {
          type: 'shape',
          shapeType: 'rectangle',
          style: {
            fill: '#D0D0D0',
            border: { width: 2, color: '#000000' }
          },
          position: {
            gridColumn: { start: 8, end: 14 },
            gridRow: { start: 6, end: 9 }
          },
          content: {
            header: safeQuadrants.bottomRight.header,
            bullets: safeQuadrants.bottomRight.points
          }
        },
        {
          type: 'text',
          content: xAxisLabel,
          style: { fontSize: 14, color: '#333333' },
          position: {
            gridColumn: { start: 2, end: 14 },
            gridRow: { start: 9, end: 9 },
            alignment: 'center'
          }
        },
        {
          type: 'text',
          content: yAxisLabel,
          style: { fontSize: 14, color: '#333333', rotation: -90 },
          position: {
            gridColumn: { start: 1, end: 2 },
            gridRow: { start: 3, end: 9 },
            alignment: 'center'
          }
        }
      ]
    };

    if (insight) {
      exportData.elements.push({
        type: 'text',
        content: insight,
        style: { fontSize: 16, italic: true, color: '#666666' },
        position: {
          gridColumn: { start: 2, end: 14 },
          gridRow: { start: 9, end: 9 },
          alignment: 'center'
        }
      });
    }

    return exportData;
  };

  const downloadAsImage = async () => {
    // Create a complete SVG representation of the matrix
    const escapeXml = (str: string) => {
      return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&apos;');
    };

    const createBulletPoints = (points: string[], x: number, y: number) => {
      return points.map((point, i) => 
        `<text x="${x}" y="${y + (i * 25)}" font-size="14" fill="#333">• ${escapeXml(point)}</text>`
      ).join('\n');
    };

    const svgContent = `
      <svg width="1920" height="1080" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">
        <!-- Background -->
        <rect width="1920" height="1080" fill="white"/>
        
        <!-- Title -->
        <text x="64" y="80" font-size="32" font-weight="bold" fill="#000">${escapeXml(title)}</text>
        
        <!-- Main Matrix Container -->
        <g transform="translate(128, 180)">
          <!-- Background rectangles for quadrants -->
          <rect x="0" y="0" width="600" height="300" fill="white" stroke="black" stroke-width="2"/>
          <rect x="600" y="0" width="600" height="300" fill="#F5F5F5" stroke="black" stroke-width="2"/>
          <rect x="0" y="300" width="600" height="300" fill="#E0E0E0" stroke="black" stroke-width="2"/>
          <rect x="600" y="300" width="600" height="300" fill="#D0D0D0" stroke="black" stroke-width="2"/>
          
          <!-- Cross lines -->
          <line x1="0" y1="300" x2="1200" y2="300" stroke="black" stroke-width="3"/>
          <line x1="600" y1="0" x2="600" y2="600" stroke="black" stroke-width="3"/>
          
          <!-- Quadrant content -->
          <!-- Top Left -->
          <text x="20" y="40" font-size="18" font-weight="bold" fill="#000">${escapeXml(safeQuadrants.topLeft.header)}</text>
          ${createBulletPoints(safeQuadrants.topLeft.points || [], 20, 70)}
          
          <!-- Top Right -->
          <text x="620" y="40" font-size="18" font-weight="bold" fill="#000">${escapeXml(safeQuadrants.topRight.header)}</text>
          ${createBulletPoints(safeQuadrants.topRight.points || [], 620, 70)}
          
          <!-- Bottom Left -->
          <text x="20" y="340" font-size="18" font-weight="bold" fill="#000">${escapeXml(safeQuadrants.bottomLeft.header)}</text>
          ${createBulletPoints(safeQuadrants.bottomLeft.points || [], 20, 370)}
          
          <!-- Bottom Right -->
          <text x="620" y="340" font-size="18" font-weight="bold" fill="#000">${escapeXml(safeQuadrants.bottomRight.header)}</text>
          ${createBulletPoints(safeQuadrants.bottomRight.points || [], 620, 370)}
          
          <!-- Axis Labels -->
          <text x="600" y="650" text-anchor="middle" font-size="16" fill="#333">${escapeXml(xAxisLabel)}</text>
          <text x="-300" y="-20" transform="rotate(-90)" text-anchor="middle" font-size="16" fill="#333">${escapeXml(yAxisLabel)}</text>
        </g>
        
        <!-- Insight -->
        ${insight ? `<text x="960" y="900" text-anchor="middle" font-size="18" font-style="italic" fill="#666">${escapeXml(insight)}</text>` : ''}
        
        <!-- Citations -->
        ${citations.length > 0 ? `<text x="64" y="1040" font-size="12" fill="#999">Sources: ${escapeXml(citations.join(', '))}</text>` : ''}
      </svg>
    `;
    
    const blob = new Blob([svgContent], { type: 'image/svg+xml;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.download = `${title.replace(/\s+/g, '-')}.svg`;
    link.href = url;
    link.click();
    URL.revokeObjectURL(url);
  };

  const downloadAsJSON = () => {
    const data = exportForPowerPoint();
    const json = JSON.stringify(data, null, 2);
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.download = `${title.replace(/\s+/g, '-')}-export.json`;
    link.href = url;
    link.click();
  };

  return (
    <div className="w-full max-w-7xl mx-auto p-4">
      {/* Export buttons */}
      <div className="flex gap-2 mb-4">
        <button
          onClick={downloadAsImage}
          className="px-4 py-2 bg-gray-800 text-white rounded hover:bg-gray-700"
        >
          Export as SVG
        </button>
        <button
          onClick={downloadAsJSON}
          className="px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-500"
        >
          Export for PowerPoint
        </button>
        </div>
      
      {/* Demo Example */}
      <div className="mt-8 p-4 bg-gray-100 rounded">
        <h3 className="font-bold mb-2">Example Usage:</h3>
        <pre className="text-xs overflow-x-auto">
{`<Matrix2x2
  title="Strategic Options Matrix"
  xAxisLabel="Cost"
  yAxisLabel="Value"
  quadrants={{
    topLeft: { header: "PURSUE", points: ["Quick wins", "Scale fast"] },
    topRight: { header: "SELECTIVE", points: ["Major bets", "ROI focus"] },
    bottomLeft: { header: "AVOID", points: ["Resource drain"] },
    bottomRight: { header: "MINIMIZE", points: ["Reduce exposure"] }
  }}
  insight="70% of initiatives fall in high-cost/low-value quadrant"
  citations={["FinOps Foundation 2024"]}
/>`}
        </pre>
      </div>
    </div>

      {/* Slide container with 16-column grid */}
      <div
        ref={slideRef}
        className="bg-white aspect-video p-8"
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(16, 1fr)',
          gridTemplateRows: 'repeat(9, 1fr)',
          gap: '2rem',
          boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)'
        }}
      >
        {/* Title */}
        <h1
          className="text-3xl font-bold text-black"
          style={{ gridColumn: '1 / 15', gridRow: '1 / 2' }}
        >
          {title}
        </h1>

        {/* Y-axis label */}
        <div
          className="flex items-center justify-center"
          style={{
            gridColumn: '1 / 2',
            gridRow: '3 / 9',
            writingMode: 'vertical-rl',
            transform: 'rotate(180deg)'
          }}
        >
          <span className="text-sm text-gray-700">{yAxisLabel}</span>
        </div>

        {/* Matrix container */}
        <div
          className="relative"
          style={{
            gridColumn: '2 / 15',
            gridRow: '3 / 8',
            display: 'grid',
            gridTemplateColumns: '1fr 1fr',
            gridTemplateRows: '1fr 1fr',
            gap: '2px',
            backgroundColor: '#000'
          }}
        >
          {/* Top Left Quadrant */}
          <div className="bg-white p-4">
            <h3 className="font-bold text-base mb-2">{safeQuadrants.topLeft.header}</h3>
            <ul className="text-sm space-y-1">
              {(safeQuadrants.topLeft.points || []).map((point, i) => (
                <li key={i} className="flex">
                  <span className="mr-2">•</span>
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Top Right Quadrant */}
          <div className="p-4" style={{ backgroundColor: '#F5F5F5' }}>
            <h3 className="font-bold text-base mb-2">{safeQuadrants.topRight.header}</h3>
            <ul className="text-sm space-y-1">
              {(safeQuadrants.topRight.points || []).map((point, i) => (
                <li key={i} className="flex">
                  <span className="mr-2">•</span>
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Bottom Left Quadrant */}
          <div className="p-4" style={{ backgroundColor: '#E0E0E0' }}>
            <h3 className="font-bold text-base mb-2">{safeQuadrants.bottomLeft.header}</h3>
            <ul className="text-sm space-y-1">
              {(safeQuadrants.bottomLeft.points || []).map((point, i) => (
                <li key={i} className="flex">
                  <span className="mr-2">•</span>
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Bottom Right Quadrant */}
          <div className="p-4" style={{ backgroundColor: '#D0D0D0' }}>
            <h3 className="font-bold text-base mb-2">{safeQuadrants.bottomRight.header}</h3>
            <ul className="text-sm space-y-1">
              {(safeQuadrants.bottomRight.points || []).map((point, i) => (
                <li key={i} className="flex">
                  <span className="mr-2">•</span>
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Axis lines */}
          <div
            className="absolute bg-black"
            style={{
              top: '50%',
              left: 0,
              right: 0,
              height: '2px',
              transform: 'translateY(-50%)'
            }}
          />
          <div
            className="absolute bg-black"
            style={{
              left: '50%',
              top: 0,
              bottom: 0,
              width: '2px',
              transform: 'translateX(-50%)'
            }}
          />
        </div>

        {/* X-axis label */}
        <div
          className="flex items-center justify-center text-sm text-gray-700"
          style={{ gridColumn: '2 / 15', gridRow: '8 / 9' }}
        >
          {xAxisLabel}
        </div>

        {/* Insight */}
        {insight && (
          <div
            className="text-center italic text-gray-600"
            style={{ gridColumn: '2 / 15', gridRow: '8 / 9', alignSelf: 'end' }}
          >
            {insight}
          </div>
        )}

        {/* Citations */}
        {citations.length > 0 && (
          <div
            className="text-xs text-gray-500"
            style={{ gridColumn: '1 / 17', gridRow: '9 / 10' }}
          >
            Sources: {citations.join(', ')}
          </div>
        )}
      </div>
    </div>
  );
}