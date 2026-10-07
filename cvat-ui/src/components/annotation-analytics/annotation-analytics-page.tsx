// Copyright (C) CVAT.ai Corporation
//
// SPDX-License-Identifier: MIT

import './styles.scss';

import React, { useCallback, useEffect, useState } from 'react';
import { useParams } from 'react-router';
import { Bar } from 'react-chartjs-2';
import {
    BarElement, CategoryScale, Chart as ChartJS, Legend, LinearScale, Tooltip,
} from 'chart.js';
import { Button } from 'antd';
import { Row, Col } from 'antd/lib/grid';
import Title from 'antd/lib/typography/Title';

import { getCore } from 'cvat-core-wrapper';
import GoBackButton from 'components/common/go-back-button';
import CVATLoadingSpinner from 'components/common/loading-spinner';

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

type AnnotationCounts = Record<string, number>;

const core = getCore();

function AnnotationAnalyticsPage(): JSX.Element {
    const taskID = +useParams<{ tid: string }>().tid;
    const [counts, setCounts] = useState<AnnotationCounts | null>(null);
    const [loading, setLoading] = useState(true);
    const [failed, setFailed] = useState(false);

    const loadCounts = useCallback(async (): Promise<void> => {
        setLoading(true);
        setFailed(false);
        try {
            const response = await core.server.request<{ data: AnnotationCounts }>(
                `/api/tasks/${taskID}/annotation-counts`,
                { method: 'GET' },
            );
            setCounts(response.data);
        } catch (_error: unknown) {
            setFailed(true);
        } finally {
            setLoading(false);
        }
    }, [taskID]);

    useEffect(() => {
        loadCounts();
    }, [loadCounts]);

    const chartData = counts ? Object.entries(counts).sort((a, b) => b[1] - a[1]) : [];

    return (
        <div className='cvat-annotation-analytics-page'>
            <Row justify='center'>
                <Col span={22} xl={18} xxl={14} className='cvat-task-top-bar'>
                    <GoBackButton />
                </Col>
            </Row>
            <Row justify='center'>
                <Col span={22} xl={18} xxl={14}>
                    <Title level={3} className='cvat-text-color'>Annotation Analytics</Title>
                    {loading && <CVATLoadingSpinner />}
                    {!loading && failed && (
                        <div className='cvat-annotation-analytics-message'>
                            <p>Unable to load annotation analytics.</p>
                            <Button type='primary' onClick={loadCounts}>Try again</Button>
                        </div>
                    )}
                    {!loading && !failed && chartData.length === 0 && (
                        <p className='cvat-annotation-analytics-message'>
                            No annotation data available for this task.
                        </p>
                    )}
                    {!loading && !failed && chartData.length > 0 && (
                        <div className='cvat-annotation-analytics-chart'>
                            <Bar
                                data={{
                                    labels: chartData.map(([className]) => className),
                                    datasets: [{
                                        label: 'Annotations',
                                        data: chartData.map(([, count]) => count),
                                        backgroundColor: '#1890ff',
                                        borderRadius: 4,
                                    }],
                                }}
                                options={{
                                    indexAxis: 'y',
                                    responsive: true,
                                    maintainAspectRatio: false,
                                    plugins: {
                                        legend: { display: false },
                                        tooltip: {
                                            callbacks: {
                                                label: (context) => ` ${context.parsed.x.toLocaleString()}`,
                                            },
                                        },
                                    },
                                    scales: {
                                        x: { beginAtZero: true, ticks: { precision: 0 } },
                                    },
                                }}
                                aria-label='Annotation counts by class'
                            />
                            <div className='cvat-annotation-analytics-counts' aria-label='Annotation counts'>
                                {chartData.map(([className, count]) => (
                                    <div className='cvat-annotation-analytics-count' key={className}>
                                        <span>{className}</span>
                                        <strong>{count.toLocaleString()}</strong>
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}
                </Col>
            </Row>
        </div>
    );
}

export default React.memo(AnnotationAnalyticsPage);
