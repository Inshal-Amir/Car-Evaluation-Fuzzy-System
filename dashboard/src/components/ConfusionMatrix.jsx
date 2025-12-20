import React from 'react'

export default function ConfusionMatrix({ matrix }) {
  const labels = ["unacc", "acc", "good", "vgood"]

  return (
    <div style={{ overflowX: 'auto' }}>
        <table style={{ borderCollapse: 'separate', borderSpacing: '4px', width: '100%', fontSize: '0.9rem' }}>
        <thead>
            <tr>
            <th style={{ padding: '8px', color: '#9ca3af', fontWeight: '500' }}>Actual \ Pred</th>
            {labels.map(l => <th key={l} style={{ padding: '8px', color: '#4b5563' }}>{l}</th>)}
            </tr>
        </thead>
        <tbody>
            {matrix.map((row, i) => (
            <tr key={i}>
                <th style={{ textAlign: 'right', paddingRight: '10px', color: '#4b5563' }}>{labels[i]}</th>
                {row.map((cell, j) => {
                    // Calculate intensity for coloring
                    const maxVal = Math.max(...row);
                    const intensity = cell > 0 ? (cell / 200) : 0; 
                    // Note: simplified intensity logic, assuming roughly balanced classes or max ~400
                    
                    return (
                        <td key={j} style={{
                            padding: '12px',
                            textAlign: 'center',
                            borderRadius: '6px',
                            backgroundColor: i === j 
                                ? `rgba(16, 185, 129, ${0.1 + (cell > 0 ? 0.8 : 0)})` // Green for correct
                                : `rgba(239, 68, 68, ${cell > 0 ? 0.1 + (cell/100) : 0.05})`, // Red tint for errors
                            color: i === j && cell > 0 ? '#065f46' : '#1f2937',
                            fontWeight: cell > 0 ? 'bold' : 'normal'
                        }}>
                        {cell}
                        </td>
                    )
                })}
            </tr>
            ))}
        </tbody>
        </table>
    </div>
  )
}