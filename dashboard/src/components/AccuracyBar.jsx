import React from 'react'
import { Bar } from 'react-chartjs-2'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

export default function AccuracyBar({ fuzzy, baseline }) {
  const data = {
    labels: ['System Accuracy'],
    datasets: [
      {
        label: 'Fuzzy System',
        data: [fuzzy],
        backgroundColor: 'rgba(99, 102, 241, 0.8)', // Indigo
        borderColor: '#4f46e5',
        borderWidth: 1,
        borderRadius: 8,
      },
      {
        label: 'Crisp Baseline',
        data: [baseline],
        backgroundColor: 'rgba(236, 72, 153, 0.8)', // Pink
        borderColor: '#db2777',
        borderWidth: 1,
        borderRadius: 8,
      },
    ],
  }

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        beginAtZero: true,
        max: 1.0,
        grid: { color: '#f3f4f6' }
      },
      x: {
        grid: { display: false }
      }
    },
    plugins: {
      legend: { position: 'bottom' }
    }
  }

  return <div style={{ height: '250px', width: '100%' }}><Bar data={data} options={options} /></div>
}