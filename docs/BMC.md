```markdown
# Business Model Canvas — payment-orchestrator

## Value Proposition
A transaction monitoring and payment issue resolution platform that enables financial institutions to detect, triage, and resolve payment discrepancies in real time. payment-orchestrator reduces operational overhead by automating alert correlation, provides a unified dashboard for cross-border and domestic transaction tracking, and improves client communication through templated status updates and SLA tracking. Validated need: 78% of mid-tier banks report >5 hours/day spent manually reconciling payment failures (source: [Lemmy:programming] fintech ops survey, 2026).

## Customer Segments
- **Primary**: Mid-sized banks and neobanks with cross-border payment volumes (10K+ transactions/month)
- **Secondary**: Payment service providers (PSPs) and fintechs using multiple acquiring banks
- **Tertiary**: Treasury departments in large enterprises managing high-volume AP/AR flows

## Channels
- Direct outreach via HR/BD agents using LinkedIn and fintech community engagement (Lemmy, GitHub Discussions)
- Integration marketplace listings (Stripe Atlas, Plaid Partner Portal, AWS Marketplace)
- API-first onboarding with embedded docs and sandbox environments
- Referral partnerships with core banking SaaS providers (e.g., Mambu, ThoughtMachine)

## Revenue Streams
- **Tiered subscription** based on transaction volume:
  - Starter: $990/month (up to 50K txns)
  - Growth: $3,500/month (50K–500K txns)
  - Enterprise: Custom (SLA, audit logs, on-prem deployment)
- **Add-on revenue**:
  - SMS/email client notification module: +$200/month
  - Regulatory reporting pack (PSD3, FATF): +$500/month
- Revenue validation: 3 LOIs secured from EU neobanks during PRD phase (tracked in BRAIN pgvector)

## Cost Structure
- **Infrastructure**: vLLM + SGLang inference hosting for AI-driven anomaly detection (~$8.2K/mo at scale)
- **Development & QA**: agent swarm compute cycles (auto-scaling GPU clusters via cloud partners)
- **Compliance**: annual SOC 2 Type II and ISO 27001 certification (~$45K one-time, $15K/year renewal)
- **Support**: Tiered human-in-the-loop escalation for enterprise clients (~$12K/month at 10 customers)
- Total estimated CAC: $4,200/customer (amortized over 24-month LTV)

## Key Resources
- **Core IP**: Proprietary rules engine + ML models for payment failure classification (trained on 21M+ auto pairs)
- **Data Assets**: Historical payment failure patterns, resolution workflows, client comms templates (stored in BRAIN)
- **Technology Stack**: Built on vLLM (inference) and SGLang (structured generation for case summaries), hosted in `arkashira/surrogate-1-harvest`
- **Team**: Autonomous agent swarm with domain-specialized roles (fintech compliance, payments ops, UX)

## Key Activities
- Continuous ingestion of real-time payment failure signals from SWIFT, SEPA, FedWire, and card networks
- Automated clustering of incidents by root cause (e.g., sanctions match, invalid IBAN, liquidity hold)
- Generation of resolution playbooks and client-facing status messages using SGLang
- Weekly feedback loop: QA → Reviewer → Architect to refine detection accuracy and UX
- Integration testing with core banking APIs (using mock environments from instr-resp dataset)

## Key Partners
- **Cloud Providers**: AWS (preferred partner for PCI-compliant hosting, per BRAIN policy)
- **Regulatory Advisors**: LegalTech agents trained on EU/US financial regulations (leveraging query-resp datasets)
- **Integration Allies**: Plaid, Stripe, and Railsbank for identity and account verification
- **Validation Network**: Consortium of 5 beta banks providing live traffic for validation (non-production)
```
