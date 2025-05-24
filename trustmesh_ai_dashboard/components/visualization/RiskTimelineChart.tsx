import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from 'recharts';

interface RiskTimelineChartProps {
  data: Array<{ date: string; riskScore: number }>;
}

export function RiskTimelineChart({ data }: RiskTimelineChartProps) {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis domain={[0, 100]} />
        <Tooltip />
        <Line type="monotone" dataKey="riskScore" stroke="#8884d8" strokeWidth={2} dot={true} />
      </LineChart>
    </ResponsiveContainer>
  );
} 