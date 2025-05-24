"use client"

import React, { useEffect, useState } from 'react';
import { Card } from '@/components/ui/Card';
import { ContractTypePieChart } from '@/components/visualization/ContractTypePieChart';
import { RiskCategoryBarChart } from '@/components/visualization/RiskCategoryBarChart';
import { RiskTimelineChart } from '@/components/visualization/RiskTimelineChart';

export default function AggregateAnalysisPage() {
  const [aggregate, setAggregate] = useState<any>(null);
  const [timeline, setTimeline] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      const aggRes = await fetch('/api/v1/analysis/aggregate').then(r => r.json());
      const timeRes = await fetch('/api/v1/analysis/timeline').then(r => r.json());
      setAggregate(aggRes);
      setTimeline(timeRes);
      setLoading(false);
    }
    fetchData();
  }, []);

  if (loading) return <div>Loading aggregate analysis...</div>;

  return (
    <div className="container mx-auto px-4 py-8 space-y-8">
      <h1 className="text-3xl font-bold text-gray-900">Aggregate Analysis</h1>
      <p className="text-gray-600 mb-4">Overview of contract types, risk categories, and risk scores over time.</p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <Card>
          <h2 className="text-xl font-semibold mb-4">Contract Type Distribution</h2>
          <ContractTypePieChart data={aggregate.contract_types} />
        </Card>
        <Card>
          <h2 className="text-xl font-semibold mb-4">Risk Category Distribution</h2>
          <RiskCategoryBarChart data={aggregate.risk_categories} />
        </Card>
      </div>
      <Card>
        <h2 className="text-xl font-semibold mb-4">Risk Score Timeline</h2>
        <RiskTimelineChart data={timeline.timeline} />
      </Card>
      <div className="text-xs text-gray-400 mt-4">
        {aggregate.disclaimer}<br />
        {timeline.disclaimer}
      </div>
    </div>
  );
} 