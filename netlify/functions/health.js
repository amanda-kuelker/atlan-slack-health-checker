exports.handler = async (event, context) => {
  // Simple demo canvas assessment
  const demoCanvas = `🏗️ DPR Construction - Data Governance Assessment

Prepared by Atlan Professional Services | November 18, 2025

🔴 Governance Health Score: 23/100 - Project Risk

📊 Current State Analysis

Assessment based on 150 key datasets across project management, financials, and operations
Construction & Engineering Data Governance Metrics:

* 📝 Project Management Documentation: 12.0% (18/150 datasets documented)
* 👥 Data Ownership: 8.0% (12 datasets with clear owners)
* ✅ Data Certification: 6.0% (9 datasets verified for accuracy)
* 🏗️ Business Context: 4.0% (6 datasets linked to business processes)

Platform Overview:

* Active Data Sources: 2+ systems (ERP, Project Management, Safety, Finance)
* Priority Focus: Construction & Engineering systems
* Compliance Readiness: Requires immediate attention

🎯 Strategic Recommendations for DPR Construction

1. 🚨 Project Management Data Discovery Crisis (CRITICAL Priority)
At 12.0% documentation, teams waste hours searching for the right data across systems.
Business Impact: Operational delays, missed opportunities, resource inefficiency
Action Plan:

* Document your top 10 critical construction datasets
* Create standard templates for data documentation
* Train teams on data discovery workflows
* Implement automated documentation for new data sources

Expected ROI: $200K+ annual savings in operational efficiency

2. ⚡ Data Accountability Gap (HIGH Priority)
With 8.0% ownership, when data issues occur, there's no clear escalation path - causing delays.
Business Impact: Process bottlenecks, quality issues, stakeholder dissatisfaction
Action Plan:

* Assign data owners to each critical business area
* Create data steward roles for high-impact processes
* Establish data quality SLAs for key metrics
* Implement regular data health monitoring

Expected ROI: 25% faster issue resolution, improved confidence

3. ⚠️ Data Trust & Compliance (MEDIUM Priority)
Only 6.0% certified data means teams don't know which information is reliable for decisions and compliance.
Business Impact: Regulatory risk, decision uncertainty, audit complications
Action Plan:

* Certify critical construction data sources
* Implement data quality validation workflows
* Create reliability standards for key processes
* Establish monthly certification reviews

Expected ROI: Reduced compliance risk, improved decision confidence

📈 30-60-90 Day Construction & Engineering Roadmap

30 Days: Foundation Building
* Document all critical construction datasets
* Assign data owners to high-priority areas
* Establish data quality standards
* Target Health Score: 43/100

60 Days: Process Optimization
* Implement automated governance workflows
* Train teams on data best practices
* Create business-facing dashboards
* Target Health Score: 58/100

90 Days: Competitive Advantage
* Achieve industry-leading governance maturity
* Demonstrate measurable ROI to leadership
* Scale patterns across all areas
* Target Health Score: 73/100

💰 Business Impact for DPR Construction

Current State Costs:
* Project managers spend 2-3 hours daily finding reliable data
* Data quality issues delay project starts by average 3 days
* Manual data validation costs ~$150K annually

Target State Benefits:
* 75% reduction in data discovery time
* 50% fewer project delays due to data issues
* $500K+ annual efficiency gains across project portfolio

🚀 Immediate Next Steps

Week 1:
* Leadership alignment on data governance priority
* Identify 5-10 most critical construction processes for pilot
* Assign dedicated data stewards to pilot areas

Week 2:
* Document pilot process datasets
* Implement data owner accountability framework
* Create quality standards for key deliverables

This Quarter:
* Scale governance practices across all critical processes
* Measure and report ROI to executive leadership
* Establish DPR Construction as construction data governance leader

Next Assessment: Schedule quarterly health checks to track progress and optimize data governance ROI.
Ready to unlock your data's potential? Let's start with your highest-impact processes first.`;

  return {
    statusCode: 200,
    headers: {
      'Content-Type': 'text/plain',
    },
    body: demoCanvas
  };
};
