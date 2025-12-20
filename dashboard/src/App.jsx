import { useState } from 'react'
import './App.css'
import Query from './pages/Query'
import Metrics from './pages/Metrics'

function App() {
  const [page, setPage] = useState('query')

  return (
    <div className="app-container">
      <div style={{ marginBottom: '40px' }}>
        <h1 style={{ color: 'white', marginBottom: '0.5rem', textShadow: '0 2px 4px rgba(0,0,0,0.2)' }}>
          Car Safety Evaluator
        </h1>
        <p style={{ color: 'rgba(255,255,255,0.8)' }}>Fuzzy Logic Powered Assessment System</p>
      </div>

      <nav className="nav-container">
        <button 
          className={`nav-btn ${page === 'query' ? 'active' : ''}`} 
          onClick={() => setPage('query')}
        >
          Predict Safety
        </button>
        <button 
          className={`nav-btn ${page === 'metrics' ? 'active' : ''}`} 
          onClick={() => setPage('metrics')}
        >
          System Metrics
        </button>
      </nav>

      <div className="content-fade-in">
        {page === 'query' ? <Query /> : <Metrics />}
      </div>
    </div>
  )
}

export default App