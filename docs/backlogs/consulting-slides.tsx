import React, { useState, useRef } from 'react';
import { Download, Grid, BarChart3, GitBranch, Map, Target, PieChart } from 'lucide-react';

// Carbon Design 16-column grid utilities
const GridContainer = ({ children, className = "" }) => (
  <div className={`grid grid-cols-16 gap-4 h-full ${className}`}>
    {children}
  </div>
);

const GridCol = ({ span = 1, start, children, className = "" }) => {
  const spanClass = `col-span-${span}`;
  const startClass = start ? `col-start-${start}` : '';
  return (
    <div className={`${spanClass} ${startClass} ${className}`}>
      {children}
    </div>
  );
};

// Slide Header Component
const SlideHeader = ({ questionWord, title, subtitle }) => (
  <div className="mb-8">
    <h1 className="text-2xl font-normal text-gray-900 border-b border-gray-300 pb-2">
      <span className="text-blue-500 font-medium">{questionWord}</span> {title}
    </h1>
    {subtitle && <p className="text-sm text-gray-600 mt-2">{subtitle}</p>}
  </div>
);

// Slide Footer Component
const SlideFooter = ({ footnote, source, companyName, pageNumber }) => (
  <div className="absolute bottom-4 left-4 right-4 flex justify-between items-end text-xs text-gray-600">
    <div>
      {footnote && <div className="mb-1">Footnote: {footnote}</div>}
      {source && <div>Source: {source}</div>}
    </div>
    <div className="flex items-center gap-2">
      <span>{companyName}</span>
      <span className="bg-gray-800 text-white px-2 py-1 rounded">{pageNumber}</span>
    </div>
  </div>
);

// Matrix2x2 Component matching your existing interface
const Matrix2x2Component = ({ 
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
}) => {
  const slideRef = useRef(null);

  // Ensure quadrants have all required properties
  const safeQuadrants = {
    topLeft: quadrants.topLeft || { header: 'Top Left', points: [] },
    topRight: quadrants.topRight || { header: 'Top Right', points: [] },
    bottomLeft: quadrants.bottomLeft || { header: 'Bottom Left', points: [] },
    bottomRight: quadrants.bottomRight || { header: 'Bottom Right', points: [] }
  const downloadAsJSON = () => {
    const data = exportToPowerPoint();
    const json = JSON.stringify(data, null, 2);
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.download = `${title.replace(/\s+/g, '-')}-export.json`;
    link.href = url;
    link.click();
    URL.revokeObjectURL(url);
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

  // Export function that returns PowerPoint-ready data (matching your exact format)
  const exportToPowerPoint = () => {
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

    // Add insight if it exists
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
    const escapeXml = (str) => {
      return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&apos;');
    };

    const createBulletPoints = (points, x, y) => {
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

  return (
    <div ref={slideRef} className="relative min-h-screen bg-white p-8">
      <SlideHeader 
        questionWord="II." 
        title={title}
      />
      
      <GridContainer>
        <GridCol span={9}>
          <div className="relative h-96 bg-gray-100 border border-gray-300">
            {/* Y-axis label */}
            <div className="absolute -left-12 top-1/2 transform -rotate-90 -translate-y-1/2 text-sm font-medium">
              {yAxisLabel}
            </div>
            
            {/* Y-axis values */}
            <div className="absolute -left-8 top-4 text-xs text-gray-600">High</div>
            <div className="absolute -left-8 top-1/2 text-xs text-gray-600">Mid</div>
            <div className="absolute -left-8 bottom-4 text-xs text-gray-600">Low</div>
            
            {/* X-axis label */}
            <div className="absolute bottom-12 left-1/2 transform -translate-x-1/2 text-sm font-medium">
              {xAxisLabel}
            </div>
            
            {/* X-axis values */}
            <div className="absolute bottom-4 left-4 text-xs text-gray-600">Low</div>
            <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 text-xs text-gray-600">Mid</div>
            <div className="absolute bottom-4 right-4 text-xs text-gray-600">High</div>
            
            {/* Grid lines */}
            <div className="absolute top-0 left-1/2 w-px h-full bg-gray-300"></div>
            <div className="absolute top-1/2 left-0 w-full h-px bg-gray-300"></div>
            
            {/* Quadrants */}
            <div className="absolute top-0 left-0 w-1/2 h-1/2 p-4 flex flex-col justify-center items-center text-center">
              <h4 className="font-medium text-sm mb-2">{safeQuadrants.topLeft.header}</h4>
              <div className="space-y-1">
                {safeQuadrants.topLeft.points.map((point, index) => (
                  <div key={index} className="w-3 h-3 bg-blue-500 rounded-full mx-auto"></div>
                ))}
              </div>
              {safeQuadrants.topLeft.points.length === 0 && (
                <div className="text-xs text-gray-500">[Insert solution/initiative]</div>
              )}
            </div>
            
            <div className="absolute top-0 right-0 w-1/2 h-1/2 p-4 flex flex-col justify-center items-center text-center">
              <h4 className="font-medium text-sm mb-2">{safeQuadrants.topRight.header}</h4>
              <div className="space-y-1">
                {safeQuadrants.topRight.points.map((point, index) => (
                  <div key={index} className="w-3 h-3 bg-blue-500 rounded-full mx-auto"></div>
                ))}
              </div>
              {safeQuadrants.topRight.points.length === 0 && (
                <div className="text-xs text-gray-500">[Insert solution/initiative]</div>
              )}
            </div>
            
            <div className="absolute bottom-0 left-0 w-1/2 h-1/2 p-4 flex flex-col justify-center items-center text-center">
              <h4 className="font-medium text-sm mb-2">{safeQuadrants.bottomLeft.header}</h4>
              <div className="space-y-1">
                {safeQuadrants.bottomLeft.points.map((point, index) => (
                  <div key={index} className="w-3 h-3 bg-blue-500 rounded-full mx-auto"></div>
                ))}
              </div>
              {safeQuadrants.bottomLeft.points.length === 0 && (
                <div className="text-xs text-gray-500">[Insert solution/initiative]</div>
              )}
            </div>
            
            <div className="absolute bottom-0 right-0 w-1/2 h-1/2 p-4 flex flex-col justify-center items-center text-center">
              <h4 className="font-medium text-sm mb-2">{safeQuadrants.bottomRight.header}</h4>
              <div className="space-y-1">
                {safeQuadrants.bottomRight.points.map((point, index) => (
                  <div key={index} className="w-3 h-3 bg-blue-500 rounded-full mx-auto"></div>
                ))}
              </div>
              {safeQuadrants.bottomRight.points.length === 0 && (
                <div className="text-xs text-gray-500">[Insert solution/initiative]</div>
              )}
            </div>
          </div>
        </GridCol>
        
        <GridCol span={6} className="ml-8">
          <div className="h-96 flex flex-col">
            {/* Priority section */}
            <div className="flex-1">
              <h3 className="font-semibold text-lg mb-4">Prioritized initiatives</h3>
              <p className="text-sm text-gray-600 mb-6">[Insert description]</p>
              
              {/* Decorative arrow */}
              <div className="w-0 h-0 border-l-8 border-r-8 border-b-16 border-l-transparent border-r-transparent border-b-gray-800 mx-auto mb-6"></div>
              
              <div className="border-t border-gray-300 border-dashed mb-6"></div>
            </div>
            
            {/* Backlog section */}
            <div className="flex-1">
              <h3 className="font-semibold text-lg mb-4">Backlog</h3>
              <p className="text-sm text-gray-600">[Insert description]</p>
            </div>
            
            {/* Insight section */}
            {insight && (
              <div className="mt-4 p-4 bg-yellow-50 border border-yellow-200 border-dashed">
                <div className="text-sm text-gray-700">{insight}</div>
              </div>
            )}
            
            {/* Citations */}
            {citations.length > 0 && (
              <div className="mt-4 text-xs text-gray-500">
                <div className="font-medium mb-1">Citations:</div>
                {citations.map((citation, index) => (
                  <div key={index}>• {citation}</div>
                ))}
              </div>
            )}
          </div>
        </GridCol>
      </GridContainer>
      
      <SlideFooter 
        footnote="1. xx"
        source="xx"
        companyName="Company Name"
        pageNumber="10"
      />
      
      {/* Export buttons */}
      <div className="absolute top-4 right-4 flex gap-2">
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
    </div>
  );
};

// DataVizSplit Component
const DataVizSplitComponent = ({ data }) => {
  const exportToPowerPoint = () => {
    const ppData = {
      type: 'dataVizSplit',
      layout: {
        header: { x: 0, y: 0, width: 16, height: 2 },
        leftPanel: { x: 0, y: 3, width: 8, height: 9 },
        rightPanel: { x: 9, y: 3, width: 7, height: 9 },
        footer: { x: 0, y: 14, width: 16, height: 1 }
      },
      content: data
    };
    
    console.log('PowerPoint Export Data:', JSON.stringify(ppData, null, 2));
    alert('PowerPoint export data logged to console');
  };

  return (
    <div className="relative min-h-screen bg-white p-8">
      <SlideHeader 
        questionWord={data.questionWord}
        title={data.title}
        subtitle={data.subtitle}
      />
      
      <GridContainer>
        <GridCol span={8}>
          <div className="h-96 bg-gray-50 border border-gray-200 p-6 flex flex-col justify-center">
            {data.type === 'waterfall' && (
              <div className="space-y-4">
                <div className="text-sm text-gray-600 mb-4">[Insert numerical goal, if applicable]: xx [currency]</div>
                <div className="flex items-end space-x-4 h-64">
                  <div className="bg-gray-800 text-white p-4 h-full flex items-center justify-center text-lg font-medium">
                    Xx [currency]
                  </div>
                  <div className="text-2xl text-gray-400">→</div>
                  <div className="space-y-2 flex-1">
                    {data.segments.map((segment, index) => (
                      <div key={index} className="bg-blue-500 text-white p-3 text-center text-sm">
                        {segment.value} • {segment.label}
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}
            
            {data.type === 'chart' && (
              <div className="h-full flex items-center justify-center text-gray-500">
                <PieChart size={120} />
                <div className="ml-8 text-sm space-y-2">
                  {data.chartData.map((item, index) => (
                    <div key={index} className="flex items-center space-x-2">
                      <div className={`w-3 h-3 ${item.color}`}></div>
                      <span>{item.label}: {item.value}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </GridCol>
        
        <GridCol span={7} className="ml-4">
          <div className="space-y-6">
            {data.rightContent.map((section, index) => (
              <div key={index}>
                <h3 className="text-blue-500 font-medium mb-2">[{section.title}]:</h3>
                <p className="text-sm text-gray-700">[{section.description}]</p>
                {section.callout && (
                  <div className="mt-4 p-4 bg-yellow-50 border border-yellow-200 border-dashed text-sm">
                    {section.callout}
                  </div>
                )}
              </div>
            ))}
          </div>
        </GridCol>
      </GridContainer>
      
      <SlideFooter 
        footnote={data.footnote}
        source={data.source}
        companyName="Company Name"
        pageNumber={data.pageNumber}
      />
      
      <button
        onClick={exportToPowerPoint}
        className="absolute top-4 right-4 flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        <Download size={16} />
        Export to PowerPoint
      </button>
    </div>
  );
};

// ProcessFlow Component
const ProcessFlowComponent = ({ data }) => {
  const exportToPowerPoint = () => {
    const ppData = {
      type: 'processFlow',
      layout: {
        header: { x: 0, y: 0, width: 16, height: 2 },
        content: { x: 0, y: 3, width: 16, height: 9 },
        footer: { x: 0, y: 14, width: 16, height: 1 }
      },
      content: data
    };
    
    console.log('PowerPoint Export Data:', JSON.stringify(ppData, null, 2));
    alert('PowerPoint export data logged to console');
  };

  return (
    <div className="relative min-h-screen bg-white p-8">
      <SlideHeader 
        questionWord={data.questionWord}
        title={data.title}
      />
      
      <div className="grid grid-cols-3 gap-8 h-96">
        {data.columns.map((column, index) => (
          <div key={index} className="text-center">
            <h3 className="font-semibold text-lg mb-6 border-b border-gray-300 pb-2">
              {column.title}
            </h3>
            
            <div className="space-y-6">
              {column.items.map((item, itemIndex) => (
                <div key={itemIndex} className="flex flex-col items-center">
                  <div className="w-16 h-16 bg-gray-100 border border-gray-300 rounded-lg flex items-center justify-center mb-3">
                    {item.icon}
                  </div>
                  <div className="text-sm">
                    <div className="font-medium">[{item.title}]</div>
                    <div className="text-gray-600 mt-1">[{item.description}]</div>
                  </div>
                </div>
              ))}
            </div>
            
            {index < data.columns.length - 1 && (
              <div className="absolute top-1/2 transform -translate-y-1/2 text-2xl text-gray-400"
                   style={{ left: `${(index + 1) * 33.33 - 3}%` }}>
                →
              </div>
            )}
          </div>
        ))}
      </div>
      
      <SlideFooter 
        footnote={data.footnote}
        source={data.source}
        companyName="Company Name"
        pageNumber={data.pageNumber}
      />
      
      <button
        onClick={exportToPowerPoint}
        className="absolute top-4 right-4 flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        <Download size={16} />
        Export to PowerPoint
      </button>
    </div>
  );
};

// JourneyMap Component
const JourneyMapComponent = ({ data }) => {
  const exportToPowerPoint = () => {
    const ppData = {
      type: 'journeyMap',
      layout: {
        header: { x: 0, y: 0, width: 16, height: 2 },
        leftPanel: { x: 0, y: 3, width: 6, height: 9 },
        rightPanel: { x: 7, y: 3, width: 9, height: 9 },
        footer: { x: 0, y: 14, width: 16, height: 1 }
      },
      content: data
    };
    
    console.log('PowerPoint Export Data:', JSON.stringify(ppData, null, 2));
    alert('PowerPoint export data logged to console');
  };

  return (
    <div className="relative min-h-screen bg-white p-8">
      <SlideHeader 
        questionWord={data.questionWord}
        title={data.title}
      />
      
      <GridContainer>
        <GridCol span={6}>
          <div className="h-96 flex flex-col justify-center">
            <h2 className="text-xl font-semibold mb-8 leading-tight">
              {data.leftTitle}
            </h2>
          </div>
        </GridCol>
        
        <GridCol span={10}>
          <div className="space-y-8">
            {/* High priority pain points */}
            <div>
              <h3 className="font-semibold mb-4">High priority pain points</h3>
              <div className="grid grid-cols-3 gap-4">
                {data.highPriorityPainPoints.map((point, index) => (
                  <div key={index} className="text-center">
                    <div className="w-12 h-12 bg-gray-100 border border-gray-300 rounded-lg flex items-center justify-center mb-2 mx-auto">
                      {point.icon}
                    </div>
                    <div className="text-sm">
                      <div className="font-medium">[{point.title}]</div>
                      <div className="text-gray-600 mt-1">[{point.description}]</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
            
            <div className="border-t border-gray-300"></div>
            
            {/* Medium/lesser priority pain points */}
            <div>
              <h3 className="font-semibold mb-4">Medium/lesser priority pain points</h3>
              <div className="grid grid-cols-4 gap-4">
                {data.mediumPriorityPainPoints.map((point, index) => (
                  <div key={index} className="text-center">
                    <div className="w-12 h-12 bg-gray-100 border border-gray-300 rounded-lg flex items-center justify-center mb-2 mx-auto">
                      {point.icon}
                    </div>
                    <div className="text-sm">
                      <div className="font-medium">[{point.title}]</div>
                      <div className="text-gray-600 mt-1">[{point.description}]</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </GridCol>
      </GridContainer>
      
      <SlideFooter 
        footnote={data.footnote}
        source={data.source}
        companyName="Company Name"
        pageNumber={data.pageNumber}
      />
      
      <button
        onClick={exportToPowerPoint}
        className="absolute top-4 right-4 flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        <Download size={16} />
        Export to PowerPoint
      </button>
    </div>
  );
};

// Main App Component
const ConsultingSlides = () => {
  const [activeComponent, setActiveComponent] = useState('matrix2x2');

  // Sample data for each component - now matching your interface
  const matrix2x2Data = {
    title: 'Prioritization of [features/components/segments]',
    xAxisLabel: 'Feasibility',
    yAxisLabel: 'Impact',
    quadrants: {
      topLeft: { 
        header: 'High Impact, Low Feasibility', 
        points: ['Initiative A', 'Initiative B'] 
      },
      topRight: { 
        header: 'High Impact, High Feasibility', 
        points: ['Initiative C'] 
      },
      bottomLeft: { 
        header: 'Low Impact, Low Feasibility', 
        points: [] 
      },
      bottomRight: { 
        header: 'Low Impact, High Feasibility', 
        points: ['Initiative D'] 
      }
    },
    insight: 'Focus on high-impact, high-feasibility initiatives first',
    citations: ['McKinsey Analysis 2024', 'Internal Strategy Review']
  };

  const dataVizSplitData = {
    questionWord: 'What',
    title: 'will improve [area of strategic initiative]?',
    subtitle: '[Insert numerical goal, if applicable]: xx [currency]',
    type: 'waterfall',
    segments: [
      { value: 'xx%', label: 'Cost cutting/efficiency lever' },
      { value: 'xx%', label: 'Cost cutting/efficiency lever' },
      { value: 'xx%', label: 'Cost cutting/efficiency lever' }
    ],
    rightContent: [
      { title: 'Cost cutting/efficiency lever', description: 'Insert description' },
      { title: 'Cost cutting/efficiency lever', description: 'Insert description' },
      { title: 'Cost cutting/efficiency lever', description: 'Insert description' }
    ],
    footnote: '1. xx',
    source: 'xx',
    pageNumber: '2'
  };

  const processFlowData = {
    questionWord: 'What',
    title: 'will [increase efficiency/reduce costs]?',
    columns: [
      {
        title: 'Focus areas',
        items: [
          { icon: <Grid size={20} />, title: 'Insert focus area/efficiency lever', description: 'Insert examples of lever' },
          { icon: <GitBranch size={20} />, title: 'Insert focus area/efficiency lever', description: 'Insert examples of lever' },
          { icon: <Target size={20} />, title: 'Insert focus area/efficiency lever', description: 'Insert examples of lever' }
        ]
      },
      {
        title: 'Examples of levers',
        items: [
          { icon: '•', title: 'Insert examples of lever', description: '' },
          { icon: '•', title: 'Insert examples of lever', description: '' },
          { icon: '•', title: 'Insert examples of lever', description: '' }
        ]
      },
      {
        title: 'Target 202x',
        items: [
          { icon: <BarChart3 size={32} className="text-blue-500" />, title: 'Insert numerical target for efficiency gains', description: '' }
        ]
      }
    ],
    footnote: '[sanitized]',
    source: '[sanitized]',
    pageNumber: '4'
  };

  const journeyMapData = {
    questionWord: 'There are significant',
    title: '[barriers/pain points] along the customer journey that lead [insert]',
    leftTitle: 'There are significant [barriers/pain points] along the customer journey that lead [insert]',
    highPriorityPainPoints: [
      { icon: <Grid size={16} />, title: 'Insert pain point', description: 'Insert description' },
      { icon: <GitBranch size={16} />, title: 'Insert pain point', description: 'Insert description' },
      { icon: <Target size={16} />, title: 'Insert pain point', description: 'Insert description' }
    ],
    mediumPriorityPainPoints: [
      { icon: <Map size={16} />, title: 'Insert pain point', description: 'Insert description' },
      { icon: <PieChart size={16} />, title: 'Insert pain point', description: 'Insert description' },
      { icon: <BarChart3 size={16} />, title: 'Insert pain point', description: 'Insert description' },
      { icon: <Grid size={16} />, title: 'Insert pain point', description: 'Insert description' }
    ],
    footnote: '1. xx',
    source: 'xx',
    pageNumber: '8'
  };

  const components = [
    { id: 'matrix2x2', name: 'Matrix 2x2', icon: <Grid size={16} /> },
    { id: 'dataviz', name: 'DataViz Split', icon: <BarChart3 size={16} /> },
    { id: 'process', name: 'Process Flow', icon: <GitBranch size={16} /> },
    { id: 'journey', name: 'Journey Map', icon: <Map size={16} /> }
  ];

  const renderComponent = () => {
    switch (activeComponent) {
      case 'matrix2x2':
        return <Matrix2x2Component data={matrix2x2Data} />;
      case 'dataviz':
        return <DataVizSplitComponent data={dataVizSplitData} />;
      case 'process':
        return <ProcessFlowComponent data={processFlowData} />;
      case 'journey':
        return <JourneyMapComponent data={journeyMapData} />;
      default:
        return <Matrix2x2Component data={matrix2x2Data} />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navigation */}
      <div className="bg-white border-b border-gray-200 p-4">
        <div className="flex space-x-4">
          {components.map((component) => (
            <button
              key={component.id}
              onClick={() => setActiveComponent(component.id)}
              className={`flex items-center space-x-2 px-4 py-2 rounded ${
                activeComponent === component.id
                  ? 'bg-blue-500 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              {component.icon}
              <span>{component.name}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Component Display */}
      <div className="relative">
        {renderComponent()}
      </div>
    </div>
  );
};

export default ConsultingSlides;