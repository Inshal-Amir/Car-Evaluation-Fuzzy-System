import React from 'react'
import { Line } from 'react-chartjs-2'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, Filler } from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, Filler)

export default function MembershipChart({ variableName, data }) {
  if (!data || data.length === 0) return null

  const labels = data[0].x.map(v => v.toFixed(2))

  // Custom colors for terms
  const colors = [
    { border: '#6366f1', bg: 'rgba(99, 102, 241, 0.2)' },
    { border: '#ec4899', bg: 'rgba(236, 72, 153, 0.2)' },
    { border: '#10b981', bg: 'rgba(16, 185, 129, 0.2)' },
    { border: '#f59e0b', bg: 'rgba(245, 158, 11, 0.2)' },
  ]

  const datasets = data.map((d, i) => ({
    label: d.term,
    data: d.y,
    borderColor: colors[i % colors.length].border,
    backgroundColor: colors[i % colors.length].bg,
    borderWidth: 2,
    fill: true,
    tension: 0.1,
    pointRadius: 0,
    pointHoverRadius: 4
  }))

  const chartData = { labels, datasets }

  const options = {
    responsive: true,
    interaction: {
        mode: 'index',
        intersect: false,
    },
    plugins: {
      legend: { position: 'top', labels: { usePointStyle: true, boxWidth: 8 } },
      title: { display: false },
      tooltip: {
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        titleColor: '#1f2937',
        bodyColor: '#1f2937',
        borderColor: '#e5e7eb',
        borderWidth: 1
      }
    },
    scales: {
      x: {
        ticks: { maxTicksLimit: 8, color: '#9ca3af' },
        grid: { display: false }
      },
      y: {
        min: 0,
        max: 1.1,
        ticks: { display: false }, // Hide Y axis numbers for cleaner look
        grid: { display: false }
      }
    }
  }

  return <Line data={chartData} options={options} />
}