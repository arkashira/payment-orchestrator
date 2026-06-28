**breakeven.md**  
*Payment‑Orchestrator – Unit Economics & Break‑Even Analysis*  

---  

## 1. Cost per Active User (monthly)

| Cost Component | Assumptions (per active user) | Monthly Cost (USD) |
|----------------|------------------------------|--------------------|
| **Compute** (AWS Fargate / GKE Autopilot) | 0.2 vCPU × $0.040/hr + 0.5 GB RAM × $0.005/hr × 730 hrs ≈ $6.00 | **$6.00** |
| **Storage** (PostgreSQL RDS + S3) | 10 GB DB (standard) @ $0.115/GB + 5 GB logs @ $0.023/GB | **$1.30** |
| **Bandwidth** (Data in/out) | 50 GB/month outbound @ $0.09/GB (first 10 GB free) | **$3.60** |
| **Third‑party APIs** (e.g., SWIFT, ACH) | 1 k API calls @ $0.0015 each | **$1.50** |
| **Observability / Logging** (CloudWatch, Loki) | 5 GB logs @ $0.10/GB | **$0.50** |
| **Support overhead** (shared ticket queue) | 0.2 h support @ $30/h | **$6.00** |
| **Total Cost / Active User** |  | **$18.90** |

> *Rounded to the nearest cent. Costs are based on on‑demand pricing in US‑East (N. Virginia) and assume average usage patterns derived from similar payment‑monitoring SaaS workloads.*

---

## 2. Pricing Tiers (monthly)

| Tier | Price / mo | Included Features | Max Users per Tier (for analysis) |
|------|------------|-------------------|-----------------------------------|
| **Starter** | **$49** | • 5,000 transactions monitored<br>• Basic alerts (email)<br>• Dashboard + CSV export<br>• Email support (24 h) | 1 – 5 |
| **Growth** | **$149** | • 25,000 transactions<br>• Advanced alerts (SMS, webhook)<br>• AI‑driven anomaly detection<br>• Role‑based access<br>• Priority email support (12 h) | 6 – 20 |
| **Enterprise** | **$499** | • Unlimited transactions<br>• Real‑time monitoring & reconciliation<br>• Custom workflow automation<br>• Dedicated CSM & 24/7 phone support<br>• SLA 99.9 % uptime | 21 + |

*Assume average usage per paying seat ≈ 1 active user (i.e., each paying entity runs the platform for its own ops team).*

---

## 3. Customer Acquisition Cost (CAC)

| Source | Cost per Lead | Conversion Rate (Lead → Paying) | CAC (USD) |
|--------|---------------|--------------------------------|-----------|
| Paid LinkedIn ads | $120 | 4 % | $3,000 |
| Content/SEO (white‑paper) | $30 | 2 % | $1,500 |
| Partner referrals | $0 | 10 % | $0 |
| **Range (typical)** | — | — | **$0 – $3,000** |

*We target a CAC ≈ $1,200 by mixing paid ads (30 %) and organic/partner channels (70 %).*

---

## 4. Lifetime Value (LTV)

| Parameter | Assumption |
|-----------|------------|
| Average Monthly Revenue per Customer (ARPU) | $149 (Growth tier weighted) |
| Gross Margin (1 – Cost/Revenue) | 65 % (Revenue – $18.90 cost) |
| Average Customer Lifetime | 24 months (2 yr churn ≈ 4 %/mo) |
| **LTV** | **$149 × 0.65 × 24 ≈ $2,322** |

*Even at the Starter tier (ARPU $49) LTV ≈ $720, still > CAC for organic channels.*

---

## 5. Break‑Even Users Count

Break‑even occurs when **Total Monthly Revenue ≥ Total Monthly Cost**.

Let **N** = number of paying customers (average mix: 60 % Growth, 30 % Starter, 10 % Enterprise).  
Weighted average price:

\[
\text{Avg Price} = 0.6×149 + 0.3×49 + 0.1×499 = \$139.4
\]

Monthly cost per user = $18.90.

\[
\text{Break‑even N} = \frac{\text{CAC (amortized over 24 mo) } + \text{Monthly Fixed Ops (≈ $5,000)}}{\text{Avg Price} - \text{Cost per User}}
\]

*Assume $5,000 fixed ops (engineer salaries, infra overhead). CAC amortized per month = $1,200 / 24 ≈ $50.*

\[
\text{Break‑even N} = \frac{5,000 + 50}{139.4 - 18.9} ≈ \frac{5,050}{120.5} ≈ **42 customers**
\]

So **≈ 42 paying accounts** (mix as above) yields profitability.

---

## 6. Path to $10 K MRR

| Target MRR | Required Revenue Mix | Approx. # Customers |
|------------|----------------------|----------------------|
| $10,000 | 70 % Growth, 20 % Starter, 10 % Enterprise | 6 × Growth ($149) = $894<br>2 × Starter ($49) = $98<br>1 × Enterprise ($499) = $499 → **$1,491** (insufficient) |
| **Actual** | Use pure Growth tier for simplicity | $10,000 ÷ $149 ≈ **67 Growth customers** |

**Practical roadmap**  

| Month | Tier Mix | # Customers | MRR |
|-------|----------|-------------|-----|
| 1‑2 | Pilot (Enterprise 1) + Starter 3 | 4 | $645 |
| 3‑4 | Add Growth 5 | 9 | $1,341 |
| 5‑6 | Growth 15 | 24 | $3,576 |
| 7‑9 | Growth 30 + Starter 5 | 35 | $5,815 |
| 10‑12 | Growth 45 + Enterprise 2 + Starter 5 | 52 | $8,743 |
| 13‑15 | Growth 60 + Enterprise 3 + Starter 7 | 70 | $11,530 → **> $10K MRR** |

*At month 13 we cross the $10 K MRR threshold, already above the 42‑customer break‑even point, delivering net profit.*

---  

### Quick Takeaways
- **Unit cost** per active user ≈ **$19/mo** → high margin at our pricing.
- **CAC** can be kept <$1,500 with a strong content/partner mix.
- **LTV** (~$2.3 k) comfortably exceeds CAC, supporting sustainable growth.
- **Break‑even** ~ **42 paying accounts** (mixed tiers).  
- **$10 K MRR** achievable with **≈ 70 Growth‑tier customers** or an equivalent mix, reachable within ~12‑15 months under a realistic sales ramp.  