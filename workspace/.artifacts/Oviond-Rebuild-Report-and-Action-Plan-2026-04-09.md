# Oviond Rebuild Report and Action Plan
## Based on Gleap historical support analysis

Prepared for: Chris Irwin  
Prepared by: Nicole Prince  
Date: 9 April 2026

---

## Executive summary

This report is based on a careful analysis of Oviond's historical Gleap data, including the full readable ticket history and a higher-signal subset used to reduce email and bot noise.

The core conclusion is simple: the rebuild should be driven less by shiny net-new features and more by trust, operability, and delivery reliability.

Gleap shows that Oviond's biggest recurring problems are not primarily demand-generation problems. They are product confidence problems. Customers repeatedly hit friction around connectors and data trust, permissions and access, builder reliability, custom domains and white-label delivery, automations, exports, billing state, and workflow operability.

If the rebuilt product makes those areas solid, Oviond becomes dramatically more credible and sticky for agencies. If not, the rebuild risks recreating the same support load in a prettier shell.

---

## Evidence base

This report draws on the following Gleap research already completed:

- Total tickets analysed: 10,844
- Non-BOT tickets: 9,334
- BOT tickets: 1,510
- Historical range reviewed: 3 May 2024 to 9 April 2026
- Filtered product-signal set: 6,157 tickets
- High-signal subset used for priority shaping: 3,854 tickets

### Dominant product themes in the higher-signal analysis

- Permissions, login, and user management: 1,901
- Connectors and data quality: 1,800
- Report builder, widgets, and editing: 1,520
- Performance and reliability: 1,218
- Custom domain and white-label: 1,054
- Billing and subscription: 980
- Automation and notifications: 555
- Report sharing, exports, and scheduling: 275
- API, webhooks, and extensibility: 267
- Onboarding and migration: 263

### Additional signals from help-search behaviour

Help-centre and support search behaviour reinforced the same themes. High-frequency searches included custom domain, API, Google Ads, integrations, white label, Google Business Profile, Google Search Console, Google Sheets, templates, delete actions, automations, and cover-page/report editing questions.

### Important interpretation

Gleap does not behave like a pure bug tracker. It behaves like a combined system for:

- product bugs
- customer-success handholding
- setup and implementation support
- white-label and report-delivery operations
- billing and account exceptions
- noisy inbound email traffic

That matters because it means the rebuild should optimise for real agency operations, not just feature completeness.

---

## Strategic diagnosis

### What Gleap is really telling us

1. **Oviond wins when it feels simple and dependable.**
2. **Oviond loses when users cannot trust the data, the delivery, or the permissions model.**
3. **White-label reliability is a core product requirement, not a side feature.**
4. **Builder inconsistency creates disproportionate support pain because it breaks confidence.**
5. **The rebuild should prioritise operational trust before expansion.**

### The rebuild principle

The rebuilt Oviond should be designed around four promises:

- Your data connects reliably.
- Your report renders consistently everywhere.
- Your clients see the right thing.
- Your branded delivery just works.

---

# Top 20 rebuild priorities

## 1. Rebuild connector reliability as core infrastructure
**Why this matters**  
This is one of the biggest recurring sources of friction in Gleap. Repeated issues show up across GA4, Google Ads, Meta, Google Business Profile, WooCommerce, Shopify, HubSpot, Microsoft Ads, Google Sheets, Ahrefs, and token-expiry scenarios. If connectors are unstable, the whole product feels unsafe.

**What the rebuild should do**
- Create a single connection service with connector-specific adapters.
- Standardise OAuth, token refresh, scope checks, and account discovery.
- Add proactive expiry detection and reconnect prompts.
- Add connector health states: connected, degraded, expired, permission error, upstream outage.
- Expose last successful sync and last failed sync clearly.
- Standardise connector error codes and user-readable diagnostics.

**Dev checklist**
- Define connector lifecycle contract.
- Add preflight validation before save.
- Add retry and backoff policies.
- Add sync health logging and alerting.
- Build regression tests for top 10 connectors.
- Add provider deprecation monitoring.

---

## 2. Use one rendering and data-resolution engine across editor, shared view, PDF, and automations
**Why this matters**  
A repeated pattern in Gleap is that something works in the editor but fails in shared reports, exports, PDFs, or scheduled sends. That destroys trust fast.

**What the rebuild should do**
- Unify report execution across all delivery surfaces.
- Make date-range resolution, filters, permissions, and query execution identical everywhere.
- Build parity testing across editor, shared, PDF, and automation outputs.
- Show when an output differs from source state.

**Dev checklist**
- Remove parallel rendering code paths.
- Create one report execution contract.
- Add snapshot parity tests.
- Normalize timezone handling centrally.
- Add render logs for scheduled runs.
- Add a preview for next scheduled output.

---

## 3. Rewrite auth, permissions, team access, and client sharing
**Why this matters**  
Permissions, login loops, account access issues, and broken team-assignment flows show up constantly. Agencies need confident control over who can see, edit, and deliver what.

**What the rebuild should do**
- Design clean role-based access control.
- Support scopes across workspace, client, project, report, and automation.
- Make invite, revoke, transfer, and role changes predictable.
- Add auditability for access changes.

**Dev checklist**
- Define role and scope matrix.
- Build permission simulator.
- Add invite and revoke audit logs.
- Add shared-report access tests.
- Add migration tooling from current permission models.
- Test edge cases for team and client assignments.

---

## 4. Make custom domains, white-label, and branded delivery fully self-serve
**Why this matters**  
Custom domains, email-domain verification, white-label setup, and domain failures are a major recurring support burden. This is not edge-case admin work. It is a core agency use case.

**What the rebuild should do**
- Let users set up custom domains themselves.
- Validate DNS and SSL status live.
- Support branded sending domains and sender verification.
- Detect broken domain configurations before customer-facing failures happen.

**Dev checklist**
- Build custom-domain setup wizard.
- Add DNS verification and SSL status checks.
- Add sender-domain verification flow.
- Add health monitoring and expiry warnings.
- Add rollback and recovery flows.
- Remove manual ops dependency from the common path.

---

## 5. Rebuild the query, filter, and calculated-metric engine
**Why this matters**  
Recurring tickets point to brittleness in filters, calculated metrics, connector-specific field behaviour, and query-builder consistency. When the reporting core is hard to trust, users feel the whole platform is fragile.

**What the rebuild should do**
- Introduce typed fields and operator rules.
- Add formula validation with clear error messages.
- Support cross-source calculations explicitly where valid.
- Detect incomplete or invalid filters before execution.

**Dev checklist**
- Build typed schema layer for dimensions and metrics.
- Build formula parser and validator.
- Add query preview and sample-row inspection.
- Add filter linting and save-time warnings.
- Build regression fixtures for known calculation bugs.
- Standardise connector-specific field mapping.

---

## 6. Add visible data health and diagnostics at widget, query, and report level
**Why this matters**  
A lot of Gleap tickets exist because users cannot tell whether a problem is caused by stale data, broken auth, filters, permissions, or upstream provider issues.

**What the rebuild should do**
- Show freshness, sync time, and health state at widget and report level.
- Explain why a widget is empty.
- Expose source account, last sync, and failure reason.
- Give support and users a shared diagnostic view.

**Dev checklist**
- Add freshness badges.
- Add widget-level empty-state diagnostics.
- Add data-source status drawers.
- Add exportable support diagnostics bundle.
- Add provider-incident banner support.
- Add editor versus shared comparison diagnostics.

---

## 7. Fix builder persistence, save integrity, and editing state management
**Why this matters**  
Tickets about settings not saving, sorting not sticking, and edits behaving unpredictably indicate state-management weakness. That makes the builder feel unreliable even when the underlying data is fine.

**What the rebuild should do**
- Make saves durable and visible.
- Protect against silent state drift.
- Support undo and conflict handling.
- Preserve editing confidence.

**Dev checklist**
- Rework save architecture.
- Add autosave and explicit save confirmation.
- Add undo and redo.
- Add unsaved-change warnings.
- Add conflict handling for concurrent edits.
- Add change history for key objects.

---

## 8. Make performance and async-job reliability a product requirement
**Why this matters**  
Refresh issues, PDF generation failures, stuck states, ghost records, and inconsistent background processing point to job-system fragility. Reliability needs to be designed, not hoped for.

**What the rebuild should do**
- Harden queues, workers, cache invalidation, and job retries.
- Make job status visible.
- Ensure deletion, rendering, syncing, and export jobs are idempotent.

**Dev checklist**
- Instrument worker and queue health.
- Define timeout and retry rules.
- Add job status UI for long-running operations.
- Add canary jobs and monitoring.
- Add stale-cache invalidation rules.
- Test against large real-world report fixtures.

---

## 9. Rebuild onboarding around first trusted live report
**Why this matters**  
A meaningful portion of Gleap friction is activation friction. Users often struggle with connecting sources, understanding what is live versus demo, and getting to a clean first output.

**What the rebuild should do**
- Guide users to a first useful, trusted report.
- Make demo versus live state obvious.
- Reduce ambiguity in setup.

**Dev checklist**
- Build guided onboarding by use case.
- Add clear live-data indicators.
- Add first-report progress checklist.
- Detect stalled onboarding states.
- Improve template import behaviour.
- Instrument onboarding drop-off points.

---

## 10. Rebuild automations as an observable delivery system
**Why this matters**  
Scheduled delivery failures are especially damaging because the customer often discovers them after a client-facing mistake. Gleap includes blank automated reports, date mismatch issues, and fragile scheduled outputs.

**What the rebuild should do**
- Make automations debuggable and previewable.
- Make date logic explicit.
- Show run history and delivery state.

**Dev checklist**
- Add test-send before activation.
- Add full run history.
- Add recipient-level delivery status.
- Add explicit timezone and date-range controls.
- Add automation version history.
- Alert owners on repeated failure or degradation.

---

## 11. Harden exports, PDFs, email delivery, and share links
**Why this matters**  
PDF failures, non-clickable links, layout issues, and export inconsistencies directly damage the client experience. This is the last mile of value delivery.

**What the rebuild should do**
- Treat export and send surfaces as production-critical.
- Validate links and layouts before delivery.
- Store enough diagnostics to debug failures quickly.

**Dev checklist**
- Build export regression suite.
- Validate share links before send.
- Improve page-break and overflow rules.
- Add branded preview for email and PDF output.
- Add fallback or retry path for failed exports.
- Preserve failed-output diagnostics.

---

## 12. Build proper delete, archive, restore, and cleanup flows
**Why this matters**  
Tickets like deleted projects still appearing or clients not deleting show that system state is not always trustworthy. That creates fear around core actions.

**What the rebuild should do**
- Separate archive from hard delete.
- Make destructive actions reversible for a safe window.
- Clean up dependent objects correctly.

**Dev checklist**
- Add soft-delete and restore.
- Define cascade rules.
- Add cleanup jobs for stale references.
- Add admin recovery tooling.
- Add destructive-action summaries.
- Add tests for ghost-state prevention.

---

## 13. Make entitlements, limits, billing state, upgrades, and reactivation obvious
**Why this matters**  
Gleap repeatedly shows confusion and failure around plan limits, project and report caps, upgrade flows, payment-state ambiguity, and reactivation.

**What the rebuild should do**
- Centralise entitlement logic.
- Make blockers transparent.
- Align upgrade prompts with actual restrictions.

**Dev checklist**
- Create central entitlement service.
- Show usage meters and exact limits.
- Improve upgrade and reactivation flows.
- Surface payment failure states clearly.
- Add account-level billing event log.
- Add safe support override tooling.

---

## 14. Add bulk agency workflows
**Why this matters**  
Agencies need repeatability. If common multi-client tasks stay manual, support and success teams absorb the pain.

**What the rebuild should do**
- Support bulk rollout and bulk admin workflows.
- Make multi-client operations efficient and safe.

**Dev checklist**
- Add clone-to-multiple-clients.
- Add bulk user and role assignment.
- Add bulk data-source remapping where possible.
- Add template version propagation.
- Add rollout preview and dry-run mode.
- Add exception reporting after bulk actions.

---

## 15. Close the highest-frequency connector and metric gaps systematically
**Why this matters**  
Gleap repeatedly points to missing or unreliable coverage around custom conversions, conversion actions, GBP search terms, Microsoft Ads auth, WooCommerce, Shopify, HubSpot, Local Service Ads, and other connector-level gaps.

**What the rebuild should do**
- Treat connector completeness as a prioritised product program.
- Rank gaps by support volume, retention risk, and agency value.

**Dev checklist**
- Create live connector gap board.
- Assign owner per priority connector.
- Add contract tests against provider APIs.
- Document metric availability and known constraints.
- Review gap board monthly using Gleap plus product usage.
- Add release gates for connector regressions.

---

## 16. Build a migration and compatibility layer from old Oviond into rebuilt Oviond
**Why this matters**  
Without a thoughtful migration layer, the rebuild could generate a new wave of support pain. Existing customers need continuity, not disruption.

**What the rebuild should do**
- Migrate users, clients, projects, reports, templates, automations, and permissions safely.
- Detect unsupported legacy configurations before cutover.

**Dev checklist**
- Define migratable object map.
- Add legacy-to-new feature mapping.
- Flag unsupported features pre-migration.
- Add parity validation after migration.
- Add rollback and staged cutover support.
- Pilot on a controlled set of real accounts first.

---

## 17. Productise API, webhooks, and MCP properly
**Why this matters**  
This is not the largest volume theme, but it is high leverage for more advanced customers and partners. Recent Gleap tickets already show MCP and API-side pain.

**What the rebuild should do**
- Provide a stable extensibility model.
- Make external integrations diagnosable and safe.

**Dev checklist**
- Add scoped API keys.
- Add webhook logs, retry, and replay.
- Add MCP setup diagnostics and health checks.
- Publish stable schemas and error contracts.
- Add rate limits with useful errors.
- Version the API intentionally.

---

## 18. Separate AI from core reporting reliability, and make BYOK work cleanly
**Why this matters**  
AI entitlement confusion is showing up in Gleap. AI can be valuable, but it should never undermine trust in the reporting core.

**What the rebuild should do**
- Separate AI access from core reporting entitlements.
- Make bring-your-own-key behaviour explicit and testable.
- Ensure AI failure does not contaminate report rendering.

**Dev checklist**
- Separate AI billing and entitlement logic.
- Add provider status and usage visibility.
- Add graceful degradation when AI is unavailable.
- Add BYOK end-to-end tests.
- Prevent AI path failures from affecting core reporting flows.

---

## 19. Put contextual help and guided troubleshooting inside the product
**Why this matters**  
Search behaviour shows users repeatedly looking for help on the same issues. That means the product is making them leave the workflow too often.

**What the rebuild should do**
- Add contextual guidance at the point of friction.
- Use real user language drawn from support history.

**Dev checklist**
- Add page-level help drawer.
- Add connector troubleshooting wizards.
- Link error codes directly to support articles.
- Add in-flow setup walkthroughs for top tasks.
- Improve search relevance using Gleap phrasing.
- Add next-step guidance from empty and error states.

---

## 20. Instrument the rebuilt app so Gleap becomes a feedback loop, not just a fire alarm
**Why this matters**  
Right now many issues are only obvious after the customer hits them. The rebuilt product should emit enough context to detect and diagnose friction early.

**What the rebuild should do**
- Make support and product telemetry work together.
- Feed product prioritisation from real operational signals.

**Dev checklist**
- Emit structured events for key product flows.
- Attach product context automatically to support tickets.
- Auto-tag tickets by area and severity where possible.
- Build weekly product-friction dashboards.
- Track funnel drop-off by connector and setup step.
- Review Gleap plus telemetry in weekly product ops.

---

# Recommended delivery sequence

## Phase 1: Beta blockers
These should be treated as non-negotiable before broad rebuild rollout.

1. Connector reliability
2. Unified rendering engine
3. Permissions and sharing
4. Custom domain and white-label self-serve
5. Query and calculated metric engine
6. Data health diagnostics
7. Builder save integrity
8. Performance and async-job reliability

## Phase 2: Must-have before general availability

9. Onboarding to first trusted live report
10. Observable automations
11. Exports, PDFs, and share delivery
12. Delete, archive, and restore
13. Entitlements and billing clarity
14. Bulk agency workflows
15. Connector and metric gap program

## Phase 3: Scale and differentiation

16. Migration and compatibility layer
17. API, webhooks, and MCP
18. AI separation and BYOK clarity
19. Contextual help and guided troubleshooting
20. Full product and support instrumentation loop

---

## Product leadership recommendation

If we are ruthless, the rebuild should be sold internally as a trust-and-operability rebuild, not a feature rebuild.

That means the product team should optimise for:
- fewer support tickets per active account
- fewer connector failures per connected account
- higher percentage of successful scheduled deliveries
- lower time-to-first-trusted-report
- fewer permission and access escalations
- higher white-label setup success rate

These are the measures most aligned with what Gleap says is actually hurting customers.

---

## Final recommendation

Do not let the rebuild get distracted by cosmetic improvements while the core agency workflows remain fragile.

The most important work is not making Oviond look more modern. It is making Oviond feel dependable.

If the rebuilt product can reliably connect data, preserve permissions, render consistently, deliver branded reports cleanly, and make failure states obvious, it will solve the biggest recurring causes of support pain and give Oviond a far stronger foundation for retention and growth.

---

## Appendix: Representative recurring issue examples from the Gleap research

Examples seen during the analysis included:
- Custom Domain Request
- Custom Domain Not Functioning
- Custom Report Domain Connection Failure
- Dashboard sent via automation does not show data and date range does not match project
- Bug Fix Assistance - not able to assign clients to team members in User Permissions
- Unable to save custom table sorting
- Issue with custom calculations
- Filtering option missing in GA4 filter
- Google Ads Conversion Actions Connection Issue in Shared Report
- Google Business Profile Search Terms data is not pulling through
- AI Assistant Non-Functional After Custom API Key Setup
- Cannot Connect Shopify as Data Source
- Deleted project still appearing as active
- PDF not downloading
- PDF Report Generation Failure
- Unable to Authenticate Microsoft Ads Connection - Advice needed

These are not isolated oddities. They line up tightly with the broader theme counts and search behaviour across the full support history.
