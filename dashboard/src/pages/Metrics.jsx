import React, { useEffect, useState } from 'react'
import { getMetrics, getMembership } from '../api/client'
import ConfusionMatrix from '../components/ConfusionMatrix'
import AccuracyBar from '../components/AccuracyBar'
import MembershipChart from '../components/MembershipChart'
import '../App.css'

export default function Metrics() {
  const [data, setData] = useState(null)
  const [mem, setMem] = useState(null)

  useEffect(() => {
    getMetrics().then(setData)
    getMembership().then(setMem)
  }, [])

  if (!data || !mem) return <div style={{color: 'white', fontSize: '1.2rem'}}>Loading system analytics...</div>

  return (
    <div style={{ textAlign: 'left', maxWidth: '1200px', margin: '0 auto' }}>
      
      {/* Top Stats Row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '20px', marginBottom: '20px' }}>
        <div className="glass-card" style={{ padding: '1.5rem', textAlign: 'center', marginBottom: 0 }}>
            <div style={{ fontSize: '0.9rem', color: '#6b7280' }}>Total Instances</div>
            <div style={{ fontSize: '2rem', fontWeight: 'bold', color: 'var(--primary)' }}>{data.stats.instances}</div>
        </div>
        <div className="glass-card" style={{ padding: '1.5rem', textAlign: 'center', marginBottom: 0 }}>
            <div style={{ fontSize: '0.9rem', color: '#6b7280' }}>Input Features</div>
            <div style={{ fontSize: '2rem', fontWeight: 'bold', color: 'var(--secondary)' }}>{data.stats.features}</div>
        </div>
        <div className="glass-card" style={{ padding: '1.5rem', textAlign: 'center', marginBottom: 0 }}>
            <div style={{ fontSize: '0.9rem', color: '#6b7280' }}>Target Classes</div>
            <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#10b981' }}>{data.stats.target_classes.length}</div>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginBottom: '20px' }}>
        <div className="glass-card" style={{ marginBottom: 0 }}>
          <h3 style={{ marginTop: 0 }}>Model Accuracy</h3>
          <AccuracyBar fuzzy={data.evaluation.accuracy} baseline={data.evaluation.baseline_accuracy} />
        </div>
        <div className="glass-card" style={{ marginBottom: 0 }}>
          <h3 style={{ marginTop: 0 }}>Confusion Matrix</h3>
          <ConfusionMatrix matrix={data.evaluation.confusion_matrix} />
        </div>
      </div>

      <h2 style={{ color: 'white', marginTop: '40px', marginBottom: '20px', textShadow: '0 2px 4px rgba(0,0,0,0.2)' }}>
          Membership Functions
      </h2>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))', gap: '20px' }}>
        {Object.keys(mem).map(k => (
          <div key={k} className="glass-card" style={{ marginBottom: 0 }}>
            <h4 style={{ marginTop: 0, textTransform: 'capitalize', color: 'var(--primary)' }}>{k}</h4>
            <MembershipChart variableName={k} data={mem[k]} />
          </div>
        ))}
      </div>
    </div>
  )
}