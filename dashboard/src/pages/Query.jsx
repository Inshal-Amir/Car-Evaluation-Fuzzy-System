import React, { useState } from 'react'
import { predict } from '../api/client'
import '../App.css' // Ensure we have the styles

const OPTIONS = {
  buying: ["low", "med", "high", "vhigh"],
  maint: ["low", "med", "high", "vhigh"],
  doors: ["2", "3", "4", "5more"],
  persons: ["2", "4", "more"],
  lug_boot: ["small", "med", "big"],
  safety: ["low", "med", "high"]
}

export default function Query() {
  const [form, setForm] = useState({
    buying: 'med',
    maint: 'med',
    doors: '4',
    persons: '4',
    lug_boot: 'med',
    safety: 'med'
  })
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResult(null)
    try {
      const res = await predict(form)
      setResult(res)
    } catch (err) {
      setError("Failed to fetch prediction.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto' }}>
      <div className="glass-card">
        <h2 style={{ marginTop: 0, borderBottom: '2px solid #f3f4f6', paddingBottom: '1rem', marginBottom: '1.5rem' }}>
          Input Car Details
        </h2>
        <form onSubmit={handleSubmit}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
            {Object.keys(OPTIONS).map(key => (
              <div key={key} className="form-group">
                <label className="styled-label">{key.replace('_', ' ')}</label>
                <select 
                  name={key} 
                  value={form[key]} 
                  onChange={handleChange}
                  className="styled-select"
                >
                  {OPTIONS[key].map(opt => <option key={opt} value={opt}>{opt}</option>)}
                </select>
              </div>
            ))}
          </div>
          
          <div style={{ marginTop: '2rem' }}>
            <button type="submit" disabled={loading} className="primary-btn">
              {loading ? "Running Fuzzy Inference..." : "Evaluate Safety"}
            </button>
          </div>
        </form>
        {error && <p style={{ color: '#ef4444', fontWeight: 'bold', marginTop: '1rem' }}>{error}</p>}
      </div>

      {result && (
        <div className="glass-card" style={{ borderLeft: '6px solid var(--secondary)' }}>
          <h2 style={{ color: 'var(--secondary)', marginTop: 0 }}>
            Result: <span style={{ fontSize: '1.5em' }}>{result.predicted_class.toUpperCase()}</span>
          </h2>
          
          <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap', marginBottom: '20px' }}>
             <div style={{ flex: 1, background: '#f9fafb', padding: '15px', borderRadius: '10px' }}>
                <h4 style={{ margin: '0 0 10px 0' }}>Score (Crisp)</h4>
                <div style={{ fontSize: '1.2em', fontWeight: 'bold', color: '#4b5563' }}>
                    {result.crisp_output.toFixed(4)}
                </div>
             </div>
             <div style={{ flex: 1, background: '#f9fafb', padding: '15px', borderRadius: '10px' }}>
                <h4 style={{ margin: '0 0 10px 0' }}>Class Probabilities</h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                    {Object.entries(result.probs).map(([k, v]) => (
                    <div key={k} style={{ display: 'flex', alignItems: 'center', fontSize: '0.9em' }}>
                        <span style={{ width: '60px', fontWeight: '600' }}>{k}</span>
                        <div style={{ flex: 1, height: '8px', background: '#e5e7eb', borderRadius: '4px', margin: '0 10px', overflow: 'hidden' }}>
                            <div style={{ width: `${v * 100}%`, background: 'var(--primary)', height: '100%' }}></div>
                        </div>
                        <span>{(v * 100).toFixed(0)}%</span>
                    </div>
                    ))}
                </div>
             </div>
          </div>

          <div style={{ textAlign: 'left', background: '#f3f4f6', padding: '15px', borderRadius: '10px' }}>
            <h3 style={{ marginTop: 0, fontSize: '1rem' }}>Fired Rules (Top 5 Active)</h3>
            <ul style={{ margin: 0, paddingLeft: '20px', color: '#4b5563', fontSize: '0.9rem' }}>
              {result.fired_rules.map((r, i) => <li key={i} style={{ marginBottom: '4px' }}>{r}</li>)}
            </ul>
          </div>
        </div>
      )}
    </div>
  )
}